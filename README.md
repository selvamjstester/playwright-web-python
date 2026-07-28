# playwright-web-python

[![CI](https://github.com/selvamjstester/playwright-web-python/actions/workflows/ci.yml/badge.svg)](https://github.com/selvamjstester/playwright-web-python/actions/workflows/ci.yml)

End-to-end **web UI automation** framework built with **Playwright** + **pytest**, using the **Page Object Model (POM)**. Tests run against the public [SauceDemo](https://www.saucedemo.com) demo store.

## Highlights

- 🧭 **Page Object Model** — clean separation of locators/actions (`pages/`) from tests (`tests/`)
- ✅ **pytest** with markers (`smoke`, `regression`, `login`, `checkout`)
- 📊 **HTML report** (`pytest-html`) + **Allure** results
- ⚙️ **Config via environment variables** (`.env` supported)
- 🤖 **GitHub Actions CI** — installs browsers and runs the suite on every push

## Project structure

```
playwright-web-python/
├── config.py              # env-driven configuration
├── conftest.py            # pytest fixtures (page, login_page)
├── pages/                 # Page Objects
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── test_login.py
│   └── test_checkout.py
├── pytest.ini
└── requirements.txt
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Running tests

```bash
# all tests (headless Chromium)
pytest --browser chromium

# only smoke tests
pytest -m smoke

# headed / debug
pytest --headed --browser chromium

# generate & open Allure report (requires the allure CLI)
allure serve allure-results
```

## Configuration

| Variable          | Default                      | Description            |
|-------------------|------------------------------|------------------------|
| `BASE_URL`        | `https://www.saucedemo.com`  | Application under test |
| `STANDARD_USER`   | `standard_user`              | Valid login user       |
| `LOCKED_USER`     | `locked_out_user`            | Locked-out user        |
| `PASSWORD`        | `secret_sauce`               | Login password         |
| `DEFAULT_TIMEOUT` | `10000`                      | Per-action timeout (ms)|

---
Part of my SDET portfolio. Built to demonstrate resilient, maintainable UI test automation.
