import pytest
from cyhy.db import database as pcsdb
from cyhy.db import CHDatabase


@pytest.fixture
def database():
    return pcsdb.db_from_config("testing")


@pytest.fixture
def ch_db(database):
    return CHDatabase(database)
