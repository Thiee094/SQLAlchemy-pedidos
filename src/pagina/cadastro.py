"""Solicitando ao usuário o pedido"""

while True:
    try:
        nome = input('Informe seu nome: ')
        if nome.isalpha():
            print(f'Olá {nome}')
            break
        else:
            print('Nome invalido, tente novamente por favor.')
    except ValueError:
        print('Não atende os requisitos, tente novamente por favor.')
        print('-------------------------------------------')
        
from datetime import datetime

while True:
    try:
        dt_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')
        data_nascimento = datetime.strptime(dt_nascimento, '%d%m%Y').date()
        data_atual = datetime.now().date()

        idade = data_atual.year - data_nascimento.year
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1  # ainda não fez aniversário esse ano

        if idade >= 15 and idade <= 80:
            print(data_nascimento)
            print('Ano cadastrado com sucesso')
            break
        else:
            print('Ano inválido! Menor de 15 anos. Tente novamente.')

    except ValueError:
        print('Formato inválido! Use data de nascimento completo')

while True:
    try:
        endereco = input('Informe seu endereço: ').strip().title()
        print('Endereço cadastrado com sucesso')
        break
    except ValueError:
        print('Tente novamente.')
        
while True:
    try:
        telefone = input('Informe seu número de Contato: ')
        if telefone.isdigit() and len(telefone) == 11:
            print('Telefone cadastrado com sucesso.')
            break
        else:
            print('Telefone invalido tente novamente')
    except ValueError:
        print('Telefone incorreto, tente novamente.')