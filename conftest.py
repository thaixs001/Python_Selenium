import pytest
import json
from utils.browser_setup import get_driver

@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    with open('config/config.json') as config_file:
        config = json.load(config_file)
    driver.get(config["base_url"])
    yield driver
    driver.quit()
