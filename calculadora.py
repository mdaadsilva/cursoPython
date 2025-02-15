def validar_numero(mensagem):
    entrada = input(mensagem)
    while not entrada.isdigit():  # Verifica se a entrada é um número
        print("Entrada inválida. Por favor, digite um número válido.")
        entrada = input(mensagem)
    return int(entrada)

# Adição
num1 = validar_numero("Soma: Digite um valor: ")
num2 = validar_numero("Soma: Digite um valor: ")
soma = num1 + num2
print('A soma de', num1, '+', num2, 'é de:', soma)

# Subtração
num3 = validar_numero("Subtração: Digite um valor: ")
num4 = validar_numero("Subtração: Digite um valor: ")
subtracao = num3 - num4
print("A subtração de", num3, "-", num4, "é de:", subtracao)

# Multiplicação
num5 = validar_numero("Multiplicação: Digite um valor: ")
num6 = validar_numero("Multiplicação: Digite um valor: ")
multiplicacao = num5 * num6
print("A multiplicação de", num5, "*", num6, "é de:", multiplicacao)

# Divisão
num7 = validar_numero("Divisão: Digite um valor: ")
num8 = validar_numero("Divisão: Digite um valor: ")
if num8 == 0:
    print("Erro: Não é possível dividir por zero.")
else:
    divisao = num7 // num8
    print("A divisão de", num7, "//", num8, "é de:", divisao)