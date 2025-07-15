from transformers import pipeline
from typing import Dict

# Load zero-shot classifier once
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define your supported intents
INTENT_LABELS = [
    "set_alarm",
    "get_alarm",
    "cancel_alarm",
    "get_meeting_schedule",
    "add_calendar_event",
    "track_amazon_shipment",
    "track_flipkart_shipment",
    "greeting",
    "goodbye",
    "unknown"
]

def detect_intent(text: str) -> Dict:
    result = classifier(text, INTENT_LABELS)
    return {
        "intent": result["labels"][0],
        "confidence": result["scores"][0],
        "raw_result": result
    }
