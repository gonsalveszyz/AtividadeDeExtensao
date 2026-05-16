# Sistema de Média de Notas em Python

Este projeto é um sistema simples desenvolvido em **Python** com o objetivo de calcular a média de três notas informadas pelo usuário e, com base no resultado obtido, determinar a situação final do aluno.

O programa utiliza conceitos fundamentais da linguagem Python, como:

- Entrada de dados com `input()`;
- Conversão de tipos com `float()`;
- Operações matemáticas;
- Formatação de números decimais com f-string;
- Saída de dados com `print()`;
- Estruturas condicionais com `if`, `elif` e `else`.

---

## Objetivo do Projeto

O objetivo principal deste projeto é praticar a lógica de programação por meio de um sistema simples de cálculo de média escolar.

O programa solicita três notas ao usuário, calcula a média aritmética entre elas e classifica o aluno em uma das seguintes situações:

- **Aprovado**
- **Recuperação**
- **Reprovado**

Esse tipo de sistema é muito comum em exercícios introdutórios de programação, pois trabalha conceitos essenciais para o desenvolvimento de qualquer aplicação.

---

## Código do Projeto

```python
# Sistema de Media de Notas

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculo da media
media = (nota1 + nota2 + nota3) / 3

# Saida de dados
print("A média das notas é: ", f"{media:.1f}")

# Tomada de decisoes 
if media >= 7:
    print("Sua media foi: " + f"{media:.1f}" + " - Aprovado")
elif media >= 5:
    print("Sua media foi: " + f"{media:.1f}" + " - Recuperação")
else:
    print("Sua media foi: " + f"{media:.1f}" + " - Reprovado")
