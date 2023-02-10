from Stack import Stack

def decimal_to_binary(dec_num):
    S = Stack()
    
    while dec_num > 0:
        r = dec_num % 2
        S.push(r)
        dec_num = dec_num // 2
    
    bin_num = ''
    
    while not S.is_empty():
        bin_num += str(S.pop())
    
    return bin_num

dec_num = int(input('Enter Decimal Number - '))

bin_num = decimal_to_binary(dec_num)

print(bin_num)

# T0 Validate ...  

print(int(bin_num,2))
