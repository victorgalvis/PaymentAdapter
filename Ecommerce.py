from abc import ABC, abstractmethod

#Interfaz 
class PaymentAdapter(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

#Clases adaptables
class CreditCardPayment:
    def process_credit_card(self, monto):
        print(f"Procesando pago con tarjeta de crédito por ${monto}")

class DebitCardPayment:
    def process_debit_card(self, monto):
        print(f"Procesando pago con tarjeta de débito por ${monto}")

class PayPalPayment:
    def make_payment(self, monto):
        print(f"Realizando pago con PayPal por ${monto}")

#Adaptadores (Adapter)
class CreditCardAdapter(PaymentAdapter):
    def __init__(self, credit_card_payment):
        self.credit_card_payment = credit_card_payment

    def pagar(self, monto):
        # Llama al método específico del objeto adaptable
        self.credit_card_payment.process_credit_card(monto)

class DebitCardAdapter(PaymentAdapter):
    def __init__(self, debit_card_payment):
        self.debit_card_payment = debit_card_payment

    def pagar(self, monto):
        # Llama al método específico del objeto adaptable
        self.debit_card_payment.process_debit_card(monto)

class PayPalAdapter(PaymentAdapter):
    def __init__(self, paypal_payment):
        self.paypal_payment = paypal_payment

    def pagar(self, monto):
        # Llama al método específico del objeto adaptable
        self.paypal_payment.make_payment(monto)


#Cliente: ECommerceApp
class ECommerceApp:
    def __init__(self, payment_adapter):
        self.payment_adapter = payment_adapter

    def realizar_pago(self, monto):
        # El cliente utiliza la interfaz común para realizar el pago
        self.payment_adapter.pagar(monto)
          
####USO:
# Instanciar los adaptables
tarjeta_credito = CreditCardPayment()
tarjeta_debito = DebitCardPayment()
paypal = PayPalPayment()

# Instanciar los adaptadores
adapter_credito = CreditCardAdapter(tarjeta_credito)
adapter_debito = DebitCardAdapter(tarjeta_debito)
adapter_paypal = PayPalAdapter(paypal)

# Cliente utilizando diferentes adaptadores
ecommerce_app = ECommerceApp(adapter_credito)
ecommerce_app.realizar_pago(100000)  


ecommerce_app = ECommerceApp(adapter_debito)
ecommerce_app.realizar_pago(50000)  

ecommerce_app = ECommerceApp(adapter_paypal)
ecommerce_app.realizar_pago(15000)  

