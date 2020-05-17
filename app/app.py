#coding:utf-8
from flask import Flask, render_template, request, redirect
from .models.ip import Ip
from .constants import BITMASK_TO_MASK
from .utils import decimal_to_binary, binary_formater, octet_formater



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():

    ip_address = ""
    if request.method == 'POST':    
        ip = request.form['ipaddress']
        mask = request.form['mask']

        #: a before check if mask was given in bitmask form and
        #: replace it for his respective value in decimal form
        mask = BITMASK_TO_MASK[mask] if mask in BITMASK_TO_MASK else mask

        try:
            ip_address = Ip(ip, mask)
    
            #: Add IP in binary form
            #: Add IP in octal form
            #: Add IP in hexadecimal form

        except ValueError as error:
            return "Você digitou um valor errado para mascara ou ip"

    return render_template('index.html', decimal=ip_address)
