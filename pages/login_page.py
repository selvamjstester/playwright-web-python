from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR = "[data-test='error']"

    def load(self, base_url: str):
        self.goto(base_url)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def error_message(self) -> str:
        return self.text(self.ERROR)

    def has_error(self) -> bool:
        return self.is_visible(self.ERROR)
