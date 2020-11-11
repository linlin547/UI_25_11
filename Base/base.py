from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver


class Base:

    def __init__(self):
        # 声明driver
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组(定位类型,属性值) demo:(By.ID,"id属性值")
        :param timeout: 超时时间
        :param poll: 搜素间隔
        :return:定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc[0], loc[1]))

    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: 元组(定位类型,属性值) demo:(By.ID,"id属性值")
        :param timeout: 超时时间
        :param poll: 搜素间隔
        :return:定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(loc[0], loc[1]))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击元素
        :param loc: 元组(定位类型,属性值) demo:(By.ID,"id属性值")
        :param timeout: 超时时间
        :param poll: 搜素间隔
        :return:
        """
        self.search_ele(loc, timeout, poll).click()

    def input_text(self, loc, text, timeout=5, poll=1.0):
        """
        输入框输入内容
        :param loc: 元组(定位类型,属性值) demo:(By.ID,"id属性值")
        :param text: 输入值
        :param timeout: 超时时间
        :param poll: 搜素间隔
        :return:
        """
        # 定位
        ele = self.search_ele(loc, timeout, poll)
        # 清空输入框
        ele.clear()
        # 输入操作
        ele.send_keys(text)
