from models import db, Enrollment
from datetime import datetime

def enroll_client_service(client_id, program_id, notes=None):
    # Check for existing active enrollment
    existing = Enrollment.query.filter_by(
        client_id=client_id,
        program_id=program_id,
        active=True
    ).first()
    
    if existing:
        raise ValueError("Client already enrolled in this program")
    
    enrollment = Enrollment(
        client_id=client_id,
        program_id=program_id,
        enrolled_at=datetime.utcnow(),
        active=True,
        notes=notes
    )
    db.session.add(enrollment)
    db.session.commit()
    return enrollment

def update_enrollment_status(enrollment_id, active):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    enrollment.active = active
    enrollment.status_changed_at = datetime.utcnow()
    db.session.commit()
    return enrollment
