# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input("escolha um numero para a tabuada "))

for i in range(1, 11):
    print(num * i)