
import acessoBd

#menu para usuário
menu = "---------------------------\n"
menu+="[1] para inserir uma cantora\n"
menu+="[2] para atualizar algum dado\n"
menu+="[3] para deletar uma cantora\n"
menu+="[4] para realizar uma busca\n"
menu+="[5] finalizar conexão com o BD\n"

#menu updates
up = "---------------------------\n"
up+="[1] para atualizar o nome\n"
up+="[2] para atualizar a quantidade de albuns\n"
up+="[3] para atualizar a média arrecadada por música\n"
up+="[4] para atualizar a data do próximo lançamento\n"
up+="[5] para voltar\n"
up+= "---------------------------\n"

#menu busca
menuBusca="---------------------------\n"
menuBusca +="[1] para buscar uma cantora\n"
menuBusca +="[2] para buscar todas as cantoras (ordem alfabética)\n"
menuBusca += "[3] para voltar\n"
menuBusca+="---------------------------\n"

while True:

    print(menu)
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        nome = str(input("Digite o nome da cantora: "))
        quantidadeAlbuns = int(input("Digite a quantidade de albuns: "))
        media_por_musica = float(input("Digite a média recebida por música: "))
        dataProx_lancamento = str(input("Digite a data do próximo lançamento: "))
        acessoBd.insert(nome, quantidadeAlbuns, media_por_musica, dataProx_lancamento)
    if opcao == 2:
        print(up)
        opcaoUp = int(input("Digite sua opção: "))
        while True:
            if opcaoUp == 1: 
                codigo = int(input("Digite o código da cantora que deseja atualizar o nome: "))
                novoNome = str(input("Digite o novo nome: "))
                acessoBd.updateNome(codigo, novoNome)
                break
            elif opcaoUp == 2:
                codigo = int(input("Digite o código da cantora que deseja atualizar a quantidade de álbuns: "))
                novaQuant=int(input("Digite a nova quantidade de álbuns: "))
                acessoBd.updateAlbuns(codigo, novaQuant)
                break
            elif opcaoUp == 3:
                codigo = int(input("Digite o código da cantora que deseja atualizar a média arrecadada por música: "))
                novaMedia = float(input("Digite a nova média: "))
                acessoBd.updateMedia(codigo, novaMedia)
                break
            elif opcaoUp == 4:
                codigo = int(input("Digite o código da cantora que deseja atualizar a data do próximo lançamento: "))
                novaData = str(input("Digite a nova data: "))
                acessoBd.updateData(codigo, novaData)
                break
            elif opcaoUp == 5:
                break
    if opcao == 3:
        acessoBd.selectGeral()
        codigo = int(input("Digite o código da cantora que deseja apagar: "))
        acessoBd.delete(codigo)
    if opcao == 4:
        while True:
            print(menuBusca)
            opcaoBusca = int(input("Digite sua opção: "))
            if opcaoBusca == 1:
                codigo = int(input("Digite o código da cantora que deseja buscar: "))
                acessoBd.selectUma(codigo)
            elif opcaoBusca == 2:
                acessoBd.selectGeral()
            elif opcaoBusca == 3: 
                break
    if opcao == 5:
        acessoBd.cursor.close()
        acessoBd.connection.close()
        print("Conexão ao PostgreSQL foi encerrada.")
        break
