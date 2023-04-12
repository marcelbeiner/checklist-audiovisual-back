from pydantic import BaseModel
from model.checklist import Checklist

class CheckListSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Guitarrda"
    valor: float = 250.00
    serial_number: str = "KGXY"
    observacao: str = "produto novo"


def apresenta_checklist(checklist: Checklist):
    return{
        'id': checklist.id,
        'nome': checklist.nome,
        'valor': checklist.valor,
        'serial_number': checklist.serial_number,
        'observacao': checklist.observacao
    }