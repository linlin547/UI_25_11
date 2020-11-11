import allure, pytest
from selenium import webdriver


class Test001:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")

    @allure.step("测试方法1")
    def test_001(self):
        print("\ntest_001")

        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        self.driver.quit()

    @pytest.mark.dependency(name="a")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("测试方法1")
    def test_002(self):
        print(111)
        assert False

    @pytest.mark.dependency(depends=["a"])
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("测试方法1")
    def test_003(self):
        print(111)
