from abc import ABC, abstractmethod


class WebDriverInterFace(ABC):

    @abstractmethod
    def get_driver(self):
        pass

class ChromeDriver(WebDriverInterFace):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

class FireFoxDriver(WebDriverInterFace):

    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

class BrowserContext:

    def __init__(self, strategy):
        self._strategy = strategy

    def get_driver(self):
        return self._strategy.get_driver()

browser_context = BrowserContext(ChromeDriver())
