import random



def jogador():
    try:
        
        player = input("""
        escolha 
        [P] PARA PEDRA
        [PP] PARA PAPEL
        [T] PARA TESOURA:
        """).upper()

        if player not in {"P", "PP", "T"}:
            raise ValueError("Opção inválida. Digite apenas P, PP ou T.")
        
        comp = random.choice(['p','pp','t']).upper()
        print(f'voce escolheu {player}, computador escolheu {comp}')
        if player in {"P", 'PP', 'T'} and comp == player:
            print('empate')
        elif player == "P" and comp == "T":
            print("você ganhou")
        elif player =="T" and comp == "PP":
            print("você ganhou")
        elif player == "PP" and comp == "p":
            print("você ganhou")

        elif player == "T" and comp == "P":
            print("você perdeu")
        elif player =="PP" and comp == "T":
            print("você perdeu")
        elif player == "P" and comp == "PP":
            print("você perdeu")
    except ValueError as e:
        print(f"Erro: {e}")
        jogador()

print(jogador())