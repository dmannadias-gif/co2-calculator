import math
from co2calc.models import Deslocamento, MeioTransporte, ResultadoEmissao
from co2calc.errors import DistanciaInvalidaError, DiasInvalidosError

# Fatores de emissão (kg CO2/km). Ver docs/fatores-emissao.md para fontes.
FATORES_EMISSAO_KG_KM = {
    MeioTransporte.CARRO_GASOLINA: 0.175,
    MeioTransporte.MOTO: 0.052,
    MeioTransporte.ONIBUS: 0.038,
    MeioTransporte.METRO: 0.004,
    MeioTransporte.BICICLETA_CAMINHADA: 0.0,
}

ABSORCAO_ARVORE_KG_ANO = 8.16
SEMANAS_POR_ANO = 52


def validar_deslocamento(deslocamento: Deslocamento) -> None:
    if deslocamento.distancia_km <= 0:
        raise DistanciaInvalidaError(
            f"Distância deve ser maior que zero, recebido: {deslocamento.distancia_km}"
        )
    if not (1 <= deslocamento.dias_por_semana <= 7):
        raise DiasInvalidosError(
            f"Dias por semana deve estar entre 1 e 7, recebido: {deslocamento.dias_por_semana}"
        )


def calcular_emissao_diaria(deslocamento: Deslocamento) -> float:
    validar_deslocamento(deslocamento)
    fator = FATORES_EMISSAO_KG_KM[deslocamento.transporte]
    return round(deslocamento.distancia_km * fator, 3)


def calcular_emissao_anual(deslocamento: Deslocamento) -> float:
    emissao_diaria = calcular_emissao_diaria(deslocamento)
    dias_no_ano = deslocamento.dias_por_semana * SEMANAS_POR_ANO
    return round(emissao_diaria * dias_no_ano, 2)


def converter_em_arvores(emissao_anual_kg: float) -> int:
    return math.ceil(emissao_anual_kg / ABSORCAO_ARVORE_KG_ANO)


def gerar_resultado(deslocamento: Deslocamento) -> ResultadoEmissao:
    emissao_diaria = calcular_emissao_diaria(deslocamento)
    emissao_anual = calcular_emissao_anual(deslocamento)
    arvores = converter_em_arvores(emissao_anual)
    return ResultadoEmissao(
        emissao_diaria_kg=emissao_diaria,
        emissao_anual_kg=emissao_anual,
        arvores_equivalentes=arvores,
    )
