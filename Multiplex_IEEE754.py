import Multiplex
import Division

def binaryToDecimal(value):
    res = 0
    for i in range(len(value)):
        res += int(value[len(value) - i - 1]) * 2 ** i
    return res


def floatToBinary(value):
    isNegative = False
    if value < 0:
        value *= -1
        isNegative = True
    index = str(value).find('.')
    first_part = bin(int(str(value)[:index])).replace("0b", "")
    second_part_dec = float('0' + str(value)[index:])
    second_part_bin = ''
    for i in range(24):
        if second_part_dec - 2**(-i-1) >= 0:
            second_part_bin += '1'
            second_part_dec -= 2**(-i-1)
        else:
            second_part_bin += '0'
    full = first_part + '.' + second_part_bin
    index = full.find('.')
    first_one = 1 if full.find('1') == 0 else full.find('1')
    order = index - first_one
    full = full.replace('.', '')
    full = full[:index-order] + '.' + full[index-order:]
    res = '1' if isNegative else '0'
    res += Multiplex.base32(Multiplex.decimalToBinary(127 + order))[24:] + full[full.find('.')+1:]
    if len(res) < 32:
        res = res + "0"*(32-len(res))
    res = res[:32]
    if isNegative:
        value *= -1

    return res

def xor(value1, value2):
    return '0' if value1[0] == value2[0] else '1'


def multiplexNatural(value1, value2):

    value1 = "0" * 24 + value1
    res = 48 * '0'
    for i in range(24):
        if value2[23] == '1':
            res = Multiplex.sumFunc(value1, res)
            if len(res) == 49:
                res = res[1:]
        value2 = '0' + value2[:23]
        value1 = value1[1:] + '0'
    return res


def multiplex(value1, value2):
    dcvalue1 = value1
    dcvalue2 = value2
    print("Value1 = ", value1)
    print("Value2 = ", value2)
    value1 = floatToBinary(value1)
    value2 = floatToBinary(value2)
    if len(value2) < 32:
        value2 = value2 + "0"*(32-len(value2))
    if len(value1) < 32:
        value1 = value1 + "0"*(32-len(value1))
    print("Value1 = ", value1)
    print("Value2 = ", value2)
    print("Виконуємо XOR між бітом зі знаком:               ", xor(value1, value2))
    mantissa = multiplexNatural('1' + value1[9:], '1' + value2[9:])
    print("Перемножуємо мантиси множника1 та множника2:     ", mantissa)
    mantissa = mantissa[mantissa.find('1') + 1:]
    print("Нормалізовуємо мантису:                          ", mantissa)
    order = Multiplex.sumFunc(value1[1:9], value2[1:9], True)
    print("Додаємо порядки множника1 та множника2:          ", order)
    order = Division.subtraction(order, '001111111' if len(order) == 9 else '01111111')[1:]
    if len(order) < 8:
        order = "0" * (8 - len(order))+order
    order = Multiplex.sumFunc('00000001', order)
    print("Віднімаємо зміщення (127 біт) та додаємо 1:      ", order)
    res = xor(value1, value2) + order + mantissa
    res = res + (32 - len(res)) * '0' if len(res) < 33 else res[:32]

    print('Pезультат: ', res)

    print("           ", floatToBinary(dcvalue1 * dcvalue2))

    return res



