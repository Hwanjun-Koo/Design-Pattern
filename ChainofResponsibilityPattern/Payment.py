class Handler:
    def __init__(self):
        self.next_handler = None
    
    def setNext(self, handler):
        self.next_handler = handler
      
    def handle(self, req):
        if self.next_handler:
            return self.next_handler.handle(req)
        
        print("All paying methods failed")
        return None

class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == 'cash':
            print(f"Processing cash {req['amount']} won")
        else:
            print(f"CashHandler failed")
            super().handle(req)
            
class CreditCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'creditCard':
            print(f"Processing {req['amount']} won in Credit Card")
        else:
            print(f"CreditCardHandler failed")
            super().handle(req)
            
class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'debitCard':
            print(f"Processing {req['amount']} won in Debit Card")
        else:
            print(f"DebitCardHandler failed")
            super().handle(req)

cash_handler = CashHandler()
creditcard_handler = CreditCardHandler()
debitcard_handler = DebitCardHandler()

cash_handler.setNext(creditcard_handler)
creditcard_handler.setNext(debitcard_handler)

payment = {
    "method": "debitCard",
    "amount": 10000
}        
cash_handler.handle(payment)