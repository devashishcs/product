from flask import Blueprint, jsonify
from service.data_extraction import load_data, get_columns, group_by_po_number, total_sales_by_sku
# Create a blueprint
quickcom = Blueprint("quickcom", __name__)

# Define a simple route
@quickcom.route("/ping", methods=["GET"])
def ping():
    sheets = load_data()
    data = {name: df.to_dict(orient="records") for name, df in sheets.items()}
    #Json structue
    return jsonify(data), 200

@quickcom.route("/get_coloumn", methods=["GET"])
def get_coloumn():
    data = get_columns() 
    return jsonify(data), 200

@quickcom.route("/group_by_po_number", methods=["GET"])
def by_POnumber():
    data = group_by_po_number() 
    return jsonify(data), 200

@quickcom.route("/sales_by_sku", methods=["GET"])
def by_sku():
    data = total_sales_by_sku() 
    return jsonify(data), 200