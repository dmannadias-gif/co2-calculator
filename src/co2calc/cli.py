from co2calc.models import Deslocamento, MeioTransporte
from co2calc.core import gerar_resultado
from co2calc.errors import EntradaInvalidaError

MENU_TRANSPORTES = {
    "1": MeioTransporte.CARRO_GASOLINA,
    "2": MeioTransporte.MOTO,
    "3": MeioTransporte.ONIBUS,
    "4": MeioTransporte.METRO,
    "5": MeioTransporte.BICICLETA_CAMINHADA,
}


def ler_distancia() -> float:
    while True:
        try:
            return float(input("Distância diária (km): ").replace(",", "."))
        except ValueError:
            print("Erro: digite um número válido. Exemplo: 12.5")


def ler_transporte() -> MeioTransporte:
    print("\nMeio de transporte:")
    print(
        "1 - Carro a gasolina\n2 - Moto\n3 - Ônibus\n4 - Metrô\n5 - Bicicleta/Caminhada"
    )
    while True:
        opcao = input("Escolha (1-5): ").strip()
        if opcao in MENU_TRANSPORTES:
            return MENU_TRANSPORTES[opcao]
        print("Erro: opção inválida.")


def ler_dias() -> int:
    while True:
        try:
            dias = int(input("Dias por semana que faz esse trajeto (1-7): "))
            if 1 <= dias <= 7:
                return dias
            print("Erro: informe um valor entre 1 e 7.")
        except ValueError:
            print("Erro: digite um número inteiro.")


def exibir_resultado(resultado) -> None:
    print("\n--- Resultado ---")
    print(f"Emissão diária: {resultado.emissao_diaria_kg} kg de CO2")
    print(f"Emissão anual: {resultado.emissao_anual_kg} kg de CO2")
    print(
        f"Equivalente a {resultado.arvores_equivalentes} árvores para compensar por ano"
    )


def executar() -> None:
    print("=== Calculadora de Emissão de CO2 (ODS 13) ===\n")
    try:
        distancia = ler_distancia()
        transporte = ler_transporte()
        dias = ler_dias()
        deslocamento = Deslocamento(
            distancia_km=distancia, transporte=transporte, dias_por_semana=dias
        )
        resultado = gerar_resultado(deslocamento)
        exibir_resultado(resultado)
    except EntradaInvalidaError as e:
        print(f"\nErro nos dados informados: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")
