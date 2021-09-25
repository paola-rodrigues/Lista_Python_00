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

'''
28.. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos ˆ
tres valores lidos.
'''
print("Questão 28")
valores = input ("Digite os três valores:  ").split()
a, b, c = int(valores[0]), int(valores[1]), int(valores[2])
soma =  (a + b + c)**2
print("O quadrados dos três valores é {}".format(soma))
print(type(soma))
