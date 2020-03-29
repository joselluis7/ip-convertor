#-*-coding:utf-8

class DecimalIP():

    def __init__(self, ip,mask):
        self.ip_address = ip
        self.netmask = mask
        self.broadcast = ""
        self.network = ""
        self.max_host = ""
        self.min_host = ""
        self.valid_host = 0
        self.num_host = 0

    def __repr__(self):
        return "%r"
