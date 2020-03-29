#coding:utf-8
from flask import Flask, render_template, request, redirect
from .model.utils import octet_formater, binary_formater

decimal_format = {}
binary_format = {}

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():

    if request.method == 'POST':
        
        ip = request.form['ipaddress']
        mask = request.form['mask']

        decimal_format.clear()
        binary_format.clear()

        try:
            ip_calculator(ip,mask)
            return redirect('/')
        except:
            return "Alguma coisa correu mal"
    else:
        return render_template('index.html',decimal_format=decimal_format,network_type='private',bitmask="24", host_number=254,binary_format=binary_format)


def ip_calculator(ip, mask):

    ip = ip.split('.')
    mask = mask.split('.')
    ip_broadcast, ip_network,ip_min, ip_max = [],[],[],[]
    for i in range(len(ip)):
        ip_network.append(int(ip[i]) & int(mask[i]))
        ip_broadcast.append((~int(mask[i]) & 255 )|int(ip_network[i]))
        if i == len(ip) - 1:
            ip_max.append(int(ip_broadcast[i]) & ~1)
            ip_min.append(int(ip_network[i])^1)
        else:   
           ip_max.append(int(ip_broadcast[i]))
           ip_min.append(int(ip_network[i]))

    """
    Separar as funcoes, e incluir objectos
    """
    decimal_format['ip'] = octet_formater(ip)
    decimal_format['mask'] = octet_formater(mask)
    decimal_format['network'] = octet_formater(ip_network)
    decimal_format['broadcast'] = octet_formater(ip_broadcast)
    decimal_format['min'] = octet_formater(ip_min)
    decimal_format['max'] = octet_formater(ip_max)
    binary_format['ip'] = octet_formater(binary_formater(ip))
    binary_format['mask'] = octet_formater(binary_formater(mask))
    binary_format['network'] = octet_formater(binary_formater(ip_network))
    binary_format['broadcast'] = octet_formater(binary_formater(ip_broadcast))
    binary_format['max'] = octet_formater(binary_formater(ip_max))
    binary_format['min'] = octet_formater(binary_formater(ip_min))

    #binary_format['ip'] =  octet_formater()


