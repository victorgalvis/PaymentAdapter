#####Paso 1: Definir las Interfaces de los Métodos de Pago

class CreditCardPayment:
    def process_credit_card_payment(self, card_number, amount):
        """Interfaz para el sistema de pago con tarjeta de crédito"""
        return f"Pagando {amount} usando tarjeta de crédito {card_number}."


class DebitCardPayment:
    def process_debit_card_payment(self, card_number, amount):
        """Interfaz para el sistema de pago con tarjeta de débito"""
        return f"Pagando {amount} usando tarjeta de débito {card_number}."


class PayPalPayment:
    def make_payment(self, email, amount):
        """Interfaz para el sistema de pago con PayPal"""
        return f"Pagando {amount} usando PayPal cuenta {email}."



######Paso 2: Crear el Adaptador Unificado
# Adaptador que permite usar PayPal como un método de pago de tarjeta de crédito
# 
class PaymentAdapter:
    def process_payment(self, identifier, amount):
        """Interfaz común que todos los adaptadores deben implementar"""
        pass

class CreditCardAdapter(PaymentAdapter):
    def __init__(self, credit_card_payment):
        """Adaptador para tarjetas de crédito"""
        self.credit_card_payment = credit_card_payment

    def process_payment(self, identifier, amount):
        return self.credit_card_payment.process_credit_card_payment(identifier, amount)

class DebitCardAdapter(PaymentAdapter):
    def __init__(self, debit_card_payment):
        """Adaptador para tarjetas de débito"""
        self.debit_card_payment = debit_card_payment

    def process_payment(self, identifier, amount):
        return self.debit_card_payment.process_debit_card_payment(identifier, amount)

class PayPalAdapter(PaymentAdapter):
    def __init__(self, paypal_payment):
        """Adaptador para PayPal"""
        self.paypal_payment = paypal_payment

    def process_payment(self, identifier, amount):
        return self.paypal_payment.make_payment(identifier, amount)



#####Paso 3: Uso de los Adaptadores

# Create instances of payment methods
credit_card_payment = CreditCardPayment()
debit_card_payment = DebitCardPayment()
paypal_payment = PayPalPayment()

# Create adapters for each payment method
credit_card_adapter = CreditCardAdapter(credit_card_payment)
debit_card_adapter = DebitCardAdapter(debit_card_payment)
paypal_adapter = PayPalAdapter(paypal_payment)

# Using adapters to make payments
print(credit_card_adapter.process_payment("1234-5678-9012-3456", 100000))
print(debit_card_adapter.process_payment("9876-5432-1098-7654", 50000))
print(paypal_adapter.process_payment("victorgalvis@yopmail.com", 75000))
