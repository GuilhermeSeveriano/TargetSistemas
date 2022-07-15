# Primeiro iremos definir a quantidade de termos que irá ser mostrado na tela de acordo com a regra da sequencia fibonacci
num = int(input("Informe um número que definirá a quantidade de caracteres da sequencia fibonacci "))

#Após isso iremos definir os termos que sempre darão inicio na contagem para termos um padrão de soma
fib1 = 0 # primeiro termo fibonacci
fib2 = 1 # segundo termo fibonacci 0 -> 1
print(f"{fib1} - {fib2}", end="")

cont = 3 #contador que dará inicio aos novos termos

#Definido os dois primeiros termos faremos uma condição que diz, enquanto o contador for menor ou igual a quantidade de termos informados pela váriavel num faça a soma da variavel anterior + atual
while cont <= num:
    fibatual = fib1 + fib2
    fib1 = fib2
    fib2 = fibatual
    cont = cont + 1
    print (" - {}".format(fibatual), end="")
print (" - Fim")