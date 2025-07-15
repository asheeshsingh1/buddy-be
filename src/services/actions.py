from src.services.alarms.alarms import AlarmHandler

def handle_set_alarm(transcription: str) -> str:
    alarm = AlarmHandler()
    return alarm.handle_set_alarm(transcription=transcription)

def handle_cancel_alarm(transcription: str) -> str:
    alarm = AlarmHandler()
    return alarm.handle_cancel_alarm(transcription=transcription)

def handle_flipkart_status() -> str:
    return ""