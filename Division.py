import Multiplex


def subtraction(value1, value2):
    value2 = Multiplex.changeSign(value2)
    res = Multiplex.sumFunc(value1, value2)
    if len(res) != len(value2):
        return res[1:]
    return res


def comparison(value1, value2):
    isValue2Biggger = False
    for i in range(len(value1)):
        if value1[i] == '1' and value2[i] == '0':
            isValue2Biggger = False
            break
        elif value2[i] == '1' and value1[i] == '0':
            isValue2Biggger = True
            break
    return isValue2Biggger


def division(value1, value2):
    print("Value1 = ", value1)
    print("Value2 = ", value2)
    n = 32 - len(Multiplex.decimalToBinary(value2))
    value1 = Multiplex.base32(Multiplex.decimalToBinary(value1))
    value2 = Multiplex.decimalToBinary(value2) + ((32 - len(Multiplex.decimalToBinary(value2))) * '0')
    print("Value1 = ", value1)
    print("Value2 = ", value2, "     Перший знаковий біт дільника нормалізовуємо з першим бітом діленого")
    quotient = 32 * '0'
    for i in range(n + 1):
        print("\nІтерація:  ", i+1)
        if comparison(value1, value2):
            quotient = quotient[1:] + '0'
            value2 = '0' + value2[:-1]
            print("Value1     ", value1)
            print("Value2     ", value2, "   Робимо зсув діленого вліво")
            print("Quotient   ", quotient, '   Порівнюємо, дільник більше діленого, тому в результат записуємо 0 та зсуваємо результат вліво')

        elif not comparison(value1, value2):
            quotient = quotient[1:] + '1'
            value1 = subtraction(value1, value2)
            value2 = '0' + value2[:-1]
            print("Value1     ", value1)
            print("Value2     ", value2, "   Робимо зсув діленого вліво")
            print("Quotient   ", quotient, '   Порівнюємо, дільник менше діленого, тому в результат записуємо 1 та зсуваємо результат вліво')
    remainder = 32 * '0' + value1
    print("\nРезультат  ",quotient)
    print("Остача     ",remainder )



