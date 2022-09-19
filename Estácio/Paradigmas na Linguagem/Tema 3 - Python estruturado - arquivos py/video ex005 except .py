numerador = eval(input('entre com o numerador: '))
denominador = eval(input('entre com o denominador: '))

try:
    print(f'a divisão da fração é igual a{numerador/denominador}') # o que esta dentro do try pode gerar uma exceção
except ZeroDivisionError:
    print('digite outro denominador que não seja o "zero"') # pois se o denominador for zero da erro no programa e causa a exceção para se o divisor for "zero"
except:
    print('os parametros informados causam erro no sistema')