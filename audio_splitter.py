import os  # Import os for handling file paths
import cv2
import numpy as np
import librosa
import matplotlib.pyplot as plt
from moviepy.editor import *
from pydub import AudioSegment
from pydub.silence import split_on_silence  # Import the split_on_silence function
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("audio_processing.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

input_file_path = "/Users/harshayarravarapu/Documents/GitHub/Song_generator/data/THAMAN_LOVE_SONGS/thaman_love_songs1.mp3"


#Uncomment if you want to extract audio from the video file
# video_path = '/Users/harshayarravarapu/Documents/GitHub/Song_generator/data/THAMAN_LOVE_SONGS/thaman_love_songs1.mp4'  
# video = VideoFileClip(video_path)
# video.audio.write_audiofile("/Users/harshayarravarapu/Documents/GitHub/Song_generator/data/THAMAN_LOVE_SONGS/thaman_love_songs1.mp3")


try:
    # Load your audio
    song = AudioSegment.from_mp3(input_file_path)
    logging.info("Audio loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load audio: {e}")
    raise

# Split the audio into chunks based on silence
try:
    chunks = split_on_silence(
        song, 
        min_silence_len=500,  # Reduced to 1 second
        silence_thresh=song.dBFS - 30  # Set threshold dynamically
    )
    logging.info(f"Audio successfully split into {len(chunks)} chunks.")
except Exception as e:
    logging.error(f"Failed to split audio: {e}")
    raise

# Get the directory of the input file
output_directory = os.path.dirname(input_file_path)

# Print the number of chunks and their durations
for i, chunk in enumerate(chunks):
    logging.info(f"Chunk {i+1} duration: {len(chunk) / 1000:.2f} seconds")

# Save the chunks as separate audio files
for i, chunk in enumerate(chunks):
    try:
        output_file_path = os.path.join(output_directory, f"thaman_love_song_{i+28}.mp3")
        chunk.export(output_file_path, format="mp3")
        logging.info(f"Chunk {i+1} exported successfully to {output_file_path}.")
    except Exception as e:
        logging.error(f"Failed to export chunk {i+1}: {e}")
