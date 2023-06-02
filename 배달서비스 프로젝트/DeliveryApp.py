import pygame

class DeliveryApp:
    def __init__(self, restaurant_db, current_order):
        self.restaurant_db = restaurant_db
        self.current_order = current_order
        self.prompt = ["식당을 골라주세요", "음식을 선택해주세요", "고객 이름을 입력해주세요", "배달 주소를 입력해주세요", "차량을 선택해주세요", "플라스틱 사용 여부를 입력해주세요(True/False)", "요청 사항을 입력해주세요"]
        self.input_list = [""] * len(self.prompt)  # Initialize the list with empty strings
        self.current_input = 0
        self.font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글을 지원하는 폰트 파일 경로
        
    def get_user_input(self):
        pygame.init()
        self.font = pygame.font.Font(self.font_path, 36)
        self.screen = pygame.display.set_mode((800, 600))
        running = True
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
                            self.input_list = [""] * len(self.prompt)
                            self.current_input = 0
                    elif event.key == pygame.K_BACKSPACE:  # Backspace key
                        self.input_list[self.current_input] = self.input_list[self.current_input][:-1]
                    else:
                        self.input_list[self.current_input] += event.unicode
            # Render the current input string
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            for i in range(len(self.prompt)):
                text = self.font.render(self.prompt[i] + ": " + self.input_list[i], True, (255, 255, 255))
                self.screen.blit(text, (20, 20 + 40 * i))
            pygame.display.flip()
        pygame.quit()