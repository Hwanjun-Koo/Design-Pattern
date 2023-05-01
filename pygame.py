import pygame
import MyVector as mv #vector 클래스

rgb = { #Dicitonary 형태
    'BLACK':(0, 0, 0),
    'WHITE':(255, 255, 255),
    'BLUE':(0, 0, 255),
    'GREEN':(0, 255, 0),
    'RED':(255, 0, 0),
    'YELLOW':(255, 255, 0)
}
#Implementor
class Actor: #모든 등장인물

    def __init__(self, x, y):
        self.pos = mv.MyVector(x, y) #인물의 위치 (2차원)
        self.name = ""
        self.skill = ""
    def setPos(self, x, y): #위치 업데이트
        self.pos.x = x
        self.pos.y = y
    def move(self, delta):
        self.pos = self.pos + delta #delta = 변화량
    def setName(self, name): #등장인물의 이름 설정
        self.name = name
    def setSkill(self, skill): #스킬을 직접 만들도록
        pass 
    def setQuest(self, quest): #퀘스트 지정
        pass

#Concrete Implementor 1
class Hero(Actor):  #Hero를 생성

    def setSkill(self, skill): #스킬 지정
        self.skill = skill
        
#Concrete Implementor 2
class Enemy(Actor): #Enemy 생성

    def setSkill(self, skill): 
        self.skill = skill
        
#Concrete Implementor 3(My own)
class NPC(Actor): 
    def __init__(self, x, y):
        super().__init__(x, y)
        self.start_pos = mv.MyVector(x, y)
        self.quest = ""

    
    def setQuest(self, quest):
        self.quest = quest
        
    def move(self, delta):
        if delta != mv.MyVector(0, 0):
            self.pos = self.pos + delta #delta = 변화량


#Abstraction
class GameFramework:

    def __init__(self):
        self.pygame = pygame #pygame 객체 생성
        self.screen = 0

        self.nY = 0 
        self.nX = 0

        self.hero = 0 #기능을 실제로 수행하는 위임자 존재 pass와 유사

        print("init")

    def setDisplay(self, nX, nY): 
        self.nY = nY
        self.nX = nX
        self.screen = self.pygame.display.set_mode([self.nX, self.nY]) #게임창 크기 지정
        self.pygame.display.set_caption("Prince") #게임창의 이름


    def setHero(self, hero:Actor): #Actor 클래스로부터 위임받음
        self.hero = hero

    def ready(self):
        self.pygame.init() #pygame 초기화

    def drawPolygon(self, color, points, thickness): #다각형 표현기능
        self.pygame.draw.polygon(self.screen, color, points, thickness)

    def drawEdges(self):
        p1 = mv.MyVector(0, 0)
        p2 = mv.MyVector(0, 10)
        p3 = mv.MyVector(10, 0)
        
        self.drawPolygon(rgb["WHITE"], [p1.vec(), p2.vec(), p3.vec()], 1) #MyVector 클래스의 vec함수를 이용하여 삼각형 모양 생성

    def printText(self, msg, color, pos):
        font= self.pygame.font.SysFont("consolas",20) #글씨체와 글씨 크기 설정
        textSurface     = font.render(msg,True, color, None) #self.pygame.Color(color)#입력받은 글씨 색깔로 설정
        textRect        = textSurface.get_rect() #텍스트를 직사각형의 컨테이너에 담아 위치를 지정해줌
        textRect.topleft= pos #텍스트의 위치를 좌상단으로 설정
        self.screen.blit(textSurface, textRect) #blit함수로 텍스트를 스크린에 그려냄

    #게임 실행
    def launch(self):
        pass


#Refined Abstraction 1
class WhiteGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(60) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: #alt + f4
                    print("종료")
                    done = True

                elif event.type == self.pygame.KEYDOWN: #키를 눌렀을때
                    print("key down")
                    if event.key == self.pygame.K_LEFT: #어떤키가 눌렸는가?
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP: #컴퓨터에선 y좌표계가 현실과 반대라서 위로 갈 떄가 음수이다.
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP: #키를 눌렀다가 뗄 때
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:
                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["WHITE"])
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec())
                if isinstance(self.hero, NPC):
                    self.printText(self.hero.quest, rgb["BLUE"], (self.hero.pos + mv.MyVector(0, 15)).vec())
                     # NPC 객체는 이동하지 않음
                else:
                    self.hero.move(delta)#주인공의 위치가 업데이트 됨
                    self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())
                 
            self.pygame.display.flip() #버퍼를 지워줌 이게 있어야 입력이 계속 반영됨

        self.pygame.quit()


#Refined Abstraction 2
class BlackGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(30) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["BLACK"])
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec())
                if isinstance(self.hero, NPC):
                    self.printText(self.hero.quest, rgb["BLUE"], (self.hero.pos + mv.MyVector(0, 15)).vec())
                     # NPC 객체는 이동하지 않음
                else:
                    self.hero.move(delta)#주인공의 위치가 업데이트 됨
                    self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()
        
#Refined Abstraction 3
class YellowGame(GameFramework):

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()
  
        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(30) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

               print("pressed", self.hero.pos.getState()) #in console
               self.screen.fill(rgb["YELLOW"])
               self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec())
               if isinstance(self.hero, NPC):
                   self.printText(self.hero.quest, rgb["BLUE"], (self.hero.pos + mv.MyVector(0, 15)).vec())
                    # NPC 객체는 이동하지 않음
               else:
                   self.hero.move(delta)#주인공의 위치가 업데이트 됨
                   self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()



game = YellowGame() 
game.ready()
game.setDisplay(800, 500)
game.drawEdges()

hero = Hero(0, 0)
hero.setName("Hwanjun Koo")
hero.setSkill("201900435")

game.setHero(hero)

game.launch()






