from typing import Literal
from enum import Enum

# Enums
class FirestoreOperator(str, Enum):
    '''
    Tipos de operadores aceitos na filtragem de dados do Firestore
    '''
    
    EQUAL = '=='
    NOT_EQUAL = '!='
    GREATER_THAN = '>'
    GREATER_THAN_EQUAL = '>='
    LESS_THAN = '<'
    LESS_THAN_EQUAL = '<='
    IN_LIST = 'in'
    ARRAY_CONTAINS = 'array-contains'

# Constantes
PESSOAS_FIELDS = Literal['idade', 'nome', 'sexo']
