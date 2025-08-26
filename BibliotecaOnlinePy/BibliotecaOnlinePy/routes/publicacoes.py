from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field
from models import Publicacao, Livro, Revista, Jornal
from services.publicacao_service import PublicacaoService

router = APIRouter()

# DTOs using pydantic
class PublicacaoCreateDto(BaseModel):
    tipo: str = Field(..., example="Livro")
    titulo: str
    autor: str
    ano: int
    paginas: Optional[int] = None
    genero: Optional[str] = None
    edicao: Optional[int] = None
    mes: Optional[str] = None
    data_publicacao: Optional[str] = None
    caderno: Optional[str] = None

class PublicacaoReadDto(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    tipo: str
    taxa_emprestimo: float
    dados_especificos: Optional[dict] = None

# Singleton service instance (simple approach)
_service = PublicacaoService()

def to_read_dto(p: Publicacao) -> PublicacaoReadDto:
    dados = None
    if isinstance(p, Livro):
        dados = {"paginas": p.paginas, "genero": p.genero}
    elif isinstance(p, Revista):
        dados = {"edicao": p.edicao, "mes": p.mes}
    elif isinstance(p, Jornal):
        dados = {"data_publicacao": str(p.data_publicacao), "caderno": p.caderno}
    return PublicacaoReadDto(id=p.id, titulo=p.titulo, autor=p.autor, ano=p.ano, tipo=p.tipo, taxa_emprestimo=p.calcular_taxa_emprestimo(), dados_especificos=dados)

@router.get("/", response_model=List[PublicacaoReadDto])
def get_all(tipo: Optional[str] = None):
    items = _service.get_all() if not tipo else _service.get_by_tipo(tipo)
    return [to_read_dto(p) for p in items]

@router.get("/{id}", response_model=PublicacaoReadDto)
def get_by_id(id: int):
    p = _service.get_by_id(id)
    if not p:
        raise HTTPException(status_code=404, detail="Publicação não encontrada")
    return to_read_dto(p)

@router.post("/", response_model=PublicacaoReadDto, status_code=201)
def create(dto: PublicacaoCreateDto):
    tipo = dto.tipo.strip().lower()
    if tipo == "livro":
        p = Livro(titulo=dto.titulo, autor=dto.autor, ano=dto.ano, paginas=dto.paginas or 0, genero=dto.genero or "")
    elif tipo == "revista":
        p = Revista(titulo=dto.titulo, autor=dto.autor, ano=dto.ano, edicao=dto.edicao or 0, mes=dto.mes or "")
    elif tipo == "jornal":
        data = None
        if dto.data_publicacao:
            data = dto.data_publicacao
        p = Jornal(titulo=dto.titulo, autor=dto.autor, ano=dto.ano, caderno=dto.caderno or "")
        if data:
            from datetime import date
            try:
                p.data_publicacao = date.fromisoformat(data)
            except Exception:
                pass
    else:
        raise HTTPException(status_code=400, detail="Tipo inválido. Use: Livro, Revista ou Jornal.")
    created = _service.add(p)
    return to_read_dto(created)

@router.put("/{id}", status_code=204)
def update(id: int, dto: PublicacaoCreateDto):
    tipo = dto.tipo.strip().lower()
    if tipo == "livro":
        p = Livro(titulo=dto.titulo, autor=dto.autor, ano=dto.ano, paginas=dto.paginas or 0, genero=dto.genero or "")
    elif tipo == "revista":
        p = Revista(titulo=dto.titulo, autor=dto.autor, ano=dto.ano, edicao=dto.edicao or 0, mes=dto.mes or "")
    elif tipo == "jornal":
        p = Jornal(titulo=dto.titulo, autor=dto.autor, ano=dto.ano, caderno=dto.caderno or "")
        if dto.data_publicacao:
            from datetime import date
            try:
                p.data_publicacao = date.fromisoformat(dto.data_publicacao)
            except Exception:
                pass
    else:
        raise HTTPException(status_code=400, detail="Tipo inválido. Use: Livro, Revista ou Jornal.")
    ok = _service.update(id, p)
    if not ok:
        raise HTTPException(status_code=404, detail="Publicação não encontrada")
    return None

@router.delete("/{id}", status_code=204)
def delete(id: int):
    ok = _service.delete(id)
    if not ok:
        raise HTTPException(status_code=404, detail="Publicação não encontrada")
    return None
