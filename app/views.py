#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import exc
from app import app

from flask import request, jsonify
from app.utils import make_error, BadRequest, validate

from app.payment import ProcessPayment


@app.after_request
def set_header(response):
    '''Set Response Header to return the content type as application/json
    '''

    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/processpayment', methods=['POST'])
def process_payment():
    '''Process Payment Method
    :param CreditCardNumber(required): the CreditCardNumber of the Card.
    :type CreditCardNumber: string
    :param CardHolder(required): the Name of the Card Holder
    :type CardHolder: string
    :param ExpirationDate(required): the expiry date of the card in mm/yyyy
    :type ExpirationDate: string
    :param SecurityCode(optional): the SecurityCode of the Card (3 digit)
    :type SecurityCode: string
    :param Amount(required): the amount to be deducted from the card
    :type Amount: decimal
    :returns: message
    :rtype: dictionary
    '''

    data = request.get_json()
    if data:
        try:
            data = dict(data)
            # Validate the Payload
            validate(data)
            # Init the ProcessPayment
            payment = ProcessPayment(data)
            # Execute the Use Payment Method
            result = payment.use_payment()
            return jsonify(result), 200
        except (BadRequest, KeyError, exc.IntegrityError) as e:
            return make_error('failure', 400, str(e))
        except Exception as e:
            return make_error('Internal Server Error',
                              500,
                              'Internal Server Error')
    else:
        return make_error('failure', 400, 'Please send card details')
