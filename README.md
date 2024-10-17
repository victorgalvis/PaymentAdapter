# Patrón Adapter (Adaptador) 

**Caso:**
En una empresa de tecnología se usa una aplicación de comercio electrónico que integra varios métodos de pago, como tarjetas de débito, tarjetas de crédito y PayPal, se ha decidido implementar un sistema que permita manejar las transacciones de forma unificada. Cada método de pago tiene su propia API, lo que genera la necesidad de adaptarlas para que trabajen juntas sin problemas.


# payment 
**Implementación en Python:** 


1. Creación de Interfaces específicas:
Se definen interfaces PaymentAdapter

2. Se crean clases Adaptable: 
Las clases (CreditCardPayment, DebitCardPayment, PayPalPayment)

3. Se crean clases Adaptable:
adaptadores (CreditCardAdapter, DebitCardAdapter, PayPalAdapter)

4. Cliente: ECommerceApp

5. Uso:

> [!NOTE]
>**Instanciar los adaptables**
>tarjeta_credito = CreditCardPayment()
>tarjeta_debito = DebitCardPayment()
>paypal = PayPalPayment()
> 

> [!NOTE]
>**Instanciar los adaptadores**
>adapter_credito = CreditCardAdapter(tarjeta_credito)
>adapter_debito = DebitCardAdapter(tarjeta_debito)
>adapter_paypal = PayPalAdapter(paypal)
> 


> [!TIP]
>**Cliente ECommerceApp: **
> 
>ecommerce_app = ECommerceApp(adapter_credito)
>ecommerce_app.realizar_pago(100000)  
>
>ecommerce_app = ECommerceApp(adapter_debito)
>ecommerce_app.realizar_pago(50000)  
>
>ecommerce_app = ECommerceApp(adapter_paypal)
>ecommerce_app.realizar_pago(15000)
> 



