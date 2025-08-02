# Imports
from scripts.firebase_requests import FirebaseRequests
from models.response import *
from typing import List, Any
from fastapi import FastAPI
from models.consts import *

# Variáveis
app = FastAPI()
requests = FirebaseRequests()

# Rotas
@app.get('/')
def home() -> str:
    return 'Bem vindo(a) a API.\nUtilize /docs para ver todos os endpoints da API.'

@app.post('/pessoas', response_model=List[Pessoas])
def read_pessoas() -> List[Pessoas]:
    '''
    Busca todos os registros dentro da coleção "Pessoas"

    Returns:\n
        List[Pessoas]: Registros
    '''

    return requests.read_all_collection(Pessoas)

@app.post('/pessoas/{parameter}/{operator}/{value}', response_model=List[Pessoas])
def read_pessoas_by_parameter(
    parameter:PESSOAS_FIELDS,
    operator:FirestoreOperator,
    value:Any
    ) -> List[Pessoas]:
    '''
    Busca registros específicos dentro da coleção "Pessoas"
    
    Args:\n
        parameter (PESSOAS_FIELDS): Campo da tabela
        operator (FirestoreOperator): Operador de comparação
        value (Any): Valor de comparação

    Returns:\n
        List[Pessoas]: Lista de Pessoas
    '''

    return requests.read_documents_by_parameter(Pessoas, parameter, operator, value)

@app.post('/pessoas/create', response_model=str)
def create_pessoas(pessoa:Pessoas) -> str:
    '''
    Cria um registro na coleção "Pessoas

    Args:\n
        pessoa (Pessoas): Dados do novo registro

    Returns:\n
        str: ID do novo registro
    '''
    
    return requests.create_document(pessoa)
