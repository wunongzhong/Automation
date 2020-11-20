import os
import pytest

if __name__ == '__main__':
    pytest.main(["-s","./frameworkddt/common_pytest.py","--alluredir", "./report/xml"])
    os.system("allure generate --clean ./report/xml/ -o ./result/html/")