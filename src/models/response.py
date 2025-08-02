from pydantic import BaseModel
from typing import Literal, Optional

class Pessoas(BaseModel):
    '''
    Resposta da API no coleção de Pessoas

    - idade: **int**
    - nome: **str**
    - sexo: **Literal["M", "F"]**
    '''

    id: Optional[str] = None
    idade: int
    nome: str
    sexo: Literal['M', 'F']
