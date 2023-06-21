import pygame
import time

class DeliveryUI:
    def __init__(self, vehicle, delivery_time):
        self.screen_width = 800
        self.screen_height = 600
        
        self.deliver_width = 100
        self.deliver_height = 100
        
        self.x = 0
        self.y = self.screen_height // 2 - self.deliver_height // 2
        
        self.vehicle = vehicle
        
        self.bike_image = pygame.image.load("오토바이 아이콘.png")
        self.bike_image = pygame.transform.scale(self.bike_image, (self.deliver_width, self.deliver_height))
        
        self.walking_image = pygame.image.load("도보 아이콘.png")
        self.walking_image = pygame.transform.scale(self.walking_image, (self.deliver_width, self.deliver_height))
        
        self.bicycle_image = pygame.image.load("자전거 아이콘.png")
        self.bicycle_image = pygame.transform.scale(self.bicycle_image, (self.deliver_width, self.deliver_height)) 

        self.delivery_time = delivery_time
        self.deliver_speed = self.screen_width / (self.deliver_width * self.delivery_time)
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.start_time = None
        self.font = pygame.font.Font(None, 30)  # 폰트 설정        
        
    
    def update_deliver_position(self):
        self.x += self.deliver_speed

    def draw_walking(self):
        self.screen.blit(self.walking_image, (self.x, self.y))
        
    def draw_bike(self):
        self.screen.blit(self.bike_image, (self.x, self.y))
        
    def draw_bicylce(self):
        self.screen.blit(self.bicycle_image, (self.x, self.y))
        
    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.update_deliver_position()

            self.screen.fill((255, 255, 255))
            if self.vehicle == "도보":
                self.draw_walking()
            elif self.vehicle == "오토바이":
                self.draw_bike()
            elif self.vehicle == "자전거":
                self.draw_bicylce()
            pygame.display.update()
            
            if self.x + self.deliver_width >= self.screen_width:
                break

            self.clock.tick(60) 