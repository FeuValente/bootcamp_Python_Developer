def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 2020, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# O caractere "/" indica que os parâmetros à esquerda devem ser passados como argumentos posicionais
# O caractere "*" indica que os parâmetros à direita devem ser passados como argumentos nomeados

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=2020, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")