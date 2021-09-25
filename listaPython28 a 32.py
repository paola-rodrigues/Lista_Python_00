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
valores = (input ("Digite os três valores seperando com espaço:  ")).split()
a, b, c = float(valores[0]), float(valores[1]), float(valores[2])
soma =  float('%.2f' %((a + b + c)**2))
print("O quadrados dos três valores é {}".format(soma))
print(type(soma))

'''
29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
'''
print("Questão 29")

notas = input ("Digite quatro valores de nota seperando com espaço:  ").split()
notas_int = [float(p) for p in notas]
soma = (float(notas[0]) + float(notas[1]) + float(notas[2]) + float(notas[3]))/4
print("A média da nota é {}".format(soma))
print(type(soma))  

'''
30.Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente 
em dólares. 
'''
print("Questão 30")
      
valor_real = float(input(" Digite o valor em real R$: "))
valor_dolar = float(input(" Digite a cotação em dólar US: "))
total_dolar = float('%.2f' %(valor_real/ valor_dolar))       
print("O valor em dólar é {}".format(total_dolar))      
print(type(total_dolar))    

'''
31.Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
'''

'''
32.Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de 
seu dobro
'''

'''
33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua area.
'''
