FROM python:3.11-slim

# install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy project files
COPY . .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# start the live script
CMD ["python", "live.py"]
