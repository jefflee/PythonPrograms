import yt_dlp
from openai import OpenAI
from pydub import AudioSegment

# 設定要下載的影片 URL
youTubeUrl = "https://www.youtube.com/watch?v=_cfbv5G-brk"
# youTubeUrl = "https://www.youtube.com/watch?v=2qKcr99hEeQ"


def download_audio(url):
    # 設定下載選項
    ydl_opts = {
        'format': 'bestaudio/best',  # 只下載最佳音質的音訊
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # 轉換為 mp3 格式
            'preferredquality': '192',  # 設定音質為 192kbps
        }],
        'outtmpl': f'output/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # 取得檔案標題並加上副檔名
        filename = f'output/{info['title']}.mp3'
        return filename


fileName = download_audio(youTubeUrl)

# 讀取下載下來的音檔
audio_file = AudioSegment.from_file(fileName)

print('Strat to do transcription')

# 切割音檔成多個小檔案
chunk_size = 100 * 1000  # 100 秒
chunks = [audio_file[i:i + chunk_size]
          for i in range(0, len(audio_file), chunk_size)]

# 使用 OpenAI 的 Audio API 將每個小檔案轉成文字，然後合併在一起
client = OpenAI()
transcript = ""
for chunk in chunks:
    with chunk.export("output/temp.mp3", format="mp3") as f:
        result = client.audio.transcriptions.create(model="whisper-1", file=f)
        transcript += result.text

print(transcript)


# 依照我們指定的長度分割字串
def split_text(text, max_length):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


# 依照 type 處理文字
def process_text(text, type):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": type + text}
        ]
    )
    return response.choices[0].message.content


# 處理長字串
def process_long_text(long_text, type):
    text_list = split_text(long_text, 1200)
    processed_text_list = [process_text(text, type) for text in text_list]
    return "".join(processed_text_list)


print('Start refinement')

# Translate to Chinese
# if translateToChinese:
#     processed_transcript = process_long_text(transcript, "請翻譯成繁體中文閱讀：\n")

# 呼叫分段處理函式
processed_transcript = process_long_text(transcript, "若不是繁體中文，請先翻譯成繁體中文，再使用繁體中文閱讀，幫我改錯字、加標點符號，並分段使內容更通順：\n")

# 呼叫取得摘要函式
processed_summary = process_long_text(processed_transcript, "閱讀以下文字，用「-」作為前綴條列出重點，用「繁體中文」呈現：\n")

output = "摘要：\n" + processed_summary + "\n\n\n逐字稿：\n" + processed_transcript
print(output)

with open("output/text.txt", "w", encoding="utf-8") as file:
    file.write(output)

print('Finished')
