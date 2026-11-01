
import os

import pytest

from screenplay.actor import Actor


@pytest.fixture
def base_url_tienda():
    return os.getenv("BASE_URL", "http://localhost:3000")


@pytest.fixture
def cliente(page):
    return Actor("Cliente QA", page)
