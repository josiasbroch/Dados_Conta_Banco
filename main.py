'''
EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar_saldo
'''
from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Josias', '033984540-62', 24)

conta_do_josias = Conta(cliente1, 10.50, 1000)

print(conta_do_josias.cliente.nome, conta_do_josias.consulta_saldo())

conta_do_josias.depositar(1000.40)
print(conta_do_josias.consulta_saldo())

conta_do_josias.sacar(1400)
print(conta_do_josias.consulta_saldo())
