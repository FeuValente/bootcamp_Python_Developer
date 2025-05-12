def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserdido com sucesso! {marca} {modelo} {ano} {placa}")


salvar_carro("Fusca", "Fusca", 1980, "ABC-1234")
salvar_carro(marca="Fusca", modelo="Fusca", ano=1980, placa="ABC-1234")
salvar_carro(**{"marca": "Fusca", "modelo": "Fusca", "ano": 1980, "placa": "ABC-1234"})