# Funções de conversão
def metros_para_quilometros(metros):
    return metros / 1000

def quilometros_para_metros(quilometros):
    return quilometros * 1000

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função principal para o menu
def menu():
    print("Bem-vindo ao Conversor de Unidades!")
    print("Escolha uma opção:")
    print("1. Conversão de Distâncias")
    print("2. Conversão de Temperaturas")
    print("3. Sair")

# Função para conversão de distâncias
def converter_distancias():
    print("Escolha uma conversão de distância:")
    print("1. Metros para Quilômetros")
    print("2. Quilômetros para Metros")
    escolha = input("Digite sua escolha (1 ou 2): ")

    if escolha == '1':
        metros = float(input("Digite o valor em metros: "))
        print(f"{metros} metros é igual a {metros_para_quilometros(metros)} quilômetros.")
    elif escolha == '2':
        quilometros = float(input("Digite o valor em quilômetros: "))
        print(f"{quilometros} quilômetros é igual a {quilometros_para_metros(quilometros)} metros.")
    else:
        print("Opção inválida!")

# Função para conversão de temperaturas
def converter_temperaturas():
    print("Escolha uma conversão de temperatura:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    escolha = input("Digite sua escolha (1 ou 2): ")

    if escolha == '1':
        celsius = float(input("Digite o valor em Celsius: "))
        print(f"{celsius} graus Celsius é igual a {celsius_para_fahrenheit(celsius)} graus Fahrenheit.")
    elif escolha == '2':
        fahrenheit = float(input("Digite o valor em Fahrenheit: "))
        print(f"{fahrenheit} graus Fahrenheit é igual a {fahrenheit_para_celsius(fahrenheit)} graus Celsius.")
    else:
        print("Opção inválida!")

# Função para iniciar o programa
def iniciar():
    while True:
        menu()
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == '1':
            converter_distancias()
        elif opcao == '2':
            converter_temperaturas()
        elif opcao == '3':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
iniciar()
