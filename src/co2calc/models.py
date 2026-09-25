from dataclasses import dataclass
from enum import Enum


class MeioTransporte(Enum):
    CARRO_GASOLINA = "carro_gasolina"
    MOTO = "moto"
    ONIBUS = "onibus"
    METRO = "metro"
    BICICLETA_CAMINHADA = "bicicleta_caminhada"


@dataclass(frozen=True)
class Deslocamento:
    distancia_km: float
    transporte: MeioTransporte
    dias_por_semana: int


@dataclass(frozen=True)
class ResultadoEmissao:
    emissao_diaria_kg: float
    emissao_anual_kg: float
    arvores_equivalentes: int
