import pytest
import fantasy


fantasy.USERS = {}
user1 = fantasy.User(1, "pepe", "1234")
user2 = fantasy.User(1, "pepe", "1234")


def test_user_building():
    assert user1.username == "pepe"
    assert user1.id == 1
    assert user1.budget == 50_000_000
    assert user1.log_status == False


def test_corrected_id():
    assert user2.id == 2


def test_login():
    user1.login("1234")
    assert user1.log_status == True


def test_logout():
    user1.logout()
    assert user1.log_status == False


def test_login_wrong_answer():
    user2.login("0")
    assert user2.log_status == False


def test_buying_driver():
    user1.login("1234")
    user1.buy_driver("Fernando Alonso")
    user1.buy_driver("Lance Stroll")
    assert user1.team["drivers"] == ["Fernando Alonso", "Lance Stroll"]


def test_excepcion_login():
    user1.logout()
    with pytest.raises(fantasy.LoginError) as err:
        user1.buy_driver("Lance Stroll")
    assert str(err.value) == f"The user is not logged"


def check_not_enough_budget():
    user1.budget = 0
    user1.login("1234")
    check = user1.buy("Fernando Alonso")
    user1.budget = 50_000_000
    assert check == f"Not enough budget to buy the driver"


def driver_existence():
    check = user1.buy_driver("Leo Messi")
    assert check == f"Driver Leo Messi is not racing in F1"
