from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.editor import VideoFileClip
import pysrt
# Load the video file
clip = VideoFileClip("test.mp4").fps()

# Load the subtitle file
subs = pysrt.open("dahwin.srt")

# Create a list of textclip with subtitles
subtitle_clips = [TextClip(sub.text, font='Arial', fontsize=24, color='white', align='center').set_duration(sub.end.seconds - sub.start.seconds) for sub in subs]

# Overlay the subtitles on the video
subbed_clip = concatenate_videoclips([clip]+subtitle_clips, method='compose')

# Write the output to a new file
subbed_clip.write_videofile("dahwin_substitle.mp4")

