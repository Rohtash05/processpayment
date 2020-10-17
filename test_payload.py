#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from app import payment, utils


class PayloadTest(unittest.TestCase):

    # Test Card Number

    def test_card_number(self):

        # Test VISA Card

        test_1 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_1 = dict(test_1)
        assert utils.validate(test_1) is None

        test_2 = {
            'CreditCardNumber': '4012888888881881',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_2 = dict(test_2)
        assert utils.validate(test_2) is None

        # Test Master Card

        test_3 = {
            'CreditCardNumber': '5555555555554444',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_3 = dict(test_3)
        assert utils.validate(test_3) is None

        test_4 = {
            'CreditCardNumber': '5105105105105100',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_4 = dict(test_4)
        assert utils.validate(test_4) is None

        # Test American Express Card

        test_5 = {
            'CreditCardNumber': '378282246310005',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_5 = dict(test_5)
        test = utils.validate(test_5)

        assert utils.validate(test_5) is None

        test_6 = {
            'CreditCardNumber': '371449635398431',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_6 = dict(test_6)
        assert utils.validate(test_6) is None

        # Discover Card

        test_7 = {
            'CreditCardNumber': '6011111111111117',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_7 = dict(test_7)
        assert utils.validate(test_7) is None

        test_8 = {
            'CreditCardNumber': '6011000990139424',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_8 = dict(test_8)
        assert utils.validate(test_8) is None

        test_9 = {
            'CreditCardNumber': 'tests',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_9 = dict(test_9)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_9)
        assert ex.exception.message \
            == 'Please Enter a Valid Card Number'

        test_10 = {
            'CreditCardNumber': '78979879789798798798798798798797',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_10 = dict(test_10)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_10)
        assert ex.exception.message \
            == 'Please Enter a Valid Card Number'

        test_11 = {
            'CreditCardNumber': 'tests798897987AFSDF@',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_11 = dict(test_11)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_11)
        assert ex.exception.message \
            == 'Please Enter a Valid Card Number'

    # Test Card Holder Name

    def test_card_holder(self):

        # Test No CardHolder

        test_1 = {
            'CreditCardNumber': '4242424242424242',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_1 = dict(test_1)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_1)
        assert ex.exception.message == "'CardHolder' is mandatory"

        # Test CardHolder Not string

        test_2 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 123,
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_2 = dict(test_2)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_2)
        assert ex.exception.message == 'Name should be a string'

        # Test Correct Details

        test_3 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'Test1',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_3 = dict(test_3)
        assert utils.validate(test_3) is None

    # Test Card Expiry date

    def test_expiry_date(self):

        # Test No Expiry Date

        test_1 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_1 = dict(test_1)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_1)
        assert ex.exception.message == "'ExpirationDate' is mandatory"

        # Test Past Expiry Date

        test_2 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '02/2018',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_2 = dict(test_2)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_2)
        assert ex.exception.message == 'Expire Date cannot be in past'

        # Test Invalid Date Format

        test_3 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '122020',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_3 = dict(test_3)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_3)
        assert ex.exception.message == 'Date is not Valid'

        test_4 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '2020/12',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_4 = dict(test_4)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_4)
        assert ex.exception.message == 'Date is not Valid'

        # Test Correct Details

        test_5 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'Test1',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_5 = dict(test_5)
        assert utils.validate(test_5) is None

    # Test Security Code

    def test_security_code(self):

        # Test No Security Code

        test_1 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '02/2021',
            'Amount': 512.88,
            }
        test_1 = dict(test_1)
        assert utils.validate(test_1) is None

        # Test Security Code not of length 3

        test_2 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '02/2022',
            'SecurityCode': '5766',
            'Amount': 512.88,
            }
        test_2 = dict(test_2)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_2)
        assert ex.exception.message \
            == 'Security Code must be of 3 digits'

        test_3 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '02/2022',
            'SecurityCode': 'ad',
            'Amount': 512.88,
            }
        test_3 = dict(test_3)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_3)
        assert ex.exception.message \
            == 'Security Code must be of 3 digits'

        # Test Security Code Not a String

        test_3 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'TEst',
            'ExpirationDate': '02/2022',
            'SecurityCode': 123,
            'Amount': 512.88,
            }
        test_3 = dict(test_3)
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_3)
        assert ex.exception.message \
            == 'Security Code should be a string'

        # Test Correct Details

        test_4 = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'Test1',
            'ExpirationDate': '02/2021',
            'SecurityCode': '576',
            'Amount': 512.88,
            }
        test_4 = dict(test_4)
        assert utils.validate(test_4) is None

    # Test Amount

    def test_amount(self):
        test_amount = {
            'CreditCardNumber': '4242424242424242',
            'CardHolder': 'Test Card Holder',
            'ExpirationDate': '02/2022',
            'SecurityCode': '576',
            'Amount': 512,
            }
        test_amount = dict(test_amount)

        # Test Positive Amount

        test_amount['Amount'] = 10
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_amount)
        assert ex.exception.message == 'Amount Should be decimal'

        # Test Negative Amount

        test_amount['Amount'] = -10
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_amount)

        assert ex.exception.message == 'Amount Should be decimal'

        test_amount['Amount'] = -10.10
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_amount)

        assert ex.exception.message \
            == 'Amount Should not be less than zero'

        # Test No Amount

        test_amount['Amount'] = None

        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_amount)
        assert ex.exception.message == 'Amount Should be decimal'

        # Test Zero Amount

        test_amount['Amount'] = 0

        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_amount)
        assert ex.exception.message == 'Amount Should be decimal'

        # Test Decimal Amount

        test_amount['Amount'] = 100.12

        assert utils.validate(test_amount) is None

        # Test Integer Amount

        test_amount['Amount'] = 100
        with self.assertRaises(utils.BadRequest) as ex:
            utils.validate(test_amount)
        assert ex.exception.message == 'Amount Should be decimal'


if __name__ == '__main__':
    unittest.main()
