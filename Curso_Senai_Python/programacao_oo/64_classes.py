
from cliente import Cliente
from conta import Conta

cliente01 = Cliente("Alfredo", 123121, 1212,
             "alfredo@gmail.com", True)
cliente02 = Cliente("Adam", 317881, 8765,
             "AdamEscroto@gmail.com", True)
cliente03 = Cliente("Albert Einstein", 128492, 4920,
             "Eusoufoda@gmail.com", True)

saldo1 = 5000
saldo2 = 1500
saldo3 = 3000

Conta01 = Conta("Conta Poupança", "Esta é a conta corrente do Sr. Alfredo", cliente01, saldo=saldo1)
Conta02 = Conta("Conta Poupança", "Esta é a conta corrente do Sr. Adam", cliente01, saldo=saldo2)
Conta03 = Conta("Conta Poupança", "Esta é a conta corrente do Sr. Einstein", cliente01, saldo=saldo3)

Conta01.depositar(3000)
Valor1 = saldo1 + 3000
Conta01.sacar(50)
Conta01.get_extrato()
print(f"O saldo da conta do Sr {cliente01.nome} "
      f"é {Conta01.get_saldo()} ")


Conta02.depositar(20)
Valor2 = saldo2 + 20
Conta02.sacar(900)
Conta02.get_extrato()
print(f"O saldo da conta do Sr {cliente02.nome} "
      f"é {Conta02.get_saldo()}")

Conta03.depositar(100)
Valor3 = saldo3 + 100
Conta03.sacar(5000)
Conta03.get_extrato()
print(f"O saldo da conta do Sr {cliente03.nome} "
      f"é {Conta03.get_saldo()}")




