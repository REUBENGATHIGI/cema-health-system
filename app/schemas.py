from app import ma

class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id','name')

class ProgramSchema(ma.Schema):
    class Meta:
        fields = ('id','name')

class EnrollmentSchema(ma.Schema):
    class Meta:
        fields = ('id','client_id','program_id')
