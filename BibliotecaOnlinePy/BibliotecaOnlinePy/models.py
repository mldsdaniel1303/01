from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from typing import Any

class IEmprestavel(ABC):
    @abstractmethod
    def calcular_taxa_emprestimo(self) -> float:
        ...

@dataclass
class Publicacao(IEmprestavel):
    id: int = 0
    titulo: str = ""
    autor: str = ""
    ano: int = 0

    @property
    def tipo(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def calcular_taxa_emprestimo(self) -> float:
        raise NotImplementedError
    

@dataclass
class Livro(Publicacao):
    paginas: int = 0
    genero: str = ""

    def calcular_taxa_emprestimo(self) -> float:
        # taxa base 2.50 + 0.01 por página
        return 2.50 + (0.01 * self.paginas)

@dataclass
class Revista(Publicacao):
    edicao: int = 0
    mes: str = ""

    def calcular_taxa_emprestimo(self) -> float:
        return 1.50

@dataclass
class Jornal(Publicacao):
    data_publicacao: date = field(default_factory=date.today)
    caderno: str = ""

    def calcular_taxa_emprestimo(self) -> float:
        return 1.00
