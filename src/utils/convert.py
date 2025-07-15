from pydub import AudioSegment
import uuid

def convert_to_pcm_wav(input_path: str) -> str:
    # Load with pydub (supports mp3, wav, m4a, etc.)
    audio = AudioSegment.from_file(input_path)

    # Force correct format for Vosk
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)

    output_path = f"/tmp/{uuid.uuid4().hex}.wav"
    audio.export(output_path, format="wav")
    return output_path