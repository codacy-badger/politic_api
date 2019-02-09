import os , urllib.request
import functools , json , pprint
from .office_model import add_office , get_offices , get_office
from flask import(
    Blueprint, request, url_for, Response,jsonify
)
   
#create a Blueprint named office
#the blueprint needs to know where its defines __name__ is passed as the second argument
bp = Blueprint('office', __name__, url_prefix='/api/v1/office')



@bp.route('', methods = ['POST'])
def office_list():
    if request.method == 'POST':
        data = request.get_json()       
        if data == None:
            return jsonify({"result": "failure", "error":"400", "message":"Bad Request: Ensure that your data is in JSON format"}), 400
        add_office(data)
        return jsonify({'status':201,'data':data})
    
    
