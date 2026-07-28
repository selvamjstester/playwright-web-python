import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central test configuration, overridable via environment variables."""

    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
    PASSWORD = os.getenv("PASSWORD", "secret_sauce")
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
