import random

#Gerando senhas aleatórias de 16 caracteres com as melhores praticas

minusculas = "abcdefghijklmnopqrstuvxywz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
numeros = "0123456789"
simbolos = "!@#$%ˆ&()*\[]{}+/?<>-" 

caracteres = minusculas + maiusculas + numeros + simbolos
tamanho = 16

senha = "".join(random.sample(caracteres,tamanho))
print("Senha gerada:" + senha)