from pydantic import BaseModel
from model.checklist import Checklist

def apresenta_checklist(checklist: Checklist):
    return{
        'id': checklist.id,
        'nome': checklist.nome,
        'valor': checklist.valor,
        'serial_number': checklist.serial_number,
        'observacao': checklist.observacao
    }