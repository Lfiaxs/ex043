peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura**2)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print ('Você está abaixo do peso normal.')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print ('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print ('Você está com obesidade mórbida.')
