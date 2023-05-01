class Button: #버튼팩토리
    def click(self):
        pass
class DarkButton(Button): 
    def click(self):
        print("dark click")
class LightButton(Button):
    def click(self):
        print("light click")
class RedButton(Button):
    def click(self):
        print("red click")
class BlueButton(Button):
    def click(self):
        print("blue click")
        
class CheckBox: #체크박스 팩토리
    def check(self):
        pass
class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")
class LightCheckBox(CheckBox):
    def check(self):
        print("light check")
class RedCheckBox(CheckBox):
    def check(self):
        print("red check")
class BlueCheckBox(CheckBox):
    def check(self):
        print("blue check")
        
class ScrollBar: #스크롤바 팩토리
    def scroll(self):
        pass
class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("dark ScrollBar")
class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light ScrollBar")
class RedScrollBar(ScrollBar):
    def scroll(self):
        print("red ScrollBar")
class BlueScrollBar(ScrollBar):
    def scroll(self):
        print("blue ScrollBar")

class Slider: #슬라이더 팩토리
    def slide(self):
        pass
class DarkSlider(Slider):
    def slide(self):
        print("dark slide")
class LightSlider(Slider):
    def slide(self):
        print("light slide")
class RedSlider(Slider):
    def slide(self):
        print("red slide")
class BlueSlider(Slider):
    def slide(self):
        print("blue slide")   
             
class TextBox: #텍스트박스 팩토리
    def text(self):
        pass
class DarkTextBox(TextBox):
    def text(self):
        print("dark text\n")
class LightTextBox(TextBox):
    def text(self):
        print("light text\n")
class RedTextBox(TextBox):
    def text(self):
        print("red text\n")
class BlueTextBox(TextBox):
    def text(self):
        print("blue text\n")  
        
class UIFactory: #UI팩토리 
    def getButton(self):
        pass
    def getCheck(self):
        pass
    def getScroll(self):
        pass
class DarkFactory(UIFactory):
    def getButton(self):
        return DarkButton()
    def getCheck(self):
        return DarkCheckBox()
    def getScroll(self):
        return DarkScrollBar()
    def getSlider(self):
        return DarkSlider()
    def getTextBox(self):
        return DarkTextBox()
    
class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()
    def getCheck(self):
        return LightCheckBox()
    def getScroll(self):
        return LightScrollBar()
    def getSlider(self):
        return LightSlider()
    def getTextBox(self):
        return LightTextBox()
    
class RedFactory(UIFactory):
    def getButton(self):
        return RedButton()
    def getCheck(self):
        return RedCheckBox()
    def getScroll(self):
        return RedScrollBar()
    def getSlider(self):
        return RedSlider()
    def getTextBox(self):
        return RedTextBox()

class BlueFactory(UIFactory):
    def getButton(self):
        return BlueButton()
    def getCheck(self):
        return BlueCheckBox()
    def getScroll(self):
        return BlueScrollBar()
    def getSlider(self):
        return BlueSlider()
    def getTextBox(self):
        return BlueTextBox()
    
df = DarkFactory()#모드별로 객체 생성
lf = LightFactory()
rf = RedFactory()
bf = BlueFactory()

bt = df.getButton()#다크모드
ck = df.getCheck()
sc = df.getScroll()
sl = df.getSlider()
tb = df.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slide()
tb.text()

bt = lf.getButton()#라이트 모드
ck = lf.getCheck()
sc = lf.getScroll()
sl = lf.getSlider()
tb = lf.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slide()
tb.text()

bt = rf.getButton()#레드 모드
ck = rf.getCheck()
sc = rf.getScroll()
sl = rf.getSlider()
tb = rf.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slide()
tb.text()

bt = bf.getButton()#블루 모드
ck = bf.getCheck()
sc = bf.getScroll()
sl = bf.getSlider()
tb = bf.getTextBox()
bt.click()
ck.check()
sc.scroll()
sl.slide()
tb.text()