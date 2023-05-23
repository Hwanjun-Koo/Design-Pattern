import time
import copy

#배달 상태를 관찰하고 알림을 보내는 옵저버 생성
class Observer:
    def update(self):
        pass

class DeliveryObserver:
    def update(self, state):
        print(f"현재 배달 상태: {state}")
#옵저버가 관찰할 식당   
class Restaurant:
    def __init__(self):
        self.observers = []
        self.state = None
        
    def register(self, observer):
        self.observers.append(observer)
        
    def notify(self):
        for observer in self.observers:
            observer.update(self.state)
            
    def setState(self, state):
        self.state = state
        self.notify()

#주문서 작성 양식을 Prototype 패턴으로 작성           
class OrderForm:
    def __init__(self, food:str, customer:str, address:str, vehicle:str, plastic:bool, request:str):
        self.food = food
        self.customer = customer
        self.address = address
        self.vehicle = vehicle
        self.plastic = plastic
        self.request = request
        
    def order(self):
        self.usingPlastic = "O" if self.plastic else "X"
        print(f"메뉴명: {self.food}")
        print(f"주문자: {self.customer}")
        print(f"주소: {self.address}")
        print(f"배달 방식: {self.vehicle}")
        print(f"일회용품 사용 여부: {self.usingPlastic}")
        print(f"요청사항: {self.request}")
    
    def receipt(self,total_price):
        self.total_price = total_price
        self.usingPlastic = "O" if self.plastic else "X"
        print(f"메뉴명: {self.food}")
        print(f"주문자: {self.customer}")
        print(f"주소: {self.address}")
        print(f"배달 방식: {self.vehicle}")
        print(f"일회용품 사용 여부: {self.usingPlastic}")
        print(f"요청사항: {self.request}")
        print(f"총 금액: {self.total_price}")
    
    def clone(self):
        return copy.deepcopy(self)
    
class OrderPrototype:
    def __init__(self):
        self.order = OrderForm("", "", "", "", True, "")
        
    def create(self, food:str, customer:str, address:str, vehicle:str, plastic:bool, request:str) -> OrderForm:
        self.order.food = food
        self.order.customer = customer
        self.order.address = address
        self.order.vehicle = vehicle
        self.order.plastic = plastic
        self.order.request = request
        return self.order.clone()
    
#주문 상태를 자동으로 업데이트 시켜주는 Facade 패턴     
class DeliveryProcess:
    def __init__(self):
        self.restaurant = Restaurant()
        self.observer = DeliveryObserver()
        self.restaurant.register(self.observer)
        self.proto_order = OrderPrototype()
        self.default_order = self.proto_order.create("", "", "", "", True, "")
        
    def order_process(self):
        states = ["주문 확인", "주문 접수", "요리 중", "배달 출발", "배달 중", "배달 도착"]
        for state in states:
            self.restaurant.setState(state)
            time.sleep(1)
        self.default_order.order()
                
facade = DeliveryProcess()
facade.order_process()    

       
    
        
        

