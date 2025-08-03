from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["e_cell"]
registrations = db["registrations"]
events = db["events"]

def save_registration(sender, message):
    registrations.insert_one({"phone": sender, "message": message})

def get_events():
    return [event["name"] for event in events.find()]
