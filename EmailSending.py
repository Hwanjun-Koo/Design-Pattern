import copy

class Email:
    def __init__(self, sender:str, recipient:str, subject:str, body:str):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self):
        print("From: " + self.sender)
        print("To: " + self.recipient)
        print("Subject: " + self.subject)
        print("Body: " + self.body)
        print("Your email has been sent.")
    def clone(self):
        return copy.deepcopy(self)

class EmailPrototype:
    def __init__(self):
        self.email = Email("", "", "", "")

    def create(self, sender:str, recipient:str, subject:str, body:str) -> Email:
        self.email.sender = sender
        self.email.recipient = recipient
        self.email.subject = subject
        self.email.body = body
        return self.email.clone()

# 메일 프로토타입 생성
prototype = EmailPrototype()
default_email = prototype.create("", "", "", "")

# 프로토타입을 활용해 이메일 작성하기
email1 = default_email.clone()
email1.recipient = "friend@naver.com"
email1.subject = "야 이거 봐봐 쩐다"
email1.body = "이 편지는 영국에서 최초로 시작하여 ..."

email2 = default_email.clone()
email2.recipient = "professor@gmail.com"
email2.subject = "설계패턴 과목 증원관련 문의드립니다."
email2.body = "안녕하세요 저는 컴퓨터전자시스템공학부 OOO입니다 ..."

# 이메일 보내기
email1.send()
email2.send()
