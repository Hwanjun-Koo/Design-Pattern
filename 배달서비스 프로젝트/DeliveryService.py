import time
import copy
import tkinter as tk

#배달 상태를 관찰하고 알림을 보내는 옵저버 생성
class Observer:
    def update(self):
        pass

class DeliveryObserver(Observer):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.label = tk.Label(self.root, text="")
        self.label.pack()
        self.root.withdraw()
        
    def clear_label_and_close_window(self):
        self.label.config(text="")
        self.root.withdraw()  # Hide the window
        
    def show_message(self, message):
        self.root.deiconify()  # Show the window
        self.label.config(text = message)
        self.root.after(2000, self.clear_label_and_close_window)
        
    def update(self, state):
        if state == "요리 중":
            print(f"현재 배달 상태: {state}")
            self.show_message("주문이 접수되었습니다.")
        elif state == "배달 출발":
            print(f"현재 배달 상태: {state}")
            self.show_message("배달이 시작되었습니다.")
        elif state == "배달 완료":
            print(f"현재 배달 상태: {state}")
            self.show_message("배달이 완료되었습니다. 맛있게 드세요^^")
        else:
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
        
    def update_state(self, states):
        if states:
            self.restaurant.setState(states[0])
            self.observer.root.after(1000, self.update_state, states[1:])
        else:
            self.default_order.order()
            self.observer.root.quit()
        
    def order_process(self):
        states = ["주문 접수", "요리 중", "배달 출발", "배달 중", "배달 완료"]
        self.observer.root.after(0, self.update_state, states)
        self.observer.root.mainloop()
                
facade = DeliveryProcess()
facade.order_process()    


    
        
        

