import pygame
import time

class DeliveryUI:
    def __init__(self, chosen_vehicle, delivery_time):
        self.screen_width = 800
        self.screen_height = 600
        
        self.deliver_width = 80
        self.deliver_height = 80
        
        self.x = 0
        self.y = self.screen_height // 2 - self.deliver_height // 2
        self.chosen_vehicle = chosen_vehicle
        
        self.bike_image = pygame.image.load(r"C:\Users\kooju\OneDrive\바탕 화면\잡동사니\오토바이 아이콘.png")
        self.bike_image = pygame.transform.scale(self.bike_image, (self.deliver_width, self.deliver_height))
        
        self.walk_image = pygame.image.load(r"C:\Users\kooju\OneDrive\바탕 화면\잡동사니\도보 아이콘.png")
        self.walk_image = pygame.transform.scale(self.walk_image, (self.deliver_width, self.deliver_height))
        
        self.delivery_time = delivery_time
        self.deliver_speed = self.screen_width / (self.deliver_width * self.delivery_time)
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.start_time = None     
        
    
    def update_deliver_position(self):
        self.x += self.deliver_speed
        
    def draw_walk(self):
        self.screen.blit(self.walk_image, (self.x, self.y))

    def draw_bike(self):
        self.screen.blit(self.bike_image, (self.x, self.y))
        
    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.update_deliver_position()
            self.screen.fill((255, 255, 255))
            
            if self.chosen_vehicle == "오토바이":
                self.draw_bike()
            elif self.chosen_vehicle == "도보":
                self.draw_walk()
                
            pygame.display.update()
            
            if self.x + self.deliver_width >= self.screen_width:
                break

            self.clock.tick(60) 