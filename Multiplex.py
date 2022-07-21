

def decimalToBinary(decimal_value):
    return bin(decimal_value).replace("0b", "")


def base32(value):
   return ((32 - len(str(value)))*'0') + str(value)


def base64(value):
   return ((64 - len(str(value)))*'0') + str(value)


def sumFunc(value1, value2, includeOne = False):
    mem, res = 0, ''
    base = len(value1)
    for i in range(1, base + 1):
        if (value1[base - i] == '0') and (value2[base - i] == '0') and (mem == 0):
            res = '0' + res
            mem = 0
        elif (value1[base - i] == '0') and (value2[base - i] == '0') and (mem == 1):
            res = '1' + res
            mem = 0
        elif (value1[base - i] == '0') and (value2[base - i] == '1') and (mem == 0):
            res = '1' + res
            mem = 0
        elif (value1[base - i] == '0') and (value2[base - i] == '1') and (mem == 1):
            res = '0' + res
            mem = 1
        elif (value1[base - i] == '1') and (value2[base - i] == '0') and (mem == 0):
            res = '1' + res
            mem = 0
        elif (value1[base - i] == '1') and (value2[base - i] == '0') and (mem == 1):
            res = '0' + res
            mem = 1
        elif (value1[base - i] == '1') and (value2[base - i] == '1') and (mem == 0):
            res = '0' + res
            mem = 1
        elif (value1[base - i] == '1') and (value2[base - i] == '1') and (mem == 1):
            res = '1' + res
            mem = 1
    if includeOne and mem == 1:
        res = '1' + res
    return res


def multiplexFunc(value1, value2):
    print("Value1 = ", value1)
    print("Value2 = ", value2)
    sign = [1, 1]
    if value1 < 0:
        sign[0] = 0
        value1 *= -1
    if value2 < 0:
        sign[1] = 0
        value2 *= -1
    value1 = base64(decimalToBinary(value1))
    value2 = base32(decimalToBinary(value2))
    res = 64 * '0'
    print("Multiplicand: " + value1)
    print("Multiplier:   " + value2)
    print("Product:      " + res)
    for i in range(32):
        if value2[31] == '0':
            print("Молодший біт 0, робимо зсув Multiplicand <-- вліво, Multiplier --> вправо  ")
        if value2[31] == '1':
            res = sumFunc(value1, res)
            print("Молодший біт 1, додаємо Multiplicand в Product і записуємо в Product, \nРобимо зсув Multiplicand <-- вліво, Multiplier --> вправо  ")
            if len(res) == 65:
                res = res[1:]
        value2 = '0' + value2[:31]
        value1 = value1[1:] + '0'
        print("\nІтерація:    ", i+1)
        print("Multiplicand: " + value1)
        print("Multiplier:   " + value2)
        print("Product:      " + res)
    if sign[1] != sign[0]:
        res = changeSign(res)
    print("\nResult:      ", res)
    print("\n\n\n")

def changeSign(value):
    res = ''
    for i in range(len(value)):
        if value[i] == '0':
            res = res + '1'
        elif value[i] == '1':
            res = res + '0'
    res = sumFunc(res, (len(value)-1) * '0' + '1')
    return res

