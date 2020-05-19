#coding:utf-8
from flask import Flask, render_template, request
from .models.ip import Decimal, Binary  
from .constants import BITMASK_TO_MASK



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():

    decimal = None
    binary = None
    if request.method == 'POST':    
        ip = request.form['ipaddress']
        mask = request.form['mask']

        #: a before check if mask was given in bitmask form and
        #: replace it for his respective value in decimal form
        mask = BITMASK_TO_MASK[mask] if mask in BITMASK_TO_MASK else mask

        try:
            decimal = Decimal(ip,mask)
            binary = Binary(ip, mask)
        except ValueError as error:
            return "Você digitou um valor errado para mascara ou ip"

    return render_template('index.html', decimal=decimal, binary=binary)
