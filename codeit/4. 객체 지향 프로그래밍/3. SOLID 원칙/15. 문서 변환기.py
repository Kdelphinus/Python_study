from abc import ABC, abstractclassmethod


class Exporter(ABC):
    @abstractclassmethod
    def export(self, new_name: str, document):
        pass


class Document:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def content(self):
        """문서의 내용을 리턴한다"""
        return self._content

    def __str__(self):
        """문서의 정보를 문자열로 리턴한다"""
        return "문서 이름: {}\n문서 내용:\n{}".format(self._name, self._content)


class CSVExporter(Exporter):
    """문서를 csv 형식으로 변환하는 클래스"""

    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nCSV 파일로 변환 중~")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document


class HTMLExporter(Exporter):
    """문서를 HTML 형식으로 변환하는 클래스"""

    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nHTML 문서 변환 중~")

        new_content = """
<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
{}
</body>

</html>
        """.format(
            document.content
        )
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document


class ExportController:
    """문서를 특정 파일 형식으로 변환하는 클래스"""

    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter):
        """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter == None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)


# 변환기 컨트롤러 인스턴스 정의
export_handler = ExportController()

# csv 변환기 인스턴스, html 변환기 인스턴스 정의
csv_exporter = CSVExporter()
html_exporter = HTMLExporter()

# 변환할 문서 인스턴스 정의
document = Document(
    "직원정보.txt",
    """
이름|이메일
강영훈|younghoon@codeit.kr
이윤수|yoonsoo@codeit.kr
손동욱|dongwook@codeit.kr""",
)

# 기존 문서 출력
print(document)

# 변환기를 csv 변환기로 설정
export_handler.set_exporter(csv_exporter)

# 주어진 문서를 csv 문서로 변환
exported_document = export_handler.run_export("직원정보.csv", document)
# 변환된 문서 출력
print(exported_document)

export_handler.set_exporter(html_exporter)
exported_document = export_handler.run_export("직원정보.html", document)
print(exported_document)

print(CSVExporter.mro())
print(HTMLExporter.mro())