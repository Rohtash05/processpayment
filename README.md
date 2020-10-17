# Payment Processing 

`Payment Processing` is a project based on FLASK and will be doing following items:- 
- Check the Card Details 
- Validate the Payload
- Raise an error if anything fails on payload or server
- Process the Payment in 3 different Gateways based on below condition
```
The payment gateway that should be used to process each payment follows the next set of
business rules:
a) If the amount to be paid is less than £20, use CheapPaymentGateway.
b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
Otherwise, retry only once with CheapPaymentGateway.
c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
in case payment does not get processed.
```
- Project is based on TDD and have test cases for all methods


## How to start

### Prerequisite
- Install Python3, pip
- Create and activate Virtualenv if you want
    - `virtualenv <project_name>`
    - `source <project_name>/bin/activate`
- Install the requirements by `pip install -r requirements.txt`

### To Start

```
FLASK_APP=start.py flask run --host 0.0.0.0 --port 8080
```

To Run in debug mode

```
FLASK_APP=start.py FLASK_ENV=development flask run --host 0.0.0.0 --port 8080
```

To run the tests
```sh
python test_payload.py
python test_payment_gateway.py
```

Tests are based on `unittest`

### Usage
Trigger http://127.0.0.1:8080/processpayment as POST method with the following payload:

```json
{
    "CreditCardNumber":"42424242424242",
    "CardHolder":"Test card Holder",
    "ExpirationDate":"02/2021",
    "SecurityCode":"576",
    "Amount":21.88,
}
```

Extra Params to test the different mocks
- cheap_success: true - To test the Cheap Payment Success
- cheap_success: false - To test the Cheap Payment Failure
- cheap_not_available: true - To test the non availability of cheap payment gateway
- expensive_success: true - To test the Expensive Payment Success
- expensive_success: false - To test the Expensive Payment Failure
- expensive_not_available: true - To test the non availability of Expensive payment gateway
- premium_success: true - To test the Premium Payment Success
- premium_success: false - To test the Premium Payment Failure
- premium_not_available: true - To test the non availability of Premium payment gateway
 
e.g.

```sh
curl --location --request POST 'http://localhost:8080/processpayment' \
--header 'Content-Type: application/json' \
--data-raw '{
    "CreditCardNumber":"42424242424242",
    "CardHolder":"Test Card Holder Name",
    "ExpirationDate":"02/2021",
    "SecurityCode":"576",
    "Amount":21.88,
    "expensive_success": true,
}'
```

**The code is following the pep8 standards**