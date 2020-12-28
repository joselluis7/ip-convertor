from flask import Flask, render_template, request,jsonify, make_response

from .models.ip import Decimal, Binary  
from .constants import BITMASK_TO_MASK
from .jsonvalidate import validate_data



app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_all():
    decimal = None
    binary = None

    return render_template('index.html', decimal=decimal, binary=binary)


@app.route('/', methods=['POST'])
def index():

    decimal = None

    request_data = request.get_json('maskValue')
    if validate_data(request_data):
        return make_response({'error':'invalid json'},400)
    mask = request_data['maskValue']

    #: a before check if mask was given in bitmask form and
    #: replace it for his respective value in decimal form
    mask = BITMASK_TO_MASK[mask] if mask in BITMASK_TO_MASK else mask
    
    try:
        decimal = Decimal(request_data['ipValue'],mask)
        binary = Binary(request_data['ipValue'], mask)

        print(Decimal.get_dictionary(decimal))
        return jsonify({
                        'decimal': Decimal.get_dictionary(decimal),
                        'decimal': Decimal.get_dictionary(decimal)
                        })
    except ValueError as error:
        return make_response({'error':'mask value or ip incorrect'}, 422)