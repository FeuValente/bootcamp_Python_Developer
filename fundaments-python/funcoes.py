def exibir_mensagem():
    print("Ola mundo")

def exibir_mensagem_2(nome):
    print(f"Sea bem vindo {nome}!")
          
        
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Alfeu")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
