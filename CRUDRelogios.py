print ("---------- RELOJOARIA MUITO MASSA ----------")

relogios = []
menu = -1

while menu != 0:
        menu = int(input("[ 1 ] Criar Relógio\n[ 2 ] Ler Relógios\n[ 3 ] Atualizar Relógio\n[ 4 ] Remover Relógio\n[ 0 ] Sair\n\nDigite: "))
        
        # Inputs
        if menu == 0:
            input("Programa encerrado. Aperte [ Enter ] para encerrar.")

        if menu == 1:
            tipoRelogio = int(input("Selecione o tipo de relógio:\n[ 1 ] Analógico\n[ 2 ] Digital\n[ 0 ] Sair\n\nDigite: "))
            
            if tipoRelogio == 1:
                tipoDeRelogio = "Analógico"
            elif tipoRelogio == 2:
                tipoDeRelogio = "Digital"
            else:
                print("---- Relógio Cancelado. ----\n")
                continue


            marcaRelogio = int(input("Selecione a marca de relógio:\n[ 1 ] Rolex\n[ 2 ] Cartier\n[ 3 ] Omega\n[ 4 ] Breitling\n[ 0 ] Sair\n\nDigite: "))
            if marcaRelogio == 1:
                marcaDeRelogio = "Rolex"
            elif marcaRelogio == 2:
                marcaDeRelogio = "Cartier"
            elif marcaRelogio == 3:
                marcaDeRelogio = "Omega"
            elif marcaRelogio == 4:
                marcaDeRelogio = "Breitling"
            else:
                print("---- Relógio Cancelado. ----\n")
                continue

            nomeRelogio = input("\nDê um nome ao seu relógio: ")
            print("---- Relógio feito com êxito. ----\n")
            relogio = [nomeRelogio, marcaDeRelogio, tipoDeRelogio]
            relogios.append(relogio)

        if menu == 2:
            print("\n==== RELÓGIOS CRIADOS ====")
            for relogio in relogios:
                print("----------")
                print(f"Nome: {relogio[0]}")
                print(f"Marca: {relogio[1]}")
                print(f"Tipo: {relogio[2]}")
                print("----------\n")

        if menu == 3:
            print(" \n===== Qual Relógio você quer editar? =====\n")
            for i in range(len(relogios)):
                print("----------")
                print(f" ({i})")
                print(f"Nome: {relogios[i][0]}")
                print(f"Marca: {relogios[i][1]}")
                print(f"Tipo: {relogios[i][2]}")
                print("----------\n")

            relogioEditar = int(input("\nDigite: "))
            
            
            print("\n==== O que você quer alterar? ====")
            alterar = int(input("\n[ 1 ] Nome\n[ 2 ] Marca\n[ 3 ] Tipo\n\nDigite: "))

            if alterar == 1:
                novoNome = input("Digite um novo nome: ")
                relogios[relogioEditar][0] = novoNome

            elif alterar == 2:
                novaMarca = int(input("Selecione a marca de relógio:\n[ 1 ] Rolex\n[ 2 ] Cartier\n[ 3 ] Omega\n[ 4 ] Breitling\n[ 0 ] Sair\n\nDigite: "))
                if novaMarca == 1:
                    relogios[relogioEditar][1] = "Rolex"
                elif novaMarca == 2:
                    relogios[relogioEditar][1] = "Cartier"
                elif novaMarca == 3:
                    relogios[relogioEditar][1] = "Omega"
                elif novaMarca == 4:
                    relogios[relogioEditar][1] = "Breitling"
                elif novaMarca == 0:
                    print("Alteração cancelada.")
                    continue
                else:
                    print("Resposta inválida.")
                    continue
                print("\n---- Alteração concluída com êxito. ----\n")

            elif alterar == 3:
                novoTipo = int(input("Selecione o tipo de relógio:\n[ 1 ] Analógico\n[ 2 ] Digital\n[ 0 ] Sair\n\nDigite: "))
                if novoTipo == 1:
                    relogios[relogioEditar][2] = "Analógico"
                elif novoTipo == 2:
                    relogios[relogioEditar][2] = "Digital"
                elif novoTipo == 0:
                    print("Alteração cancelada.")
                    continue
                else:
                    print("Resposta invália")
                    continue

        if menu == 4:
            print(f" \n==== QUAL RELÓGIO GOSTARIA DE REMOVER? ====\n")
            for i in range(len(relogios)):
                print("----------")
                print(f" ({i})")
                print(f"Nome: {relogios[i][0]}")
                print(f"Marca: {relogios[i][1]}")
                print(f"Tipo: {relogios[i][2]}")
                print("----------")

            removerRelogio = int(input("\nDigite [-1 para cancelar]: "))
            if removerRelogio < 0:
                print("\n==== REMOÇÃO CANCELADA ====\n")
            else:
                relogios.pop(removerRelogio)
                print ("\n ---- Remoção feita com êxito ----\n")
