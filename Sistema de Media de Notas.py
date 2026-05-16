#Sistema de Media de Notas

#Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#Calculo da media
media = (nota1 + nota2 + nota3) / 3

#Saida de dados
print("A média das notas é: ", f"{media:.1f}")

#tomada de decisoes 
if media >= 7:
    print("Sua media foi: " + f"{media:.1f}" + " - Aprovado")
elif media >= 5:
    print("Sua media foi: " + f"{media:.1f}" + " - Recuperação")
else:
    print("Sua media foi: " + f"{media:.1f}" + " - Reprovado")

    #Sistema de Media de Notas e suas Caracteristicas:
    #1. Entrada de dados: O sistema solicita ao usuário que insira as notas.atraves do comando input() e as converte para o tipo float para permitir cálculos matemáticos.
    #2. Calculo da media: O sistema calcula a média das notas somando as três notas e dividindo o resultado por 3.
    #3. Saida de dados: O sistema exibe a média calculada para o usuário usando o comando print().
    #4. Tomada de decisões: O sistema utiliza estruturas condicionais (if, elif, else) para determinar