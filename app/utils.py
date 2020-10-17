#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify
from datetime import datetime
import re


class BadRequest(Exception):
    '''
        Wrapper for Bad Request Exception
    '''

    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self.message


def make_error(status, status_code, message):
    '''Function to create the error response in proper format
    '''

    response = jsonify({'status': status, 'reason': message})
    response.status_code = status_code
    return response


def check_expiry_date(date):
    '''
        Method to Validate the Expiry Date of the Card
    '''
    regex = '(0[1-9]|10|11|12)/20[0-9]{2}$'
    if not re.match(regex, date):
        raise BadRequest("Date is not Valid")

    month, year = int(date.split('/')[0]), int(date.split('/')[1])
    expiry_date = to_day_1_datetime(datetime(year, month, 1))
    current_date = to_day_1_datetime(datetime.now())

    if expiry_date < current_date:
        raise BadRequest("Expire Date cannot be in past")


def validate_card(card):

    regex = re.compile(
            '^(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}'
            '|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}'
            '|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13}'
            '|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}'
            '|(?:2131|1800|35\d{3})\d{11})$'
            )
    if not re.match(regex, card):
        raise BadRequest('Please Enter a Valid Card Number')


def to_day_1_datetime(date):
    '''
        Use the Day as Day1 in the Datetime to help in calculations
    '''
    return date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def validate(data):
    '''
        Method to Validate the payload entered by the User.
    '''
    try:
        card_number = data['CreditCardNumber']
        name = data['CardHolder']
        expiry_date = data['ExpirationDate']
        security_code = data.get('SecurityCode')
        amount = data['Amount']

        if not isinstance(name, str):
            raise BadRequest('Name should be a string')
        if security_code and not isinstance(security_code, str):
            raise BadRequest('Security Code should be a string')
        if security_code and len(security_code) != 3:
            raise BadRequest('Security Code must be of 3 digits')
        if not isinstance(amount, float):
            raise BadRequest('Amount Should be decimal')
        if int(amount) < 0:
            raise BadRequest('Amount Should not be less than zero')
        check_expiry_date(expiry_date)
        validate_card(card_number)
    except KeyError as e:
        raise BadRequest(f"{str(e)} is mandatory")
