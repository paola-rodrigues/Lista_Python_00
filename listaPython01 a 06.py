print ("1º Faça um programa que leia um numero inteiro e o imprima.")

num = int(input(" Digite um número inteiro: "))
print(type(num))

print ("2º Faça um programa que leia um numero real e o imprima.")

num = float(input(" Digite um número real: "))
print(type(num))

print ("3º Peça ao usuario para digitar três valores inteiros e imprima a soma deles.")


num_1 = int(input(" Digite primeiro número inteiro: "))
num_2 = int(input(" Digite segundo número inteiro: "))
num_3 = int(input(" Digite terceiro número inteiro: "))
soma = num_1 + num_2 + num_3
print("Soma total {}".format(soma))


print ("4ºLeia um número real e imprima o resultado do quadrado desse número.")


num = float(input(" Digite um número real: "))
total = num**2
print("Resultado do quadrado desse número é {}".format(total))


print ("5º Leia um número real e imprima a quinta parte deste número.") 

x = 20/5
print(x)
print(type(x))

num = float(input(" Digite um número real: "))
total = num/5
print("A quinta parte desse número é {}".format(total))
print(type(total))

'''
6 Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversão e: F = C ∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
'''
print("****************************************************")
print('Conversor de temperatura de Celsius para Fahrenheit!')
print("****************************************************")


c = float(input(" Digite a temperatura em graus Celsius: "))
d = (c *((9.0/5.0) + 32.0))
e = ('%.1f' %(d))
print("A temperatura em Fahrenhit é {}F".format(e))



