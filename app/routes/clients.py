from flask import Blueprint, request, jsonify
from app.services.client_service import create_client, get_all_clients, search_clients_by_name
from app.schemas import ClientSchema

clients_bp = Blueprint('clients_bp', __name__)

@clients_bp.route('/clients', methods=['POST'])
def register_client():
    data = request.get_json(); name = data.get('name')
    if not name: return jsonify({'error':'Name required'}),400
    client = create_client(name)
    return ClientSchema().jsonify(client),201

@clients_bp.route('/clients', methods=['GET'])
def list_clients():
    clients = get_all_clients()
    return ClientSchema(many=True).jsonify(clients)

@clients_bp.route('/clients/search', methods=['GET'])
def search_client():
    q = request.args.get('name')
    if not q: return jsonify({'error':'Query param name required'}),400
    results = search_clients_by_name(q)
    return ClientSchema(many=True).jsonify(results)
