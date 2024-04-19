def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuario
    [q] Sair
    =>"""

    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato
                
def saque (*, saldo, valor, limite, numero_saques, LIMITE_SAQUES, extrato):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
             
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: R$ {valor:.2f}\n'
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, limite, numero_saques, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = int(input("Informe o CPF (somente números): "))
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Digite o seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criaod com sucesso!")
       
def filtrar_usuarios(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, criação de conta encerrada!")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência:{conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        
        '''
        print("=" * 100)
        print(linha)


LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:
    opcao = menu()
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
                
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        saldo, limite, numero_saques, extrato = saque(
            saldo= saldo,
            valor= valor,
            limite= limite,
            numero_saques= numero_saques,
            LIMITE_SAQUES= LIMITE_SAQUES,
            extrato= extrato            
        )       

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "nu":
        criar_usuario(usuarios)
    
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
            contas.append(conta)
            
    elif opcao == "lc":
        listar_contas(contas)
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



