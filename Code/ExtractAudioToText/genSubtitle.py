#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: generate_subtitle
# date: "2024-01-30"
# description: "將一個長影片分割成小的mp3檔後，針對每一個mp3檔產生.srt檔，最後再合併所有內容成一個srt"
# author: Hsieh-Ting Lin, the Lizard 🦎

import argparse
import os
import tempfile
import time

from moviepy import VideoFileClip
from openai import OpenAI


def split_video(video_path, temp_dir, duration=300):
    print("\033[92m開始分割成每五分鐘一個的mp3檔！\033[0m")
    video = VideoFileClip(video_path)
    for i in range(0, int(video.duration), duration):
        chunk_filename = os.path.join(temp_dir, f"chunk_{i//duration}.mp3")
        clip = video.subclipped(i, min(i + duration, int(video.duration)))
        clip.audio.write_audiofile(chunk_filename)


def generate_subtitles(temp_dir):
    # client = OpenAI(api_key="your_key")
    client = OpenAI()
    files = [
        os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith(".mp3")
    ]
    all_subtitles = []
    print("\033[92m連結OpenAI whisper-1 API產生字幕檔\033[0m")

    for index, file in enumerate(files):
        with open(file, "rb") as audio_file:
            print(f"\033[92m讀入{os.path.basename(file)}\033[0m")
            start_time = time.time()
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="srt",
            )
            if isinstance(response, str):
                offset = index * 300 * 1000  # 300 seconds in milliseconds
                adjusted_subtitle = adjust_timing(response, offset)
                adjusted_subtitle = process_text(client, adjusted_subtitle, "請把以下內容翻譯成繁體中文 \n")
                all_subtitles.append(adjusted_subtitle)
                end_time = time.time()
                # 計算並列印整個過程所需的時間
                total_time = end_time - start_time
                print(f"∟整個過程共花費了 {total_time:.1f} 秒。")
            else:
                print(f"Failed to transcribe {file}")
                print("Response:", response)  # Print the API response

    return all_subtitles


def process_text(client, text, type):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": type + text}
        ]
    )
    return response.choices[0].message.content

def adjust_timing(subtitle, offset):
    new_subtitle = []
    for line in subtitle.split("\n"):
        if "-->" in line:
            start, end = line.split(" --> ")
            new_start = adjust_time(start, offset)
            new_end = adjust_time(end, offset)
            new_subtitle.append(f"{new_start} --> {new_end}")
        else:
            new_subtitle.append(line)
    return "\n".join(new_subtitle)


def adjust_time(time_str, offset):
    hours, minutes, seconds_milliseconds = time_str.split(":")
    seconds, milliseconds = seconds_milliseconds.split(",")

    total_milliseconds = (
        int(milliseconds)
        + (int(seconds) + (int(minutes) + int(hours) * 60) * 60) * 1000
    )
    total_milliseconds += offset

    new_hours = total_milliseconds // 3600000
    total_milliseconds %= 3600000
    new_minutes = total_milliseconds // 60000
    total_milliseconds %= 60000
    new_seconds = total_milliseconds // 1000
    new_milliseconds = total_milliseconds % 1000

    return f"{new_hours:02}:{new_minutes:02}:{new_seconds:02},{new_milliseconds:03}"


def merge_subtitles(subtitles):
    combined_subtitles = "\n".join(subtitles)
    return reindex_subtitles(combined_subtitles)


def reindex_subtitles(srt_content):
    lines = srt_content.split("\n")
    new_content = []
    index = 1

    for line in lines:
        if line.isdigit():
            new_content.append(str(index))
            index += 1
        else:
            new_content.append(line)

    return "\n".join(new_content)


def main(video_path):
    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    start_time = time.time()
    with tempfile.TemporaryDirectory() as temp_dir:
        split_video(video_path, temp_dir)
        subtitles = generate_subtitles(temp_dir)
        final_subtitles = merge_subtitles(subtitles)
        srt_filename = f"{video_filename}.srt"
        with open(srt_filename, "w", encoding="utf-8") as file:
            file.write(final_subtitles)
    print(f"\033[92m✔ 合併字幕檔{os.path.basename(srt_filename)}已完成！\033[0m")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"∟整個過程共花費了 {total_time:.1f} 秒。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate subtitles for a video.")
    parser.add_argument("-i", "--input", help="Input video file", required=True)
    args = parser.parse_args()

    main(args.input)