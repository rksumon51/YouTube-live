import os

STREAM_KEY = "z96x-91ph-1gmj-d9sx-1hy2"

VIDEO_EXTENSIONS = (".mp4", ".mkv", ".mov", ".webm", ".avi", ".flv", ".m4v")

def create_playlist():
    videos = [f for f in os.listdir() if f.lower().endswith(VIDEO_EXTENSIONS)]

    with open("playlist.txt", "w") as f:
        for video in videos:
            f.write(f"file '{video}'\n")

while True:
    create_playlist()

    cmd = f"""ffmpeg -re -fflags +genpts -err_detect ignore_err \
    -f concat -safe 0 -i playlist.txt \
    -vf scale=720:1280 \
    -vsync 1 -async 1 \
    -c:v libx264 -preset veryfast -b:v 1800k -maxrate 1800k -bufsize 3600k \
    -pix_fmt yuv420p \
    -c:a aac -b:a 128k \
    -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"""

    os.system(cmd)
