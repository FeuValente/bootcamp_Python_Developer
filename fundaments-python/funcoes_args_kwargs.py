def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.tittle()}: {valor}" for chave, valor in kwargs.itens()])
    mensagem = f"{data_extenso}\n\n{texto}\n{meta_dados}"
    print(mensagem)

exibir_poema("22 de abril de 1999, ","Zen of Python", "Beatiful is better than ugly.", autor="Tim Peters", ano=1999)