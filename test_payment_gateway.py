#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from app import payment, utils

payment_success = {'success': True, 'message': 'Payment Succeded'}

payment_failure = {'success': False, 'message': 'Payment Failed'}


class PaymentTest(unittest.TestCase):

    def test_cheap_payment_gateway(self):
        '''
            Test Cheap Payment Gateway
        '''

        # Test Cheap Gateway Success

        test_payment_payload = {'Amount': 18.10, 'cheap_success': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_success

        # Test Cheap Gateway Failure

        test_payment_payload = {'Amount': 18.10, 'cheap_success': False}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        # Test Cheap Gateway Not Available

        assert result == payment_failure

        test_payment_payload = {'Amount': 18.10,
                                'cheap_not_available': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_failure

    def test_expensive_payment_gateway(self):
        '''
            Test Expensive Payment Gateway
        '''

        # Test Expensive Gateway Success

        test_payment_payload = {'Amount': 21.10,
                                'expensive_success': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_success

        # Test Expensive Gateway Failure

        test_payment_payload = {'Amount': 22.10,
                                'expensive_success': False}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_failure

        # Test Expensive Gateway Not Available and cheap failure

        test_payment_payload = {'Amount': 22.10,
                                'expensive_not_available': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_failure

        # Test Expensive Gateway Not Available and cheap Success

        test_payment_payload = {'Amount': 22.10,
                                'expensive_not_available': True,
                                'cheap_success': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_success

    def test_premium_payment_gateway(self):
        '''
            Test Premium Payment Gateway
        '''

        # Test Premium Gateway Success

        test_payment_payload = {'Amount': 700.10,
                                'premium_success': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_success

        # Test Premium Gateway Not Available

        test_payment_payload = {'Amount': 700.10,
                                'premium_not_available': True}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_failure

        # Test Premium Gateway Failure

        test_payment_payload = {'Amount': 700.10,
                                'premium_success': False}

        init_payment = payment.ProcessPayment(test_payment_payload)
        result = init_payment.use_payment()

        assert result == payment_failure


if __name__ == '__main__':
    unittest.main()
