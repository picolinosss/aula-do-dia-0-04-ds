import random

cores = ["vermelho", "azul", "verde", "amarelo"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# define a carta que começa na mesa
cor_mesa = random.choice(cores)
num_mesa = random.choice(numeros)

while True:
    print(f"\n--- MESA: {num_mesa} {cor_mesa} ---")
    
    # sorteia carta para o jogador
    cor_jogador =  random.choice(cores)
    num_jogador = random.choice(numeros)
    print(f"sua carta: {num_jogador} {cor_jogador}")
    
    # verifica se pode jogar
    if cor_jogador == cor_mesa or num_jogador == num_mesa:
        print("Boa! você jogou e ela virou a nova carta da mesa")
        cor_mesa= cor_jogador # a carta do jogador vira a nova da mesa
        num_mesa = num_jogador
    else:
        print("Não serve! Tentando novamente...")
        
    # Pergunta se quer continuar
    continuar = input("Pressione enter para a proxima rodada ou 'sair' para parar")
    if continuar.lower() == "sair":
        break