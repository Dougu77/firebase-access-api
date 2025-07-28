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
    return 'Bem vindo(a) a API'

@app.post('/pessoas', response_model=List[Pessoas])
def pessoas() -> List[Pessoas]:
    '''
    Busca todos os registros dentro da coleção "Pessoas"

    Returns:
        List[Pessoas]: Registros
    '''
    return requests.get_all_pessoas()

@app.post('/pessoas/{parameter}/{operator}/{value}', response_model=List[Pessoas])
def pessoas_by_parameter(parameter:PESSOAS_FIELDS, operator:FirestoreOperator, value:Any) -> List[Pessoas]:
    
    return requests.get_pessoa_by_parameter(parameter, operator, value)
