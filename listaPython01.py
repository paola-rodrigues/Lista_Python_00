'''
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversão e: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
'''
print("Questão 7")
print("****************************************************")
print('Conversor de temperatura de Fahrenheit para Celsius!')
print("****************************************************")


f = float(input(" Digite a temperatura em graus Fahrenheit: "))
e = float(('%.2f' %(5.0 *((f - 32.0)/9.0))))
print("A temperatura em Celsius é {}Cº".format(e))
print(type(e))

"""
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
formula de conversão e: C = K − 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin
"""

print("Questão 8")
print("****************************************************")
print('**Conversor de temperatura de Kelvin para Celsius!**')
print("****************************************************")


k = float(input(" Digite a temperatura em graus Kelvin: "))
c = float(('%.2f' %(k - 273.15)))
print("A temperatura em Celsius é {}Cº".format(c))
print(type(c))

"""
9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
formula de conversão e: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.

"""

print("Questão 9")
print("****************************************************")
print('**Conversor de temperatura de Celsius para Kelvin!**')
print("****************************************************")


c = float(input(" Digite a temperatura em graus Celsius: "))
k = float(('%.2f' %(c + 273.15)))
print("A temperatura em Kelvin é {}".format(k))
print(type(k))

"""
10. Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s ˆ
(metros por segundo). A formula de conversão e:  M = K/3.6, sendo K a velocidade em
km/h e M em m/s
"""


print("Questão 10")
print("****************************************************")
print('******Conversor de velocidade km/h para m/s ********')
print("****************************************************")


k = float(input(" Digite a velocidade em km/h: "))
m = float(('%.2f' %(k/3.6)))
print("A velocidade é {} m/s".format(m))
print(type(m))

