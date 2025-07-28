from google.cloud.firestore import DocumentSnapshot
import firebase_admin.firestore
from models.response import *
from typing import List, Any
from models.consts import *

class FirebaseRequests():

    # Contrutor
    def __init__(self):

        # Configuração da conexão com o Firebase
        cred = firebase_admin.credentials.Certificate('firebase_key.json')
        firebase_admin.initialize_app(cred)
        self.database = firebase_admin.firestore.client()

    # Métodos genéricos
    def get_all_collection(self, name:str) -> List[DocumentSnapshot]:
        return self.database.collection(name).stream()

    def get_documents_by_parameter(self, collection:str, parameter:str, operator:FirestoreOperator, value:Any) -> List[DocumentSnapshot]:
        return self.database.collection(collection).where(parameter, operator.value, value).stream()

    # Pessoas
    def get_all_pessoas(self) -> List[Pessoas]:
        return [Pessoas(**doc.to_dict()) for doc in self.get_all_collection('Pessoas')]

    def get_pessoa_by_parameter(self, parameter:str, operator:FirestoreOperator, value:Any) -> List[Pessoas]:
        return [Pessoas(**doc.to_dict()) for doc in self.get_documents_by_parameter('Pessoas', parameter, operator, value)]
