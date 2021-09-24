'''
11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
quilometros por hora). A fórmula de conversão é: ´ K = M ∗ 3.6, sendo K a velocidade
em km/h e M em m/s.
'''
print("Questão 11")

print("****************************************************")
print('******Conversor de velocidade m/s para km/h ********')
print("****************************************************")


m = float(input(" Digite a velocidade em m/s: "))
k = float('%.2f' %(m * 3.6))
print("A velocidade é {} km/h".format(k))
print(type(k))


'''
12. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de 
conversão é:  K = 1, 61 ∗ M, sendo K a distancia em quilômetros e  M em milhas.
'''
print("Questão 12")


print("****************************************************")
print('******Conversor de milhas para quilômetros**********')
print("****************************************************")


m = float(input(" Digite a distância em milhas: "))
k = float('%.2f' %(1.61 * m))
print("A vdistância é {} quilômetros".format(k))
print(type(k))


'''
13. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de 
conversão é: M =K/1,61 , sendo K a distância em quilômetros e M em milhas.
'''
print("Questão 13")


print("****************************************************")
print('******Conversor de quilômetros para milhas *********')
print("****************************************************")


k = float(input(" Digite a distância em quilômetros: "))
m = float('%.2f' %(k /1.61))
print("A distância é {} milhas".format(m))
print(type(m))


'''
14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é:  R = G ∗ π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.
'''
print("Questão 14")

print("****************************************************")
print('********Conversor de graus para radianos************')
print("****************************************************")


g = float(input(" Digite um ângulo em graus: "))
x = 3.14
r = float('%.2f' %(g * (x/180)))
print("A ângulo em radianos é {}".format(r))
print(type(r))


'''
15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R ∗ 180/π, sendo G o ângulo em graus e R em radianos e π = 3.14.
'''
print("Questão 15")
print("****************************************************")
print('********Conversor de radianos para graus************')
print("****************************************************")


r = float(input(" Digite um ângulo em radianos: "))
x = 3.14
g = float('%.2f' %(r * (180/x)))
print("A ângulo em graus é {}".format(g))
print(type(g))



'''
16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é:´ C = P ∗ 2, 54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
'''
print("Questão 16")
print("****************************************************")
print('******Conversor de polegadas para centímetros*******')
print("****************************************************")


p = float(input(" Digite um valor em polegadas: "))
c = float('%.2f' %(p * 2.54))
print("O valor do comprimento em centímetros é {}".format(c))
print(type(c))



