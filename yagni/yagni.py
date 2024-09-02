# Example: Payment Processing

# Over-engineered:


def process_payment(self, amount, payment_method):
    if payment_method == 'credit_card':
        pass
    elif payment_method == 'paypal':
        pass
    elif payment_method == 'bitcoin':
        pass


# YAGNI aligned:

def process_payment(self, amount, payment_method):
    if payment_method == 'credit_card':
        pass 


# Start by supporting only the payment methods you currently need. Add support for PayPal or Bitcoin later in the development cycle if the demand arises.