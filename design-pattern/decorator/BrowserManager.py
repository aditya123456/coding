


class BrowserManager:

    def __init__(self, browser):
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Invalid browser"+ browser)

    def start_browser(self):
        self.driver.get("https://www.google.com")
        return self.driver

    def quit_browser(self):
        self.driver.quit()


class loggingDecorator:

    def __init__(self, browser):
        self.browserManager = browser

    def start_browser(self):
        print("starting browser")
        self.driver.get("https://www.google.com")
        print("started browser")
        return self.driver

    def quit_browser(self):
        print("stoping browser")
        self.driver.quit()

