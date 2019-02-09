import os , urllib.request
import functools , json , pprint
from .party_model import add_party , get_parties, get_party
from flask import(
    Blueprint, request, url_for, Response,jsonify
)
   
#create a Blueprint named party
#the blueprint needs to know where its defines __name__ is passed as the second argument
bp = Blueprint('party', __name__, url_prefix='/api/v1/party')

@bp.route('', methods = ['GET','POST'])
def party_list():
   if request.method == 'POST':
        data = request.get_json()       
        if data == None:
            return jsonify({"result": "failure", "error":"400", "message":"Bad Request: Ensure that your data is in JSON format"}), 400
        add_party(data)
        return jsonify({'status':201,'data':data})
   elif request.method == 'GET':
        data = get_parties()
        return jsonify({'status':200,'data':data})
    

@bp.route('/<int:id>', methods = ['GET'])
def get_a_party(id):
    if request.method == 'GET':
        data = get_party(id)
        if data == None:
            return jsonify({"result": "failure", "error":"404", "message":"The reqested resource not found"}), 404
        return jsonify({'status':200,'data':data})
   