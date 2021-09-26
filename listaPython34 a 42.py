
'''
34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do cíırculo é π ∗ raio2, considere π = 3.141592.
'''
print("Questão 34")
raio = float(input(" Digite o valor do raio do circulo: "))
i = 3.141592
area_circulo =i * (raio**2)
print(" A área  do cículo é {}".format(area_circulo))  


'''
35. Sejam a e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação: ˜
hipotenusa =√a2 + b2. Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equaçãoo. Imprima o resultado dessa operação.
'''
print("Questão 35")
a = float(input(" Digite o valor cateto A: "))
b = float(input(" Digite o valor cateto B: "))

h = ((a**2) + (b**2))**0.5

print(" A hipotenusa do triangulo é {}".format(h))  


'''
36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = π ∗ raio2 ∗ altura,
onde π = 3.141592.
'''
print("Questão 36")
altura = float(input(" Digite o valor altura:  "))
raio = float(input(" Digite o valor raio:  "))
v = 3.141592 * (raio**2) * (altura)
print(" O volume do cilindro é {}".format(v))  

'''
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%
'''
print("Questão 37")
x = float(input("Digite o valor do produto: "))
d = x * 0.88          
print(" O valor do produto com desconto de 12% é {}".format(d))          


'''
38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que 
ele recebeu um aumento de 25%.
'''
print("Questão 38")
r = float(input("Digite o valor do salário: "))
e = float('%.2f' %(x * 1.10))

print(" O valor do novo salário com aumento é {}".format(e))          


'''
39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. ˆ
Sendo que da quantia total:
• O primeiro ganhador recebera 46%; ´
• O segundo recebera 32%; ´
• O terceiro recebera o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
'''
print("Questão 39")
x = 780000.00
primeiro =  x * 0.46
segundo = x * 0.32
terceiro = x * 0.22

print(" O valor do primeiro ganhador é R$ {}, do segundo ganhado é R$ {}, do terceiro ganhado é R$ {}".format(primeiro, segundo, terceiro)) 


'''
40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser 
paga, sabendo-se que são descontados 8% para imposto de renda.
'''
print("Questão 40")
enc = 30.00
d = int(input(" Digite o número de dias trabalhado: "))
y = (d * enc)*0.92
print(" A quantia líquida é R$ {}".format(y))

'''
41. Faça um programa que leia o valor da hora de trabalho (em reais) e numero de horas ´
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre ´
o valor calculado
'''
print("Questão 41")
valor_hora = float(input("Digite o valor da hora de trabalha R$  "))
numero_hora = float(input("Digite o número de horas trablhadas:  "))
pago_fun = (valor_hora * numero_hora)* 1.10
print(" O valor a ser pago ao funcionário é R$ {}".format(pago_fun))



'''
42. Receba o salario-base de um funcionário. Calcule e imprima o salário a receber, sabendo- ´
se que esse funcionario tem uma gratificação de 5% sobre o salário-base. Além disso, ´
ele paga 7% de imposto sobre o salario-base.
'''
print("Questão 42")
salario_base = float(input("Digite o valor do salario-base: "))
salario_receber = (salario_base * 1.05) - (salario_base * 0.07)                    
print(" O salário a receber é R$ {}".format(salario_receber))
        





