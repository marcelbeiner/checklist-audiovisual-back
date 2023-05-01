from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect, request

from model import Session, Checklist
from schemas import *


info = Info(title = 'Checklist Audiovisual API', version = '1.0')
app = OpenAPI(__name__, info = info)
CORS(app)

@app.get('/')
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/checklist')
def add_checklist(form: CheckListSchema):
    """Adiciona um novo equipamento à base de dados

    Retorna uma representação dos equipamentos e comentários associados.
    """
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

        return apresenta_checklist(checklist), 200


    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Serial number de mesmo nome já salvo na base :"
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400
    
@app.get('/checklists')
def get_checklists():
    """Apresenta a Checklist de equipamentos audiovisuais e respectivas informações.
    """    
    
    session = Session()
    checklists = session.query(Checklist).all()
    if not checklists:
        return {"checklists":[]}, 200
    
    else: 
        print(checklists)
        return apresenta_checklists(checklists), 200

"""@app.get('/checklist')
def get_checklist(query: ChecklistBuscaSchema):
    checklist_id = query.checklist_id
    session = Session()
    checklist = session.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        return {"checklist":[]}, 200
    
    else: 
        print(checklist)
        return apresenta_checklist(checklist), 200"""
    
@app.delete('/checklist')
def del_checklist(query: ChecklistBuscaSchema):
    """Deleta um Equipamento a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    checklist_id = query.checklist_id
    session = Session()
    checklist = session.query(Checklist).filter(Checklist.id == checklist_id).delete()
    session.commit()
    
    if checklist:
        return {"message":"O checklist foi removido","id":checklist_id}
    else:
        return {"message":"O checklist não foi encontrado"}