import youtube_dl

# Set the URL of the YouTube video to download
url = "https://www.youtube.com/watch?v=SY2kZjVEd54"

# Create an instance of the YouTube Downloader
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

# Set the download options
opts = {
    'format': 'best',  # Select the highest resolution
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Extract audio from the video
        'preferredcodec': 'mp3',  # Save audio as an MP3 file
        'preferredquality': '192',  # Set the audio quality to 192kbps
    }]
}

# Download the video
ydl.download([url])
