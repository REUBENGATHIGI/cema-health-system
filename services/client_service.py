from models import db, Client
from datetime import datetime
from sqlalchemy import or_
from difflib import SequenceMatcher

def create_client_service(client_data):
    # Input validation
    required_fields = ['first_name', 'last_name', 'date_of_birth', 'gender']
    if not all(field in client_data for field in required_fields):
        raise ValueError("Missing required fields")
    
    client = Client(
        first_name=client_data['first_name'],
        last_name=client_data['last_name'],
        date_of_birth=datetime.strptime(client_data['date_of_birth'], '%Y-%m-%d').date(),
        gender=client_data['gender'],
        contact_number=client_data.get('contact_number'),
        email=client_data.get('email'),
        address=client_data.get('address')
    )
    db.session.add(client)
    db.session.commit()
    return client

def fuzzy_search_clients(query, threshold=0.6):
    all_clients = Client.query.all()
    results = []
    for client in all_clients:
        full_name = f"{client.first_name} {client.last_name}"
        ratio = SequenceMatcher(None, query.lower(), full_name.lower()).ratio()
        if ratio >= threshold:
            results.append((client, ratio))
    return sorted(results, key=lambda x: x[1], reverse=True)

def get_client_history(client_id):
    from models import Enrollment, Program
    return db.session.query(Enrollment, Program)\
        .join(Program, Enrollment.program_id == Program.id)\
        .filter(Enrollment.client_id == client_id)\
        .order_by(Enrollment.enrolled_at.desc())\
        .all()
