import random 

armas = ["espada", "escudo", "arco"]
arm_jog = input("Qual arma você escolhe? (arco, espada ou escudo)")
jog_comp = random.choice(armas)

while True:
    
    if arm_jog == jog_comp:
        print(f"seu adversario tambem escolheu {jog_comp} (enter para jogar novamente)")
        
    elif(arm_jog == "arco" and jog_comp == "espada") or \
        (arm_jog =="espada" and jog_comp = "escudo") or \
        (arm_jog == "escudo" and jog_comp = "arco"):
        print(f"Você venceu! seu adversario jogou {jog_comp}, e você escolehu {arm_jog}")
    
    else:
        print (f"você perdeu, seu oponente tinha {jog_comp} e você {arm_jog}")
        
    continuar = input("Pressione enter para a proxima rodada ou 'sair' para parar")
    if continuar.lower() == "sair":
        break
        