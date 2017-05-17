#MATHEUS CALABRESE
#EXERCÍCIO 7

respostas =  ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A'] #Lista com as respostas do teste


#Declaração das variaveis
maiorAcerto = 0
menorAcerto = 10
totalAlunos = 0
media = 0

while True:
    cont = 0
    acertos = 0
    erros = 0
    for resposta in respostas: #For loop que vai verificar se a resposta digitada é igual ao item correto da questão
        item = input('Digite a resposta da questão %d: '%(cont + 1)).lower()

        if resposta == item:
            acertos += 1

        else:
            erros += 1

        cont += 1

    totalAlunos += 1 #Incremento de aluno
    media += acertos #Acumuda o número de acertos em média

    if acertos > maiorAcerto: #Teste para saber se o aluno obteve a maior quantidade de acertos
        maiorAcerto = acertos

    if erros < menorAcerto: #Teste para saber se o aluno obteve a menor quantidade acertos
        menorAcerto = erros


#Verifica se mais um aluno deseja checar suas respostas.
    continuar = input('Deseja continuar a usar o programa? Digite S(sim) ou N(não)\n').lower()

    if continuar == 's':
        continue

    elif continuar == 'n':
        break

media = media / totalAlunos #Calcula a média dividindo o total dos acertos pelo número de alunos

print('%d alunos usaram o sistema'%totalAlunos)
print('A maior quantidade de acertos: %d'%maiorAcerto)
print('A menor quantidade de acertos: %d'%menorAcerto)
print('A média da turma foi: %.2f'%media)
