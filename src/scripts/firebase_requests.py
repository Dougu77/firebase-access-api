from google.cloud.firestore import DocumentSnapshot
from typing import List, Any, Type, Iterable, cast
import firebase_admin.firestore
from pydantic import BaseModel
from models.response import *
from models.consts import *

class FirebaseRequests():

    # Contrutor
    def __init__(self):

        # Configuração da conexão com o Firebase
        cred = firebase_admin.credentials.Certificate('firebase_key.json')
        firebase_admin.initialize_app(cred)
        self.database = firebase_admin.firestore.client()

    # Métodos genéricos
    def get_list(self, documents:Iterable[DocumentSnapshot]) -> List[GENERIC_BASE_MODEL]:
        result: List[GENERIC_BASE_MODEL] = []
        for doc in documents:
            data = doc.to_dict()
            data['id'] = doc.id
            result.append(data)
        return result
    
    def get_value_type(field_type: Type[Any], value: Any) -> Any:
        if field_type is int:
            return int(value)
        elif field_type is float:
            return float(value)
        elif field_type is bool:
            return str(value).lower() in ('true', '1', 'on') if isinstance(value, str) else bool(value)
        elif field_type is str:
            return str(value)
        else:
            return value
    
    def read_all_collection(self, model:Type[GENERIC_BASE_MODEL]) -> List[GENERIC_BASE_MODEL]:
        documents = cast(
            Iterable[DocumentSnapshot],
            self.database.collection(model.__name__).stream()
        )
        return self.get_list(documents)

    def read_documents_by_parameter(
        self,
        model:Type[GENERIC_BASE_MODEL],
        parameter:str,
        operator:FirestoreOperator,
        value:Any
        ) -> List[GENERIC_BASE_MODEL]:
            field_type = model.model_fields[parameter].annotation
            value = self.get_value_type(field_type, value)
            if parameter == 'id':
                document = self.database.collection(model.__name__).document(value).get()
                return self.get_list([document])
            else:
                documents = cast(
                    Iterable[DocumentSnapshot],
                    self.database.collection(model.__name__).where(parameter, operator.value, value).stream()
                )
                return self.get_list(documents)
    
    def create_document(self, value:BaseModel) -> str:
        new_document = self.database.collection(value.__class__.__name__).document()
        new_document.set(value.model_dump())
        return new_document.id
