from flask import Blueprint, request, jsonify
from services.program_service import *
from schemas import ProgramSchema

programs_bp = Blueprint('programs', __name__, url_prefix='/api/programs')
program_schema = ProgramSchema()
programs_schema = ProgramSchema(many=True)

@programs_bp.route('/', methods=['POST'])
def create_program():
    data = request.get_json()
    program = create_program_service(data)
    return program_schema.jsonify(program), 201

@programs_bp.route('/', methods=['GET'])
def get_programs():
    programs = get_all_programs_service()
    return programs_schema.jsonify(programs)

@programs_bp.route('/<int:program_id>', methods=['GET'])
def get_program(program_id):
    program = get_program_by_id_service(program_id)
    return program_schema.jsonify(program)
