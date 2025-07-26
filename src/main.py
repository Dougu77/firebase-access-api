# Imports
from models.response import *
from typing import List
from scripts.routes import Routes
import firebase_admin
import fastapi

# Criação do app da API
app = fastapi.FastAPI()

# Configuração da conexão com o Firebase
cred = firebase_admin.credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred)

# Criação do objeto da classe de rotas
routes = Routes()

# Criação das rotas
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
    return routes.get_all_pessoas()
