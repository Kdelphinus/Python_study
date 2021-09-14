class AppleKeyboard:
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def set_keyboard_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_keyboard_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_keyboard_input()


class SamsungKeyboard:
    """삼성 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.user_input = ""

    def save_user_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input

    def give_user_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input


# AppleKeyboard
keyboard_manager = KeyboardManager()
apple_keyboard = AppleKeyboard()
keyboard_manager.connect_to_keyboard(apple_keyboard)
apple_keyboard.set_keyboard_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())

# SamsungKeyboard
keyboard_manager = KeyboardManager()
samsung_keyboard = SamsungKeyboard()
keyboard_manager.connect_to_keyboard(samsung_keyboard)
samsung_keyboard.save_user_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())
# error, send_keyboard_input()이 삼성키보드에 없기 때문


# 이는 새로운 키보드가 추가될 때, 클래스를 계속 바꾸어주어야 하므로 개방 폐쇄 원칙을 지키지 않음