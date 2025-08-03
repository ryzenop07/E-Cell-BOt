import re

def format_event_list(events):
    return "\n".join([f"- {event}" for event in events])

def extract_event_name(message):
    # e.g. "register ideathon" → "ideathon"
    match = re.search(r'register\s+(.+)', message.lower())
    if match:
        return match.group(1).strip()
    return None

def is_valid_phone(phone):
    return phone.startswith("whatsapp:")  # Twilio format
