funcionarios = ["lagarto", "girafa", "peixe boi"]
horarios_pontos = ["--:--", "--:--", "--:--"]

print ("---- PRINT DE PONTO EMPRESA TRIKAS ----")
print ("nome:", funcionarios[0], "horario:", horarios_pontos[0])
print ("nome:", funcionarios[1], "horario:", horarios_pontos[1])
print ("nome:", funcionarios[2], "horario:", horarios_pontos[2])

print ("Registro de Entrada")
nome_busca = input("Digite o nome do funcionario: ")

posicao = funcionarios.index(nome_busca)

hora_atual = input("Digite o horario de entrada (ex: 08:00):")
horarios_pontos[posicao] = hora_atual

print ("Ponto Registrado com Sucesso!")
print ("Funcionario:", funcionarios[posicao])
print ("Horário de Entrada:", horarios_pontos[posicao])

print ("status Geral")
print(funcionarios[0], ":", horarios_pontos[0])
print(funcionarios[1], ":", horarios_pontos[1])
print(funcionarios[2], ":", horarios_pontos[2])