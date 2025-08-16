from flask import Blueprint, jsonify
from service.data_extraction import load_data
# Create a blueprint
quickcom = Blueprint("quickcom", __name__)

# Define a simple route
@quickcom.route("/ping", methods=["GET"])
def ping():
    sheets = load_data()  # returns a DataFrame
    data = {name: df.to_dict(orient="records") for name, df in sheets.items()}
    
    return jsonify(data), 200