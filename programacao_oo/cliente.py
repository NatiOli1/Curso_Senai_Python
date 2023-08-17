class Cliente:
    def __init__(self, nome, cpf, rg, email, ativo):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False
