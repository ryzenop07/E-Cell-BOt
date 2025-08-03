from flask import Blueprint, jsonify
from database.mongo_handler import registrations

admin = Blueprint('admin', __name__)

@admin.route("/admin/registrations")
def view_registrations():
    data = list(registrations.find({}, {'_id': 0}))
    return jsonify(data)
