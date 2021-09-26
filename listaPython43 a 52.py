'''
42. Receba o salario-base de um funcionário. Calcule e imprima o salário a receber, sabendo- ´
se que esse funcionario tem uma gratificação de 5% sobre o salário-base. Além disso, ´
ele paga 7% de imposto sobre o salario-base.
'''
print("Questão 42")
salario_base = float(input("Digite o valor do salario-base: "))
salario_receber = (salario_base * 1.05) - (salario_base * 0.07)                    
print(" O salário a receber é R$ {}".format(salario_receber))
