from twilio.twiml.messaging_response import MessagingResponse
from database.mongo_handler import save_registration, get_events

def handle_message(message, sender):
    resp = MessagingResponse()
    msg = resp.message()

    if "register" in message:
        # extract and save registration
        save_registration(sender, message)
        msg.body("✅ Registered for the event!")
    elif "events" in message:
        events = get_events()
        msg.body(f"📅 Upcoming Events:\n" + "\n".join(events))
    else:
        msg.body("Send 'events' to view or 'register <event>' to join.")
    
    return str(resp)
