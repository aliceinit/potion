from flask import Flask
import pytest

app = Flask(__name__)


@pytest.fixture
def app():
    return Flask(__name__)
