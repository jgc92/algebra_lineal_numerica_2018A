import numpy as np

def int2bin(dec_num):
    rem_list = []
    dec_num = int(dec_num)

    while dec_num > 0:
        rem = dec_num % 2
        rem_list.append(rem)
        dec_num = dec_num // 2

    bin_str = ""
    while not len(rem_list) == 0:
        bin_str += str(rem_list.pop())

    return bin_str

def dec2bin(dec_num):
    dec = np.modf(dec_num)
    dec = dec[0]
    result = []
    samples = []

    for i in range(52):
        test = np.modf(dec * 2)
        dec = np.around(test[0],1)
        samples.append(dec)

        if test[1] >= 1:
            result.append(str(1))
        else:
            result.append(str(0))
            
    if dec*2 >= 1:
        result.append(str(1))
    else:
        result.append(str(0))

    return result

def exp_mant(int_bin, dec_bin):
    exp_int = (len(int_bin) - 1) + 1023
    exp_bin = int2bin(exp_int)
    
    mantissa = int_bin[1:] + ''.join(dec_bin)
    while len(mantissa) > 52:
        mantissa = mantissa[:-1]

    return [exp_bin, mantissa]

def num2bin(num):
    if num >= 0:
        sign = '0'
    else:
        sign = '1'

    int_bin = int2bin(num)
    dec_bin = dec2bin(num)
    
    exp, mantissa = exp_mant(int_bin, dec_bin)

    result = sign + '|' + exp + '|' + mantissa
    return [int_bin, result]



def bin2num(bin):
    bin = str(bin)
    bin = bin[::-1]
    summ = 0

    for i,x in enumerate(bin):
        if x != '0':
            summ += 2**(i)

    power = len(str(summ))
    norm = '0.' + str(summ) + 'E' + str(power)

    return [summ, norm]


print(num2bin(34558))

