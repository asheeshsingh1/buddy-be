from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from src.services import speech
import uuid
import os
from src.utils.intent_processor import detect_intent
from src.utils.response_selector import select_response


router = APIRouter()

UPLOAD_DIR = "storage/uploads"
RESPONSE_DIR = "storage/responses"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESPONSE_DIR, exist_ok=True)


@router.post("/talk")
async def talk(background_tasks: BackgroundTasks, audio: UploadFile = File(...)):
    try:
        # Filter the request if not valid
        if audio is None or audio.filename == "":
            raise HTTPException(status_code=400, detail="No audio file was provided.")
        if not audio.content_type.startswith("audio/"):
            raise HTTPException(status_code=400, detail="Uploaded file must be an audio file.")
        
        # Save uploaded audio
        file_id = str(uuid.uuid4())
        input_path = f"{UPLOAD_DIR}/{file_id}_{audio.filename}"
        with open(input_path, "wb") as f:
            f.write(await audio.read())

        # Transcribe speech to text & detect intent
        transcription = speech.transcribe_vosk(input_path)        
        intent_result = detect_intent(transcription)

        # Route to appropriate response (simple echo for now)
        response_text = select_response(intent_result["intent"],transcription=transcription)

        # Generate TTS response
        output_path = f"{RESPONSE_DIR}/response_{file_id}.mp3"
        background_tasks.add_task(speech.generate_speech, response_text, output_path)

        return JSONResponse({
            "transcript": transcription,
            "intent": intent_result["intent"],
            "confidence": intent_result["confidence"],
            "response": response_text
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
