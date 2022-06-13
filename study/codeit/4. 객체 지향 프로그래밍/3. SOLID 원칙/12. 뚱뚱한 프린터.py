from abc import ABC, abstractmethod


class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file: str) -> bool:
        """문서 출력 메소드"""
        pass


class IScanner(ABC):
    @abstractmethod
    def scan(self, content: str) -> bool:
        """문서 스캔 메소드"""
        pass


class SamsungPrinter(IPrinter, IScanner):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False


class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False

    # def scan(self, content):
    #     """LG 프린터는 스캔 기능이 없기 때문에 False 리턴"""
    #     print("이 프린터는 문서를 스캔하는 기능이 없습니다.")
    #     return False


samsung_printer = SamsungPrinter(True, True, True)
lg_printer = LGPrinter(True, True, True)

samsung_printer.print_file("4월 보고서.docx")
lg_printer.print_file("4월 보고서.docx")

samsung_printer.scan("스캔 테스트 문서")
# lg_printer.scan("스캔 테스트 문서")

print(SamsungPrinter.mro())
print(LGPrinter.mro())
