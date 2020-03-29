
def dec2bin(decimal):
    
    binary=""
    stack = []
    bits = 0
    while bits < 8: # bit number
        rest = decimal % 2
        decimal = decimal//2
        stack.append(rest)
        bits += 1
    while stack:
        binary = binary + str(stack.pop())
    return binary

def binary_formater(ip):
    
    binary_ip = []
    for i in ip:
        binary_ip.append(dec2bin(int(i)))
    return binary_ip

def octet_formater(ip):

    octet_form = "" 
    for i in range(len(ip) - 1):
        octet_form += str(ip[i]) + "."
    octet_form += str(ip[i + 1])
    return octet_form