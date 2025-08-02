from typing import Literal, TypeVar
from pydantic import BaseModel
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
PESSOAS_FIELDS = Literal['id', 'idade', 'nome', 'sexo']

# Tipagem Genérica
GENERIC_BASE_MODEL = TypeVar('GENERIC_BASE_MODEL', bound=BaseModel)
