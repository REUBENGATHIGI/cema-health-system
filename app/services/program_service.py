from app.models import Program
from app import db

def create_program(name):
    program = Program(name=name)
    db.session.add(program)
    db.session.commit()
    return program

def get_all_programs():
    return Program.query.all()
