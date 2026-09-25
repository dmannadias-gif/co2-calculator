class EntradaInvalidaError(Exception):
    """Levantada quando um dado de entrada do usuário é inválido."""

    pass


class DistanciaInvalidaError(EntradaInvalidaError):
    """Distância deve ser um número maior que zero."""

    pass


class DiasInvalidosError(EntradaInvalidaError):
    """Dias por semana deve estar entre 1 e 7."""

    pass


class TransporteInvalidoError(EntradaInvalidaError):
    """Meio de transporte não reconhecido."""

    pass
