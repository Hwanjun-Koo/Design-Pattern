import time
import copy
import tkinter as tk
import math
from DeliveryUI import DeliveryUI

# 배달 상태를 관찰하고 알림을 보내는 옵저버 생성
class Observer:
    def update(self):
        pass

    def start_ui(self):
        pass


class DeliveryObserver(Observer):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.text = tk.Text(self.root, font=("Malgun", 12))
        self.text.pack()
        self.root.withdraw()  # 창 숨기기

    def clear_text_and_close_window(self):
        self.text.delete(1.0, tk.END)
        self.root.withdraw()

    def show_message(self, message):
        self.root.deiconify()  # 창 띄우기
        self.text.delete(1.0, tk.END)
        self.text.tag_configure("center", justify="center")
        self.text.insert(tk.END, message, "center")

    def show_receipt(self, receipt_text):
        self.root.deiconify()
        self.text.delete(1.0, tk.END)
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

    def start_ui(self, vehicle, delivery_time):
        ui = DeliveryUI(vehicle, delivery_time)
        ui.start()
        
# 옵저버가 관찰할 식당
class Restaurant:
    def __init__(self, name, menu, vehicles, location):
        self.observers = []
        self.state = None
        self.name = name
        self.menu = menu
        self.vehicles = vehicles
        self.location = location

    def register(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.state)

    def setState(self, state):
        self.state = state
        self.notify()

# 식당들을 저장할 데이터베이스를 Singleton 패턴으로 구축
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

# 주문서 작성 양식과 배달 완료 시 표시할 영수증을 Prototype 패턴으로 작성
class OrderForm:
    def __init__(self, food: str, customer: str, address: str, vehicle: str, plastic: bool, request: str, restaurant_name: str):
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
        restaurant_names = [
            restaurant.name for restaurant in self.restaurant_db.get_all()]
        for i, restaurant_name in enumerate(restaurant_names, start=1):
            print(f"{i}. {restaurant_name}")
        chosen_restaurant = self.restaurant_db.get_restaurant(
            restaurant_names[int(input()) - 1])
        print("선택한 식당: " + chosen_restaurant.name)
        time.sleep(0.5)

        print("다음 중 음식을 선택해 주세요")
        time.sleep(0.5)
        for i, (food, _) in enumerate(chosen_restaurant.menu.items(), start=1):
            print(f"{i}. {food}")
        food_choices = input(
            "메뉴 번호를 입력해 주세요(복수 선택 가능, 공백으로 구분해주세요): ").split(" ")
        food_list = []
        for choice in food_choices:
            food_index = int(choice.strip()) - 1
            chosen_food = list(chosen_restaurant.menu.keys())[food_index]
            food_list.append(chosen_food)
        print("<선택한 메뉴>")
        print(food_list)

        self.order.food = food_list
        self.order.customer = input("주문자 이름: ")

        coordinates = input("배달할 주소(0 ~ 99 인 좌표 형태 예시 - 30,20): ")
        latitude, longitude = coordinates.split(",")
        self.order.address = (int(latitude), int(longitude))

        print("배달 방법: ")
        for i, vehicle in enumerate(chosen_restaurant.vehicles, start=1):
            print(f"{i}. {vehicle}")
        vehicle_choice = int(input()) - 1
        chosen_vehicle = chosen_restaurant.vehicles[vehicle_choice]

        self.order.plastic = bool(
            input("일회용품 사용하시나요? (예: 아무 키 입력 후 Enter키, 아니오: Enter키) "))
        self.order.request = input("추가 요청 사항: ")
        self.order.total_price = sum(
            chosen_restaurant.menu[food][0] for food in food_list)
        self.order.restaurant_name = chosen_restaurant.name
        self.order.vehicle = chosen_vehicle
        return self.order.clone(), chosen_restaurant

class DeliveryTimeCalculator:
    def __init__(self):
        self.delivery_time_factors = {
            "도보": 0.4,  # 거리에 특정 실수를 곱한 값으로 배달 시간을 산출
            "자전거": 0.2,
            "오토바이": 0.1
        }

    def calculate_delivery_time(self, distance, vehicle):
        if vehicle in self.delivery_time_factors:
            factor = self.delivery_time_factors[vehicle]
            delivery_time = distance * factor
            return delivery_time
        else:
            return 0

# 주문 상태를 자동으로 업데이트 시켜주는 Facade 패턴
class DeliveryProcess:
    def __init__(self, restaurant_db):
        self.observer = DeliveryObserver()
        self.proto_order = OrderPrototype(restaurant_db)
        self.current_order, self.restaurant = self.proto_order.create()
        self.restaurant.register(self.observer)
        self.cooking_time = sum(
            self.restaurant.menu[food][1] for food in self.current_order.food)
        self.delivery_time_calculator = DeliveryTimeCalculator()

    def calculate_distance(self, order_coordinates, restaurant_coordinates):
        # 좌표 간 거리 계산을 직접 처리
        lat1, lon1 = order_coordinates
        lat2, lon2 = restaurant_coordinates
        distance = math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)
        return distance

    def update_state(self, states):
        if states:
            self.restaurant.setState(states[0])
            if states[0] == "요리 중":
                self.observer.root.after(
                    self.cooking_time * 1000, self.update_state, states[1:])
            elif states[0] == "배달 중":
                order_location = self.current_order.address
                restaurant_location = self.restaurant.location
                distance = self.calculate_distance(
                    order_location, restaurant_location)
                self.vehicle = self.current_order.vehicle
                self.delivery_time = self.delivery_time_calculator.calculate_delivery_time(
                    distance, self.vehicle)
                self.observer.start_ui(self.vehicle, self.delivery_time)
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

restaurant_db = RestaurantDatabase()# 식당 데이터베이스를 생성
restaurant_db.add_restaurant(Restaurant("탕수육 참 잘하는 집", {"짜장면": (7000, 3), "탕수육": (
    15000, 5), "짬뽕": (8000, 3), "가성비 혼밥세트(짜장 + 탕수육)": (20000, 6)}, ["도보", "자전거", "오토바이"], (20, 10)))
restaurant_db.add_restaurant(Restaurant("파파스시", {"스페셜 특선 초밥(16pcs)": (
    17000, 5), "오늘의 초밥(12pcs)": (15000, 3), "연어 초밥(12pcs)": (12000, 3)}, ["도보", "자전거", "오토바이"], (40, 50)))
restaurant_db.add_restaurant(Restaurant("교촌피자", {"허니피자": (17000, 5), "레드피자": (17000, 5), "허니&레드 반반 피자": (23000, 6)}, ["도보", "자전거", "오토바이"], (30, 20)))
restaurant_db.add_restaurant(Restaurant("홍콩치킨", {"마라치킨": (20000, 3), "주윤발치킨": (23000, 4), "에크타르트 2개": (5000, 2)}, ["도보","자전거", "오토바이"], (10, 50)))



delivery = DeliveryProcess(restaurant_db)
delivery.order_process()
