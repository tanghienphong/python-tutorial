from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# class CreditCardPayment(PaymentGateway):
#     def process_payment(self, amount):
#         print(f"Thanh toán bằng Thẻ Tín Dụng...")

# class PayPalPayment(PaymentGateway):
#     def process_payment(self, amount):
#         print(f"Thanh toán qua PayPal...")


# payment = CreditCardPayment()
# payment.process_payment(100)

# payment = PayPalPayment()
# payment.process_payment(200)
