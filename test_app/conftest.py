import pytest
from test_utils.driver import Driver


@pytest.fixture(scope="session")
def _driver():
    driver = Driver("http://localhost:5000")
    yield driver
    driver.exit()
