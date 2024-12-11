import speech_recognition as sr
from pydub import AudioSegment
import time
import os

# Offline transcription using CMU Sphinx
def transcribe_audio_with_sphinx(wav_file):
    print("Transcribing audio with CMU Sphinx...")
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("start time: ", start_time)
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file) as source:
            print("Loading audio file...")
            # Process the audio file in chunks
            chunk_duration = 30  # seconds
            offset = 0
            with open("transcription.txt", "w") as file:
                while True:
                    # Check if there is enough audio left to read
                    source_duration = source.DURATION
                    if offset >= source_duration:
                        break
                    remaining_duration = source_duration - offset
                    current_chunk_duration = min(chunk_duration, remaining_duration)
                    
                    audio_data = recognizer.record(source, duration=current_chunk_duration, offset=offset)
                    # Recognize speech using Sphinx and write to file
                    text = recognizer.recognize_sphinx(audio_data)
                    file.write(text + "\n")
                    offset += current_chunk_duration
                    print(f"Processed {offset} seconds of audio")

    except Exception as e:
        print(f"An error occurred: {e}")

# Transcribe the WAV file
transcribe_audio_with_sphinx("mindset.wav")