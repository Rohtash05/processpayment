PAYMENT_RESPONSE = {
    'SUCCESS': {'success': True, 'message': 'Payment Succeded'},
    'FAILURE': {'success': False, 'message': 'Payment Failed'}
}


class PaymentGateway:
    def __init__(self, data):
        self.payment_data = data
        pass

    def PremiumPaymentGateway(self):
        if self.payment_data.get('premium_success') is True:
            return True
        elif self.payment_data.get('premium_not_available') is True:
            return "premium_not_available"
        else:
            return False

    def ExpensivePaymentGateway(self):
        if self.payment_data.get('expensive_success') is True:
            return True
        elif self.payment_data.get('expensive_not_available') is True:
            return "expensive_not_available"
        else:
            return False

    def CheapPaymentGateway(self):
        if self.payment_data.get('cheap_success') is True:
            return True
        elif self.payment_data.get('cheap_not_available') is True:
            return "cheap_not_available"
        else:
            return False


class ProcessPayment:
    def __init__(self, data):
        self.payment_data = data

    def use_payment(self):
        payment_data = self.payment_data
        # Init the Payment Gateway Config
        payment_gateway = PaymentGateway(payment_data)

        # Check the amount is less than 20, then trigger Cheap Gateway
        if payment_data['Amount'] <= 20:
            res = payment_gateway.CheapPaymentGateway()
            if res is True:
                return PAYMENT_RESPONSE['SUCCESS']
            else:
                return PAYMENT_RESPONSE['FAILURE']

        # Check the amount is greater than 20 and less than 500
        # Then trigger the Expensive Payment Gateway
        # if Expensive failed, Check with Cheap
        if payment_data['Amount'] > 20 and payment_data['Amount'] <= 500:
            # Check the payment with Expensive
            res = payment_gateway.ExpensivePaymentGateway()
            if res is True:
                return PAYMENT_RESPONSE['SUCCESS']

            elif res == 'expensive_not_available':
                # Check with Cheap Payment Gateway
                cheap_payment_res = payment_gateway.CheapPaymentGateway()
                if cheap_payment_res is True:
                    return PAYMENT_RESPONSE['SUCCESS']
                # If Cheap Also Not Available Return Failure
                elif cheap_payment_res == "cheap_not_available":
                    return PAYMENT_RESPONSE['FAILURE']
                # Any other error, Return failure
                else:
                    return PAYMENT_RESPONSE['FAILURE']
            else:
                return PAYMENT_RESPONSE['FAILURE']

        # If Amount is greater tha 500
        # Try with Premium Gateway 3 times, if failed return Failure
        if payment_data['Amount'] > 500:
            for i in range(3):
                res = payment_gateway.PremiumPaymentGateway()
                # If Payment Succedeed
                if res is True:
                    return PAYMENT_RESPONSE['SUCCESS']
            # Return Failure after trying three times and payment doesn't
            # succeded
            return PAYMENT_RESPONSE['FAILURE']
