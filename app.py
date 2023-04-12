from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect

from model import Session, Checklist
from schemas import *


info = Info(title = 'Checklist Audiovisual API', version = '1.0')
app = OpenAPI(__name__, info = info)


@app.get('/')
def home():
    return redirect('/openapi')

@app.post('/checklist')
def add_checklist(form: CheckListSchema):
    checklist = Checklist(
        nome = form.nome,
        valor = form.valor,
        serial_number = form.serial_number,
        observacao = form.observacao
    )
    
    try:
        session = Session()
        session.add(checklist)
        session.commit()
        
        return 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400
    