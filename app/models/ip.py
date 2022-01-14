import math

from app.constants import CLASS_A_RANGE, CLASS_B_RANGE, CLASS_C_RANGE, BITMASK_TO_MASK
from app.utils import  binary_formater, decimal_to_binary, octet_formater


class Ip:

    ip = []
    network = []
    broadcast = []
    mask = []
    bit_mask = 0
    first_host = []
    last_host = []
    hosts_number = 0
    class_ = ""

    def __init__(self, ip, mask):
        self.clear()
        octets = ip.split('.')

        #: validade entries
        #: A brief check if the IP is valid
        if len(ip.split('.')) != 4: 
            raise ValueError(f'Missing value for an for IP')

        for octet in octets:
            if int(octet) not in range(0,256):
                raise ValueError(f'Invalid number for IP')
        
        if mask not in BITMASK_TO_MASK.values():
            raise ValueError(f' {mask} Invalid number for mask')

        
        self.ip = ip.split('.')
        self.mask = mask.split('.')
        for i in range(len(self.ip)):
            self.network.append(int(self.ip[i]) & int(self.mask[i]))
            self.broadcast.append(( ~int(self.mask[i]) & 255 ) | int(self.network[i]))
            if i == len(self.ip) - 1:
                self.last_host.append(int(self.broadcast[i]) & ~1)
                self.first_host.append(int(self.network[i])^1)
            else:   
                self.last_host.append(int(self.broadcast[i]))
                self.first_host.append(int(self.network[i]))

        self.set_bitmask(binary_formater(self.mask))
        self.set_hostnumber()
        self.set_class(self.network)

    def set_bitmask(self, mask): # 
        """A method to calculate a number of valid hosts.
           based on bitmask number, that way this method must
           be called before set_bitmask method
        """
        aux = "".join(mask)
        self.bit_mask = aux.count('1')

    def set_hostnumber(self):
        """A method to calculate a number of valid hosts.
           based on bitmask number, that way this method must
           be called before set_bitmask method
        """

        if self.bit_mask != 0 or not None: 
            self.hosts_number = int(math.pow(2, 32 - self.bit_mask) - 2) if self.bit_mask != 32 else 1

    def set_class(self,network):
        """A method to calculate which set the classe type
           Based on first octect of the Ip adress
        """
        if network[0]:
            if network[0] in CLASS_A_RANGE:
                self.class_ = "A"
            elif network[0] in CLASS_B_RANGE:
                self.class_ = "B"
            else:
                self.class_= "C"
    @staticmethod
    def get_dictionary(self):
        return {
                'ip': self.ip,
                'network': self.network,
                'broadcast': self.broadcast,
                'class':self.class_,
                'hosts_number':self.hosts_number,
                'last_host':self.last_host,
                'first_host':self.first_host,
                'prefix':self.bit_mask,
                'mask':self.mask
        }

    def clear(self):
        """Clear some list variable to avoid repeatment"""
        self.last_host.clear()
        self.first_host.clear()
        self.broadcast.clear()
        self.network.clear()


class Decimal(Ip):

    def __init__(self, ip,mask):
        super().__init__(ip, mask)
        self.ip = octet_formater(self.ip)
        self.network = octet_formater(self.network)
        self.mask = octet_formater(self.mask)
        self.first_host = octet_formater(self.first_host)
        self.last_host = octet_formater(self.last_host)
        self.broadcast = octet_formater(self.broadcast)

class Binary(Ip):
    
    def __init__(self, ip,mask):
        super().__init__(ip, mask)
        self.ip = octet_formater(binary_formater(self.ip))
        self.network = octet_formater(binary_formater(self.network))
        self.mask = octet_formater(binary_formater(self.mask))
        self.first_host = octet_formater(binary_formater(self.first_host))
        self.last_host = octet_formater(binary_formater(self.last_host))
        self.broadcast = octet_formater(binary_formater(self.broadcast))
