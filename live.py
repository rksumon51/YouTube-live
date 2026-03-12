import os

STREAM_KEY = "YOUR_STREAM_KEY"

while True:
    cmd = f"ffmpeg -re -f concat -safe 0 -i playlist.txt -vf scale=720:1280 -c:v libx264 -preset veryfast -b:v 1800k -maxrate 1800k -bufsize 3600k -pix_fmt yuv420p -c:a aac -b:a 128k -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    
    os.system(cmd)
