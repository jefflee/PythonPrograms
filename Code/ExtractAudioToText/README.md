# Main.py

### Pre-Tasks

The main.py is base on this post

https://medium.com/dean-lin/%E7%94%A8-python-%E6%90%AD%E9%85%8D-openai-%E7%9A%84-gpt-whisper-api-%E5%8F%96%E5%BE%97-youtube-%E5%BD%B1%E7%89%87%E6%91%98%E8%A6%81-4ceb57828732

Set up OpenAI API key to system environment variables
```shell
setx OPENAI_API_KEY "Your_key"
```

Install python packages
```shell
pip install yt_dlp
pip install pydub
```

PS. If you have a problem while using yt-dlp to download audio file. You might need to install FFmpeg.

----
# genSubtitle.py

The genSubtitle.py is base on this post

https://htlin222.medium.com/whisper-ai-%E7%82%BA%E9%95%B7%E5%BD%B1%E7%89%87%E4%B8%8A%E5%AD%97%E5%B9%95%E7%9A%84%E6%96%B9%E6%B3%95-e9fd1705c1b7

Run it with is command
```shell
python genSubtitle.py -i C:\video.webm
```
