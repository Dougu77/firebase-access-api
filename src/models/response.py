import pydantic

class Pessoas(pydantic.BaseModel):
    '''
    Resposta da API no coleção de Pessoas

    - idade: **int**
    - nome: **str**
    - sexo: **str**
    '''

    idade: int
    nome: str
    sexo: str
