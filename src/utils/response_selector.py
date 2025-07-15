import random
from src.services.actions import (
    handle_set_alarm,
    handle_flipkart_status,
    handle_cancel_alarm
)

def select_response(intent: str, transcription: str) -> str:
    if intent == "greeting":
        return random.choice([
            "Hi there! What can I do for you?",
            "Hello! I'm here to help."
        ])

    elif intent == "set_alarm":
        return handle_set_alarm(transcription)
    
    elif intent == "cancel_alarm":
        return handle_cancel_alarm(transcription)

    elif intent == "track_flipkart_shipment":
        return handle_flipkart_status(transcription)

    elif intent == "goodbye":
        return random.choice([
            "Goodbye! Have a great day!",
            "Take care!"
        ])

    else:
        return "Sorry, I didn't quite get that?"
