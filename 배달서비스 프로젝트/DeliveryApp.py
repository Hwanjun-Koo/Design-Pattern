import pygame
import time
from DeliveryService import Restaurant, RestaurantDatabase, OrderPrototype, DeliveryProcess

# Pygame 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Pygame 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 주문 화면을 구현할 DeliveryApplication 클래스
class DeliveryApplication:
    def __init__(self):
        self.restaurant_db = RestaurantDatabase()
        self.order_proto = OrderPrototype(self.restaurant_db)
        self.current_order = None
        self.selected_restaurant = None
        self.selected_food = []
        self.selected_vehicle = None
        self.delivery_time = None
        self.screen = None
        self.clock = None
        self.font = None

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)

    def draw_text(self, text, x, y, color=BLACK):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def draw_menu(self):
        self.screen.fill(WHITE)
        self.draw_text("다음 중 식당을 선택해 주세요.", 10, 10)
        
        restaurant_names = [restaurant.name for restaurant in self.restaurant_db.get_all()]
        for i, restaurant_name in enumerate(restaurant_names, start=1):
            self.draw_text(f"{i}. {restaurant_name}", 10, 40 + i * 30)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.selected_restaurant = self.restaurant_db.get_restaurant(restaurant_names[0])
                self.draw_food_menu()
            elif event.key == pygame.K_2:
                self.selected_restaurant = self.restaurant_db.get_restaurant(restaurant_names[1])
                self.draw_food_menu()
            elif event.key == pygame.K_RETURN:
                self.place_order()
        
    def draw_food_menu(self):
        self.screen.fill(WHITE)
        self.draw_text("다음 중 음식을 선택해 주세요.", 10, 10)
        
        self.selected_food = []
        food_list = list(self.selected_restaurant.menu.keys())
        for i, food in enumerate(food_list, start=1):
            self.draw_text(f"{i}. {food}", 10, 40 + i * 30)
        
    def draw_vehicle_menu(self):
        self.screen.fill(WHITE)
        self.draw_text("배달 방법을 선택해 주세요.", 10, 10)
        
        self.selected_vehicle = None
        vehicle_list = list(self.selected_restaurant.vehicles.keys())
        for i, vehicle in enumerate(vehicle_list, start=1):
            self.draw_text(f"{i}. {vehicle}", 10, 40 + i * 30)
        
    def place_order(self):
        self.current_order, self.selected_restaurant = self.order_proto.create()
        self.current_order.food = self.selected_food
        self.current_order.vehicle = self.selected_vehicle
        
        self.delivery_time = self.selected_restaurant.vehicles[self.selected_vehicle]
        
        self.delivery = DeliveryProcess(self.restaurant_db)
        self.delivery.current_order = self.current_order
        self.delivery.restaurant = self.selected_restaurant
        self.delivery.delivery_time = self.delivery_time
        
        pygame.quit()
        self.delivery.order_process()

    def start(self):
        self.initialize()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)
                    
            pygame.display.update()
            self.clock.tick(60) 

# 주문 화면 실행
app = DeliveryApplication()
app.start()