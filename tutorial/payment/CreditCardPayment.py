from PaymentGateway import PaymentGateway

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Thanh toán bằng Thẻ Tín Dụng...")

payment = CreditCardPayment()
payment.process_payment(100)