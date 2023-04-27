from pydantic import BaseModel
from model.checklist import Checklist
from typing import List

class CheckListSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str
    valor: float
    serial_number: str
    observacao: str

class ChecklistBuscaSchema(BaseModel):
    checklist_id: int


def apresenta_checklist(checklist: Checklist):
    return{
        'id': checklist.id,
        'nome': checklist.nome,
        'valor': checklist.valor,
        'serial_number': checklist.serial_number,
        'observacao': checklist.observacao
    }
def apresenta_checklists(checklists: List[Checklist]):
    """ Retorna uma representação dos equipamentos seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for checklist in checklists:
        result.append({
            "id": checklist.id,
            "nome": checklist.nome,
            "valor": checklist.valor,
            "serial_number": checklist.serial_number,
            "observacao": checklist.observacao
        })

    return {"checklists": result}