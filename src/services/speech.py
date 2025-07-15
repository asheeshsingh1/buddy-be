import pyttsx3

from vosk import Model, KaldiRecognizer
import wave
import json


def generate_speech(text: str, output_path: str):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()


_model = None


def get_vosk_model():
    global _model
    if _model is None:
        import os

        model_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../models/english")
        )
        _model = Model(model_path)
    return _model


model = get_vosk_model()


def transcribe_vosk(audio_path: str) -> str:
    from ..utils.convert import convert_to_pcm_wav  # or inline if you prefer

    wav_path = convert_to_pcm_wav(audio_path)
    wf = wave.open(wav_path, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio must be WAV format PCM mono")

    model = get_vosk_model()
    rec = KaldiRecognizer(model, wf.getframerate())

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part = json.loads(rec.Result())
            results.append(part.get("text", ""))

    final = json.loads(rec.FinalResult())
    results.append(final.get("text", ""))

    return " ".join(results).strip()
