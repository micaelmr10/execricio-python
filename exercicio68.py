def jogo_da_velha():
    """
   
    Função para jogar o jogo da velha.
    """

    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]


    jogador_atual = ('X')
    
    while True:
        
        imprimir_tabuleiro(tabuleiro)

        
        linha, coluna = obter_jogada(jogador_atual)

        
        if tabuleiro[linha][coluna] != ' ':
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        
        tabuleiro[linha][coluna] = jogador_atual

        
        if verifica_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"O jogador {jogador_atual} venceu!")
            break

        
        if verifica_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def imprimir_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro do jogo da velha.
    """
    print("  0  1  2")
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(f" {tabuleiro[i][j]} ", end='')
        print()

def obter_jogada(jogador):
    """
    Pede ao jogador atual para inserir sua jogada.
    """
    while True:
        try:
            linha = int(input(f"Jogador {jogador}, digite a linha (0-2): "))
            coluna = int(input(f"Jogador {jogador}, digite a coluna (0-2): "))
            if 0 <= linha <= 2 and 0 <= coluna <= 2:
                return linha, coluna
            else:
                print("Entrada inválida. Digite números entre 0 e 2.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")

def verifica_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador atual venceu.
    """
    
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True

    
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] == jogador:
            return True

    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def verifica_empate(tabuleiro):
    """
    Verifica se o jogo empatou.
    """
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True


jogo_da_velha()