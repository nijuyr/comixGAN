import os
from subprocess import call

VIDEO_DIR = os.path.join('data', 'videos')
FRAMES_DIR = os.path.join('data', 'images')

for video in os.listdir(VIDEO_DIR):
    video_name = video.split('.mp4')[0]
    os.mkdir(os.path.join(FRAMES_DIR, video_name))
    call(["ffmpeg", "-skip_frame", "nokey", "-i", os.path.join(VIDEO_DIR, video), "-vsync", "0", "-qscale:v", "1", "-f", "image2", os.path.join(FRAMES_DIR, video_name, "%06d.jpeg")])

