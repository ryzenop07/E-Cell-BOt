import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")  # e.g. whatsapp:+14155238886

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")

# Other Config
ADMIN_PASS = os.getenv("ADMIN_PASS", "changeme123")  # Optional for basic auth
