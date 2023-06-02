import pygame

class DeliveryApp:
    def __init__(self, restaurant_db, current_order):
        self.restaurant_db = restaurant_db
        self.current_order = current_order
        restaurant_list = " / ".join(f"{i+1}. {restaurant.name}" for i, restaurant in enumerate(self.restaurant_db.get_all()))
        self.prompt = [
    *restaurant_list.splitlines(),
    "식당을 골라주세요: ",
    "음식을 선택해주세요: ",
    "고객 이름을 입력해주세요: ",
    "배달 주소를 입력해주세요: ",
    "차량을 선택해주세요: ",
    "플라스틱 사용 여부를 입력해주세요(True/False): ",
    "요청 사항을 입력해주세요: "
]
        self.input_list = [""] * len(self.prompt)
        self.current_input = 0
        self.font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글을 지원하는 폰트 파일 경로
        
    def get_user_input(self):
        pygame.init()
        self.font = pygame.font.Font(self.font_path, 36)
        self.screen = pygame.display.set_mode((800, 600))
        running = True
        cursor_visible = True
        cursor_timer = pygame.time.get_ticks()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter key
                        if self.current_input < len(self.prompt) - 1:
                            self.current_input += 1
                        else:
                            self.current_order = self.restaurant_db.create(*self.input_list)
                            self.current_input = 0
                    elif event.key == pygame.K_BACKSPACE:  # Backspace key
                        self.input_list[self.current_input] = self.input_list[self.current_input][:-1]
                    else:
                        self.input_list[self.current_input] += event.unicode
            # Render the current input string
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            for i in range(len(self.prompt)):
                if i == self.current_input:
                    if i == 0:
                        text = self.font.render(self.prompt[i], True, (255, 255, 255))
                    else:
                        text = self.font.render(self.prompt[i] + self.input_list[i-1], True, (255, 255, 255))

                else:
                    text = self.font.render(self.prompt[i] + self.input_list[i-1], True, (255, 255, 255))
                self.screen.blit(text, (20, 50 + 50 * i))
            if cursor_visible and self.current_input < len(self.prompt):
                cursor_y = 50 + 50 * (self.current_input + 1)  # 커서가 "식당을 골라주세요" 문장 다음에 위치하도록 조정
                cursor_x = 20 + self.font.size(self.prompt[self.current_input + 1])[0] + self.font.size(self.input_list[self.current_input])[0]  # 커서의 x 좌표
                cx, cy = cursor_x, cursor_y
                pygame.draw.line(self.screen, (255, 255, 255), (cx, cy), (cx, cy + self.font.get_height()), 2)
                
            if pygame.time.get_ticks() - cursor_timer > 500:
                cursor_timer = pygame.time.get_ticks()
                cursor_visible = not cursor_visible
            pygame.display.flip()
        pygame.quit()