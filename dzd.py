def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2


n1 = int(input('digite seu primeiro numero: '))
n2 = int(input('digite seu segundo numero: '))
while True:
    ope = str(input('digite o operador: ')).strip()[0]
    if ope not in '+-*/':
        print('Operação invalida')
    else:
        break
print(f'o resultado de {n1} {ope} {n2} = {calculadora(n1, n2, ope)}')

