import pytest

from config import Config


@pytest.fixture(scope="session")
def base_url() -> str:
    return Config.BASE_URL


@pytest.fixture(autouse=True)
def _configure_page(page):
    """Apply a sane default timeout to every test's page."""
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    yield


@pytest.fixture
def login_page(page, base_url):
    from pages.login_page import LoginPage

    lp = LoginPage(page)
    lp.load(base_url)
    return lp
