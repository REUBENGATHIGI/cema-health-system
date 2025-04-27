from flask import Blueprint, request, jsonify
from app.services.program_service import create_program, get_all_programs
from app.schemas import ProgramSchema

programs_bp = Blueprint('programs_bp', __name__)

@programs_bp.route('/programs', methods=['POST'])
def register_program():
    data = request.get_json(); name = data.get('name')
    if not name: return jsonify({'error':'Name required'}),400
    program = create_program(name)
    return ProgramSchema().jsonify(program),201

@programs_bp.route('/programs', methods=['GET'])
def list_programs():
    progs = get_all_programs()
    return ProgramSchema(many=True).jsonify(progs)
