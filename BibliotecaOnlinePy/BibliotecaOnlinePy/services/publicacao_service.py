from typing import Dict, List, Optional
from models import Publicacao, Livro, Revista, Jornal
import threading
from datetime import date

class PublicacaoService:
    def __init__(self):
        self._itens: Dict[int, Publicacao] = {}
        self._next_id = 1
        self._lock = threading.Lock()
        # seed
        self.add(Livro(titulo="Padrões de Projeto", autor="GoF", ano=1994, paginas=395, genero="Engenharia de Software"))
        self.add(Revista(titulo="Ciência Hoje", autor="SBPC", ano=2023, edicao=412, mes="Junho"))
        self.add(Jornal(titulo="Gaceta Diário", autor="Redação", ano=date.today().year, data_publicacao=date.today(), caderno="Economia"))

    def get_all(self) -> List[Publicacao]:
        return list(self._itens.values())

    def get_by_id(self, id: int) -> Optional[Publicacao]:
        return self._itens.get(id)

    def add(self, item: Publicacao) -> Publicacao:
        with self._lock:
            item.id = self._next_id
            self._itens[self._next_id] = item
            self._next_id += 1
        return item

    def update(self, id: int, item: Publicacao) -> bool:
        with self._lock:
            if id not in self._itens:
                return False
            item.id = id
            self._itens[id] = item
            return True

    def delete(self, id: int) -> bool:
        with self._lock:
            return self._itens.pop(id, None) is not None

    def get_by_tipo(self, tipo: str) -> List[Publicacao]:
        return [p for p in self._itens.values() if p.tipo.lower() == tipo.lower()]
