from pathlib import Path

import pytest
from faker import Faker

from browser_launcher import BrowserLauncher

CONFIG_PATH = Path(__file__).parent / 'config_browser.yaml'


@pytest.fixture()
def browser():
    driver = BrowserLauncher(str(CONFIG_PATH))
    page = driver.create_page()
    yield page
    driver.close()


random_generator = Faker()
