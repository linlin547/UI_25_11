from appium import webdriver


class Driver:
    # app的driver
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明手机driver"""
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = 'com.android.settings'
            desired_caps['appActivity'] = '.Settings'
            # 对手机驱动对象赋值
            cls.__app_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            return cls.__app_driver
        else:
            # driver可以继续使用
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出手机driver"""
        if cls.__app_driver:
            # 手机驱动有值
            # 退出
            cls.__app_driver.quit()
            # 置为None
            cls.__app_driver = None
