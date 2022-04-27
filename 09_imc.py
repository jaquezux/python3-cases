peso = float(input("Indique o seu peso: "))
altura = float(input("Indique a sua altura (em metros): "))
imc = peso / (altura ** 2)

print("\n===========================")
print("O peso indicado foi: {}kg.".format(peso))
print("A altura indicada foi: {:.2f}m.".format(altura))
print("O IMC calculado foi: {:.2f}.".format(imc))
print("===========================\n")


if imc < 18.5:
    print("O seu imc é de {:.2f}, você está abaixo do peso.".format(imc))

elif imc >= 18.5 and imc <= 24.9:
    print("O seu IMC é de {:.2f} e você está dentro do peso ideal.".format(imc))

elif imc >= 25.0 and imc <= 29.9:
    print("O seu IMC é de {:.2f} e você está acima do peso.".format(imc))

else:
    print("O seu IMC é de {:.2f} e você está com obesidade.".format(imc))