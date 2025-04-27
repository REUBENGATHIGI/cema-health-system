from flask import Blueprint, request, jsonify
from services.enrollment_service import *
from schemas import EnrollmentSchema

enrollments_bp = Blueprint('enrollments', __name__, url_prefix='/api/enrollments')
enrollment_schema = EnrollmentSchema()
enrollments_schema = EnrollmentSchema(many=True)

@enrollments_bp.route('/', methods=['POST'])
def create_enrollment():
    data = request.get_json()
    enrollment = enroll_client_service(data['client_id'], data['program_id'])
    return enrollment_schema.jsonify(enrollment), 201

@enrollments_bp.route('/client/<int:client_id>', methods=['GET'])
def get_client_enrollments(client_id):
    enrollments = get_client_enrollments_service(client_id)
    return enrollments_schema.jsonify(enrollments)

@enrollments_bp.route('/program/<int:program_id>', methods=['GET'])
def get_program_enrollments(program_id):
    enrollments = get_program_enrollments_service(program_id)
    return enrollments_schema.jsonify(enrollments)
