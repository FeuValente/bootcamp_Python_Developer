def somar(a, b):
    return a + b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")

exibir_resultado(10, 5, somar)
# A função `exibir_resultado` recebe dois números e uma função como parâmetros.
# Ela chama a função passada como argumento e exibe o resultado.
# Isso demonstra como funções podem ser passadas como argumentos para outras funções.
