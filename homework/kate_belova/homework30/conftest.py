from pathlib import Path
from typing import Any, Generator

import pytest
from playwright.sync_api import Page

from homework.kate_belova.homework30.browser_launcher import BrowserLauncher

CONFIG_PATH = Path(__file__).parent / 'config_browser.yaml'


@pytest.fixture()
def browser() -> Generator[Page, Any, None]:
    driver = BrowserLauncher(str(CONFIG_PATH))
    page = driver.create_page()
    yield page
    driver.close()
