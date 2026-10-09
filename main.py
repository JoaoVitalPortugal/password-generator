import random

alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabeto_minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caracteres_especiais = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '\\']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def criar_senha(tamanho):
    if type(tamanho) is not int:
        return "Tamanho inválido. Digite um número inteiro."

    if tamanho < 6 or tamanho > 14:
        return "Tamanho inválido. A senha deve ter entre 6 e 14 caracteres."

    senha = ""
    grupos = [alfabeto_maiusculo, alfabeto_minusculo, caracteres_especiais, numeros]

    for _ in range(tamanho):
        grupo_escolhido = random.choice(grupos)
        senha += random.choice(grupo_escolhido)

    return senha