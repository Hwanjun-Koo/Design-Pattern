import time
import copy
import tkinter as tk
from DeliveryUI import DeliveryUI

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
            
    def start_ui(self, delivery_time):
        ui = DeliveryUI(delivery_time)
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
            print("식당 목록 불러오는중..")
            time.sleep(1)
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
        
    def create(self) -> OrderForm:
        print("다음 중 식당을 선택해 주세요.")
        time.sleep(0.5)
        restaurant_names = [restaurant.name for restaurant in self.restaurant_db.get_all()]
        for i, restaurant_name in enumerate(restaurant_names, start=1):
            print(f"{i}. {restaurant_name}")
        chosen_restaurant = self.restaurant_db.get_restaurant(restaurant_names[int(input()) - 1])
        
        print("다음 중 음식을 선택해 주세요")
        time.sleep(0.5)
        for i, (food, _) in enumerate(chosen_restaurant.menu.items(), start=1):
            print(f"{i}. {food}")
        food_choices = input("메뉴 앞 번호를 입력해 주세요(복수 선택 가능, 공백으로 구분해주세요): ").split(" ")
        food_list= []
        for choice in food_choices:
            food_index = int(choice.strip()) - 1
            chosen_food = list(chosen_restaurant.menu.keys())[food_index]
            food_list.append(chosen_food)
      
        print(food_list)
        
        self.order.food = food_list
        self.order.customer = input("주문자 이름: ")
        self.order.address = input("배달할 주소: ")
        print("배달 방법: ")
        for i, (vehicle, _) in enumerate(chosen_restaurant.vehicles.items(), start=1):
            print(f"{i}. {vehicle}")
        vehicle_choice = int(input()) - 1
        chosen_vehicle = list(chosen_restaurant.vehicles.keys())[vehicle_choice]
        self.order.delivery_time = chosen_restaurant.vehicles[chosen_vehicle]
        
        self.order.plastic = bool(input("일회용품 사용하시나요? (예: y키 입력 후 Enter키, 아니오: Enter키) "))
        self.order.request = input("추가 요청 사항: ")
        self.order.total_price = sum(chosen_restaurant.menu[food][0] for food in food_list)
        self.order.restaurant_name = chosen_restaurant.name
        self.order.vehicle = chosen_vehicle
        return self.order.clone(), chosen_restaurant
#주문 상태를 자동으로 업데이트 시켜주는 프로세스를 Facade 패턴으로 구현    
class DeliveryProcess:
    def __init__(self, restaurant_db):
        self.observer = DeliveryObserver()
        self.proto_order = OrderPrototype(restaurant_db)
        self.current_order, self.restaurant = self.proto_order.create()
        self.restaurant.register(self.observer)
        self.cooking_time = sum(self.restaurant.menu[food][1] for food in self.current_order.food)
        self.delivery_time = self.current_order.delivery_time
        
    def update_state(self, states):
        if states:
            self.restaurant.setState(states[0])
            if states[0] == "요리 중":
                self.observer.root.after(self.cooking_time * 1000, self.update_state, states[1:])
            elif states[0] == "배달 중":
                self.observer.start_ui(self.delivery_time)
                self.update_state(states[1:])
            elif states[0] == "배달 완료":
                receipt_text = self.current_order.receipt()
                self.observer.show_receipt(receipt_text)
            else:
                self.observer.root.after(1000, self.update_state, states[1:])

    def order_process(self):
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
