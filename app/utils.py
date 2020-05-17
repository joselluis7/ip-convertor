

def decimal_to_binary(decimal):
    """Convert decimal number to binary
    
    Args:
        decimal {str} -- a decimal number to be converted

    returns: 
        str -- binary converted
    """
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
    """ Turn  number into  four binary octect
    
    Args:
        ip {list} -- list containing octect of an ip number

    returns: 
        list -- containg four position of binary octect 
        like ["10111101","01010110,"10001001","00000010"]
    """
    binary_ip = []
    for i in ip:
        binary_ip.append(decimal_to_binary(int(i)))
    return binary_ip


def octet_formater(ip):
    """Set the final format of ip adding . (dot)
    
    Args:
        ip {list} - list containing 4 position wich represent octect of an ip number

    returns: 
        str -- containing an ip in commom format
    """
    octet_form = "" 
    for i in range(len(ip) - 1):
        octet_form += str(ip[i]) + "."
    octet_form += str(ip[i + 1])
    return octet_form