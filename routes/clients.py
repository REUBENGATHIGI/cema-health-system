from flask import Blueprint, request, jsonify
from services.client_service import *
from schemas import ClientSchema

clients_bp = Blueprint('clients', __name__, url_prefix='/api/clients')
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)

@clients_bp.route('/', methods=['POST'])
def create_client():
    data = request.get_json()
    client = create_client_service(data)
    return client_schema.jsonify(client), 201

@clients_bp.route('/', methods=['GET'])
def get_clients():
    clients = get_all_clients_service()
    return clients_schema.jsonify(clients)

@clients_bp.route('/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = get_client_by_id_service(client_id)
    return client_schema.jsonify(client)

@clients_bp.route('/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    client = update_client_service(client_id, data)
    return client_schema.jsonify(client)

@clients_bp.route('/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    delete_client_service(client_id)
    return jsonify({'message': 'Client deleted'}), 200

@clients_bp.route('/search', methods=['GET'])
def search_clients():
    query = request.args.get('q')
    clients = search_clients_service(query)
    return clients_schema.jsonify(clients)
