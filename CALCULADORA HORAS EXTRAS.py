#Solicita que informe o salario do colaborador
salario = float(input('Informe o salario do colaborador: R$ '))

#Realiza o calculo de salario/hora
valor_hora = round(salario / 220, 2)
print('Salario hora: R$', valor_hora)

#Solicita que informe a quantidade de horas extras feitas no mes
he50 = float(input(
    'Informe a quantidade de horas extras 50% feitas no mes:', ))
he100 = float(
    input('Informe a quantidade de horas extras 100% feitas no mes:', ))
he120 = float(
    input('Informe a quantidade de horas extras 120% feitas no mes:', ))

extra50 = round((valor_hora * 0.5 + valor_hora) * he50, 2)
extra100 = round((valor_hora * 1.0 + valor_hora) * he100, 2)
extra120 = round((valor_hora * 1.2 + valor_hora) * he120, 2)

total_a_receber = (extra50 + extra100 + extra120)

print('O colaborador deve receber um total de: R$', total_a_receber)
