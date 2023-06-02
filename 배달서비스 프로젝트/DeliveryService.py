import time
import copy
import tkinter as tk
from DeliveryUI import DeliveryUI
from DeliveryApp import DeliveryApp

#배달 상태를 관찰하고 알림을 보내는 옵저버 생성
class Observer:
    def update(self):
        pass
    
    def start_ui(self):
        pass

class DeliveryObserver(Observer):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.label = tk.Label(self.root, text="")
        self.label.pack()
        self.root.withdraw() # 창 숨기기
        
    def clear_label_and_close_window(self):
        self.label.config(text="")
        self.root.withdraw()  
        
    def show_message(self, message):
        self.root.deiconify()  # 창 띄우기
        self.label.config(text = message)

    def show_receipt(self, receipt_text):
        self.root.deiconify()  
        self.text = tk.Text(self.root)
        self.text.pack()
        self.text.insert(tk.END, receipt_text)
        
    def update(self, state):
        if state == "요리 중":
            print(f"현재 배달 상태: {state}")
            self.show_message("주문이 접수되었습니다.")
        elif state == "배달 출발":
            print(f"현재 배달 상태: {state}")
            self.show_message("배달이 시작되었습니다.")
        elif state == "배달 중":
            print(f"현재 배달 상태: {state}")
            self.show_message("배달 중...")
            
        elif state == "배달 완료":
            print(f"현재 배달 상태: {state}")
            self.show_message("배달이 완료되었습니다. 맛있게 드세요^^")
        else:
            print(f"현재 배달 상태: {state}")
            
    def start_ui(self, chosen_vehicle, delivery_time):
        ui = DeliveryUI(chosen_vehicle, delivery_time)
        ui.start()
#옵저버가 관찰할 식당   
class Restaurant:
    def __init__(self, name, menu, vehicles):
        self.observers = []
        self.state = None
        self.name = name
        self.menu = menu
        self.vehicles = vehicles
        
    def register(self, observer):
        self.observers.append(observer)
        
    def notify(self):
        for observer in self.observers:
            observer.update(self.state)
            
    def setState(self, state):
        self.state = state
        self.notify()

    
#식당들을 저장할 데이터베이스를 Singleton 패턴으로 구축
class RestaurantDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RestaurantDatabase, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.restaurants = {}

    def add_restaurant(self, restaurant):
        self.restaurants[restaurant.name] = restaurant

    def get_restaurant(self, name):
        return self.restaurants.get(name, None)

    def get_all(self):
        return list(self.restaurants.values())

#주문서 작성 양식과 배달 완료 시 표시할 영수증을 Prototype 패턴으로 작성           
class OrderForm:
    def __init__(self, food:str, customer:str, address:str, vehicle:str, plastic:bool, request:str, restaurant_name:str):
        self.food = food
        self.customer = customer
        self.address = address
        self.vehicle = vehicle
        self.plastic = plastic
        self.request = request
        self.total_price = 0
        self.restaurant_name = restaurant_name
        
    def receipt(self):
        self.usingPlastic = "O" if self.plastic else "X"
        receipt_text = f"""
        가게명:{self.restaurant_name}
        메뉴명: {self.food}
        주문자: {self.customer}
        주소: {self.address}
        배달 방식: {self.vehicle}
        일회용품 사용 여부: {self.usingPlastic}
        요청사항: {self.request}
        총 금액: {self.total_price} 원
        """
        return receipt_text
    
    def clone(self):
        return copy.deepcopy(self)
    
class OrderPrototype:
    def __init__(self, restaurant_db):
        self.order = OrderForm("", "", "", "", True, "", "")
        self.restaurant_db = restaurant_db
        
    def create(self, restaurant_name:str, food:str, customer:str, address:str, vehicle:str, plastic:str, request:str) -> OrderForm:
        new_order = self.order.clone()
        new_order.restaurant_name = restaurant_name
        new_order.food = food
        new_order.customer = customer
        new_order.address = address
        new_order.vehicle = vehicle
        new_order.plastic = bool(plastic.lower() == "true")
        new_order.request = request
        return new_order
#주문 상태를 자동으로 업데이트 시켜주는 프로세스를 Facade 패턴으로 구현    
class DeliveryProcess:
    def __init__(self, restaurant_db):
        self.observer = DeliveryObserver()
        self.restaurant_db = restaurant_db
        self.proto_order = OrderPrototype(restaurant_db)
        self.current_order = None

    def get_user_input(self):
        # DeliveryApp 호출하여 pygame에서 주문 정보를 입력 받고 self.current_order 업데이트
        app = DeliveryApp(self.restaurant_db, self.current_order)
        user_inputs = app.get_user_input()
        return self.proto_order.create(*user_inputs)

    def order_process(self):
        self.current_order = self.get_user_input()
        self.restaurant = self.restaurant_db.get_restaurant(self.current_order.restaurant_name)
        self.restaurant.register(self.observer)
        self.cooking_time = sum(self.restaurant.menu[food][1] for food in self.current_order.food)
        self.vehicle = self.current_order.vehicle
        self.delivery_time = self.current_order.delivery_time

        states = ["주문 접수", "요리 중", "배달 출발", "배달 중", "배달 완료"]
        self.update_state(states)
        self.observer.root.mainloop()

# 식당 데이터베이스를 생성
restaurant_db = RestaurantDatabase()

# 식당과 메뉴를 추가.
restaurant_db.add_restaurant(Restaurant("상하이 반점", {"짜장면": (7000, 3),  "탕수육": (15000, 5), "짬뽕": (8000, 3)}, {"도보": 5, "오토바이": 2}))
restaurant_db.add_restaurant(Restaurant("호나준 스시", {"스페셜 특선 초밥(16pcs)": (
    17000, 5),  "오늘의 초밥(12pcs)": (15000, 3), "연어 초밥(12pcs)": (12000, 3)}, {"도보": 5, "오토바이": 2}))

delivery = DeliveryProcess(restaurant_db)   
delivery.order_process()
