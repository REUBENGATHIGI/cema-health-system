from app.models import Enrollment
from app import db

def enroll_client(client_id, program_id):
    enrollment = Enrollment(client_id=client_id, program_id=program_id)
    db.session.add(enrollment)
    db.session.commit()
    return enrollment
