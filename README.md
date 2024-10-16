# Patrón Adapter (Adaptador) 

**Caso:**
En una empresa de tecnología se usa una aplicación de comercio electrónico que integra varios métodos de pago, como tarjetas de débito, tarjetas de crédito y PayPal, se ha decidido implementar un sistema que permita manejar las transacciones de forma unificada. Cada método de pago tiene su propia API, lo que genera la necesidad de adaptarlas para que trabajen juntas sin problemas.


# payment 
**Implementación en Python:** 


1. Definir las Interfaces de los Métodos de Pago:
Se definen interfaces para cada tipo de pago (tarjetas de crédito, débito y PayPal)

2. Crear el Adaptador Unificado:
Los adaptadores (CreditCardAdapter, DebitCardAdapter y PayPalAdapter) implementan una interfaz común (**PaymentAdapter**) para unificar la forma en que se manejan los pagos

3. Uso:
**Create instances of payment methods**
credit_card_payment = CreditCardPayment()
debit_card_payment = DebitCardPayment()
paypal_payment = PayPalPayment()

**Create adapters for each payment method**
credit_card_adapter = CreditCardAdapter(credit_card_payment)
debit_card_adapter = DebitCardAdapter(debit_card_payment)
paypal_adapter = PayPalAdapter(paypal_payment)

> [!TIP]
> **Using adapters to make payments**
> 
>print(credit_card_adapter.process_payment("1234-5678-9012-3456", 100000))
>print(debit_card_adapter.process_payment("9876-5432-1098-7654", 50000))
>print(paypal_adapter.process_payment("victorgalvis@yopmail.com", 75000))


