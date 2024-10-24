# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.


def conta_a_na_string(s):
    contagem = s.lower().count('a')
    return contagem

string = input("Informe uma string: ")

contagem = conta_a_na_string(string)
if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")