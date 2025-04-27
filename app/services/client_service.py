from app.models import Client
from app import db

def create_client(name):
    client = Client(name=name)
    db.session.add(client)
    db.session.commit()
    return client

def get_all_clients():
    return Client.query.all()

def search_clients_by_name(q):
    return Client.query.filter(Client.name.ilike(f'%{q}%')).all()
