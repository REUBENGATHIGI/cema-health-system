from models import db, Program

def create_program_service(program_data):
    program = Program(
        name=program_data['name'],
        description=program_data.get('description', '')
    )
    db.session.add(program)
    db.session.commit()
    return program

def get_all_programs_service():
    return Program.query.all()

def get_program_by_id_service(program_id):
    return Program.query.get_or_404(program_id)
