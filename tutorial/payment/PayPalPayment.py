from PaymentGateway import PaymentGateway

class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Thanh toán qua PayPal...")

payment = PayPalPayment()
payment.process_payment(200)
