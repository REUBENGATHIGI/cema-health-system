from flask import Blueprint, request, jsonify
from app.services.enrollment_service import enroll_client
from app.schemas import EnrollmentSchema

enrollments_bp = Blueprint('enrollments_bp', __name__)

@enrollments_bp.route('/enrollments', methods=['POST'])
def enroll():
    data = request.get_json()
    cid = data.get('client_id'); pid = data.get('program_id')
    if not cid or not pid: return jsonify({'error':'client_id & program_id required'}),400
    enrollment = enroll_client(cid, pid)
    return EnrollmentSchema().jsonify(enrollment),201
