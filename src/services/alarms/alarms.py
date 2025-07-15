import re

class AlarmHandler:

    # def __init__(self):
    NUM_WORDS = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12
    }

    @staticmethod
    def handle_set_alarm(transcription: str) -> str:
        transcription = transcription.lower()

        # First, try normal numeric format
        match = re.search(r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", transcription)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2)) if match.group(2) else 0
            period = match.group(3).upper() if match.group(3) else "AM"
            return f"Setting an alarm for {hour}:{minute:02d} {period}"

        # Second, try word-based match: e.g., "seven am"
        for word, num in AlarmHandler.NUM_WORDS.items():
            if f"{word} am" in transcription or f"{word} a m" in transcription:
                return f"Setting an alarm for {num:02d}:00 AM"
            elif f"{word} pm" in transcription or f"{word} p m" in transcription:
                return f"Setting an alarm for {num:02d}:00 PM"

        return "What time should I set the alarm for?"

    @staticmethod
    def handle_cancel_alarm(transcription: str) -> str:
        transcription = transcription.lower()

        # Try numeric time format (e.g., "cancel alarm for 7:30 am")
        match = re.search(r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", transcription)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2)) if match.group(2) else 0
            period = match.group(3).upper() if match.group(3) else "AM"
            return f"Cancelling the alarm set for {hour}:{minute:02d} {period}."

        # Try word-based time format (e.g., "cancel alarm for seven am")
        for word, num in AlarmHandler.NUM_WORDS.items():
            if f"{word} am" in transcription or f"{word} a m" in transcription:
                return f"Cancelling the alarm set for {num:02d}:00 AM."
            elif f"{word} pm" in transcription or f"{word} p m" in transcription:
                return f"Cancelling the alarm set for {num:02d}:00 PM."

        # If no time is mentioned, cancel all or prompt
        if "cancel all alarms" in transcription or "delete all alarms" in transcription:
            return "Cancelling all alarms."

        return "I couldn't understand which alarm to cancel. Please specify a time."