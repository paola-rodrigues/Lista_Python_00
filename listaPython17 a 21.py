'''
17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: ´ P = C /2,54 , sendo C o comprimento em centímetros e P o
comprimento em polegadas.
'''
print("Questão 17")
print("****************************************************")
print('******Conversor de centímetros para polegadas*******')
print("****************************************************")


c = float(input(" Digite o valor do comprimento em centímetros: "))
p = float('%.2f' %(c/ 2.54))
print("O valor comprimento em polegadas é {}".format(p))
print(type(p))

'''
18. Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 ∗ M, sendo L o volume em litros e M o volume em metros cubicos.
'''
print("Questão 18")
print("****************************************************")
print('******Conversor de metros cúbicos para litros*******')
print("****************************************************")


m = float(input(" Digite o valor em metros cúbicos: "))
l = float('%.2f' %(1000 * m))
print("O valor do volume em litos é {}".format(l))
print(type(l))

'''
19. Leia um valor de volume em litros e apresente-o convertido em metros cubicos ´ m3.
A fórmula de convers ´ ao˜ e: ´ M = L/1000 , sendo L o volume em litros e M o volume em metros
cúbicos.
'''
print("Questão 19")
print("****************************************************")
print('******Conversor de litros para metros cúbicos*******')
print("****************************************************")


l = float(input(" Digite o valor do volume em litros: "))
m = float('%.2f' %(l /1000 ))
print("O valor do volume em metros cúbicos é {}".format(m))
print(type(m))

'''
20.Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula ´
de conversão é:´ L = K/0,45 , sendo K a massa em quilogramas e L a massa em libras.
'''
print("Questão 20")
print("****************************************************")
print('*******Conversor de quilogramas para libras*********')
print("****************************************************")


k = float(input(" Digite o valor da massa em quilogramas: "))
l = float('%.2f' %(k /0.45 ))
print("O valor da massa em libras é {}".format(l))
print(type(l))

'''
21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula ´
de conversão é: K = L ∗ 0, 45, sendo K a massa em quilogramas e L a massa em libras.
'''
print("Questão 21")
print("****************************************************")
print('********Conversor de libras para quilogramas********')
print("****************************************************")


l = float(input(" Digite o valor da massa em libras: "))
k = float('%.2f' %(l *0.45 ))
print("O valor da massa em quilogramas é {}".format(k))
print(type(k))
