from flask import Flask, render_template, request,jsonify, make_response

from .models.ip import Decimal, Binary  
from .constants import BITMASK_TO_MASK



app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_all():
    decimal = None
    binary = None

    return render_template('index.html', decimal=decimal, binary=binary)


@app.route('/', methods=['POST'])
def index():

    decimal = None

    request_data = request.get_json('mask')
    mask = request_data['mask']
    print("TYPE: ",type(mask))
    #: a before check if mask was given in bitmask form and
    #: replace it for his respective value in decimal form
    mask = BITMASK_TO_MASK[mask] if mask in BITMASK_TO_MASK else mask
    
    try:
        decimal = Decimal(request_data['ip'],mask)
        binary = Binary(request_data['ip'], mask)
        return jsonify({
                        'decimal': Decimal.get_dictionary(decimal),
                        'binary': Binary.get_dictionary(binary)
                        })
    except ValueError as error:
        return make_response({'error':'mask value or ip incorrect'}, 422)