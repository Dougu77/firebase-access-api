from google.cloud.firestore import DocumentSnapshot
import firebase_admin.firestore
from models.response import *
from typing import List

class Routes():
    
    def __init__(self):
        self.database = firebase_admin.firestore.client()

    def get_all_collection(self, name:str) -> List[DocumentSnapshot]:
        return self.database.collection(name).stream()

    def get_all_pessoas(self) -> List[Pessoas]:
        return [Pessoas(**doc.to_dict()) for doc in self.get_all_collection('Pessoas')]
