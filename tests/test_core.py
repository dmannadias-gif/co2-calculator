import pytest
from co2calc.models import Deslocamento, MeioTransporte
from co2calc.core import (
    calcular_emissao_diaria,
    calcular_emissao_anual,
    converter_em_arvores,
    gerar_resultado,
)
from co2calc.errors import DistanciaInvalidaError, DiasInvalidosError


def test_emissao_diaria_carro_gasolina():
    d = Deslocamento(
        distancia_km=20, transporte=MeioTransporte.CARRO_GASOLINA, dias_por_semana=5
    )
    assert calcular_emissao_diaria(d) == 3.5


def test_emissao_anual_carro_gasolina():
    d = Deslocamento(
        distancia_km=20, transporte=MeioTransporte.CARRO_GASOLINA, dias_por_semana=5
    )
    assert calcular_emissao_anual(d) == 910.0


def test_bicicleta_nao_emite():
    d = Deslocamento(
        distancia_km=20,
        transporte=MeioTransporte.BICICLETA_CAMINHADA,
        dias_por_semana=5,
    )
    assert calcular_emissao_anual(d) == 0.0


def test_conversao_em_arvores_arredonda_para_cima():
    assert converter_em_arvores(910.0) == 112


def test_distancia_zero_levanta_erro():
    d = Deslocamento(
        distancia_km=0, transporte=MeioTransporte.CARRO_GASOLINA, dias_por_semana=5
    )
    with pytest.raises(DistanciaInvalidaError):
        calcular_emissao_diaria(d)


def test_distancia_negativa_levanta_erro():
    d = Deslocamento(
        distancia_km=-5, transporte=MeioTransporte.CARRO_GASOLINA, dias_por_semana=5
    )
    with pytest.raises(DistanciaInvalidaError):
        calcular_emissao_diaria(d)


def test_dias_fora_do_intervalo_levanta_erro():
    d = Deslocamento(
        distancia_km=20, transporte=MeioTransporte.CARRO_GASOLINA, dias_por_semana=8
    )
    with pytest.raises(DiasInvalidosError):
        calcular_emissao_diaria(d)


def test_gerar_resultado_completo():
    d = Deslocamento(
        distancia_km=20, transporte=MeioTransporte.CARRO_GASOLINA, dias_por_semana=5
    )
    resultado = gerar_resultado(d)
    assert resultado.emissao_diaria_kg == 3.5
    assert resultado.emissao_anual_kg == 910.0
    assert resultado.arvores_equivalentes == 112
