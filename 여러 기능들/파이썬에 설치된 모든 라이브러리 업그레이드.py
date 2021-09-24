"""pip으로 설치된 라이브러리 버전 확인(터미널에 직접 입력)
-> pip freeze"""


# 출처: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=qbxlvnf11&logNo=221450772712
import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(
    ["%s==%s" % (package.key, package.version) for package in installed_packages]
)
print(installed_packages_list)

import pip
from subprocess import call

for package in installed_packages_list:
    print("pip install --upgrade " + package[: package.find("==")])
    call("pip install --upgrade " + package[: package.find("==")], shell=True)
