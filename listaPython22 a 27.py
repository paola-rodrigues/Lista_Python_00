
'''
22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula ´
de conversão é: M = 0, 91 ∗ J, sendo J o comprimento em jardas e M o comprimento
em metros.
'''
print("Questão 22")
print("****************************************************")
print('**********Conversor de jardas para metros***********')
print("****************************************************")

j = float(input(" Digite o valor do comprimento em jardas: "))
m = float('%.2f' %(0.91 *j))
print("O valor do comprimento em metros é {}".format(m))
print(type(m))



'''
23. Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula ´
de conversão é: ´ J = M/0,91 , sendo J o comprimento em jardas e M o comprimento em
metros.
'''
print("Questão 23")
print("****************************************************")
print('**********Conversor de metros para jardas***********')
print("****************************************************")

m = float(input(" Digite o valor do comprimento em metros: "))
j = float('%.2f' %(m /0.91))
print("O valor do comprimento em jardas é {}".format(j))
print(type(j))

'''
24. Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres. A
fórmula de conversão˜ é:  A = M ∗ 0, 000247, sendo M a área em metros quadrados  A
a área em acres.
'''
print("Questão 24")
print("****************************************************")
print('**********Conversor de m² para acres****************')
print("****************************************************")

m = float(input(" Digite o valor da área em m²: "))
a = float('%.2f' %(m * 0.000247))
print("O valor da área em acres é {}".format(a))
print(type(a))

'''
25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m2
. A fórmula de conversão˜ é: M = A ∗ 4048, 58, sendo M a área em metros quadrados e A a
área em acres.
'''
print("Questão 25")
print("****************************************************")
print('**********Conversor de acres para m²****************')
print("****************************************************")

a = float(input(" Digite o valor da área em acres: "))
m = float('%.2f' %(a * 4048.58))
print("O valor da área em metros quadrados é {}".format(m))
print(type(m))

'''
26.Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares.
A fórmula de conversão˜ é: H = M ∗ 0, 0001, sendo M a área em metros quadrados e H
a área em hectares.
'''

print("Questão 26")
print("****************************************************")
print('*********Conversor de m² para hectares**************')
print("****************************************************")

m = float(input(" Digite o valor da área em m²: "))
h = float('%.2f' %(m * 0.0001))
print("O valor da área em hectares é {}".format(h))
print(type(h))
'''
27.Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2.
A fórmula de conversão˜ é: M = H ∗ 10000, sendo M a área em metros quadrados e H
a área em hectares.
'''
print("Questão 27")
print("****************************************************")
print('*********Conversor de hectares para m²*************')
print("****************************************************")

h = float(input(" Digite o valor da área em hectares: "))
m = float('%.2f' %(h * 10000))
print("O valor da área em m² é {}".format(m))
print(type(m))


