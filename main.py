from flask import Flask, request
import sounddevice as sd
import scipy.io.wavfile as wavfile

app = Flask(__name__)

audio_frames = []
audio_samplerate = 44100
audio_channels = 1
audio_duration = 5

def start_recording():
    global audio_frames
    audio_frames = sd.rec(int(audio_samplerate * audio_duration), samplerate=audio_samplerate, channels=audio_channels)

def stop_recording():
    global audio_frames
    wavfile.write("recording.wav", audio_samplerate, audio_frames)

@app.route("/start_recording", methods=["POST"])
def start_recording_route():
    start_recording()
    return "Recording started"

@app.route("/stop_recording", methods=["POST"])
def stop_recording_route():
    stop_recording()
    return "Recording stopped"

if __name__ == "__main__":
    app.run()