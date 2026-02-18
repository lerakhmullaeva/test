import os
from pathlib import Path

import pytest
import requests


# Можеш змінити через env, але дефолт як у твоєму auto.py
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8080")

# Креденшали як у auto.py (можна теж перекинути через env)
USERNAME = os.getenv("API_USER", "test_user")
PASSWORD = os.getenv("API_PASS", "test_pass")

# Вимога: логінг у файл test_search_log.txt
LOG_FILE = Path(os.getenv("TEST_LOG_FILE", "test_search_log.txt"))


def _log(msg: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg.rstrip() + "\n")


@pytest.fixture(autouse=True)
def log_test_boundaries(request):
    _log(f"\n=== START {request.node.nodeid} ===")
    yield
    _log(f"=== END {request.node.nodeid} ===")


@pytest.fixture(scope="session")
def session() -> requests.Session:
    """
    Вимога: використовуємо requests.Session
    """
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s


@pytest.fixture(scope="session")
def token(session: requests.Session) -> str:
    """
    Логін 1 раз за сесію: POST /auth через Basic Auth.
    """
    url = f"{BASE_URL}/auth"
    _log(f"AUTH POST {url} user={USERNAME}")

    r = session.post(url, auth=(USERNAME, PASSWORD), timeout=10)
    _log(f"AUTH status={r.status_code} body={r.text}")

    assert r.status_code == 200
    data = r.json()
    assert "access_token" in data
    return data["access_token"]


@pytest.fixture(scope="session")
def authed_session(session: requests.Session, token: str) -> requests.Session:
    """
    Після отримання токена прописуємо його в headers Session (вимога зі скріну).
    """
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


def _assert_sorted(items: list[dict], key: str) -> None:
    values = [i[key] for i in items]
    assert values == sorted(values), f"Expected sorted by {key}, got {values}"


# =========================
# AUTH tests
# =========================

def test_auth_success(session: requests.Session):
    r = session.post(f"{BASE_URL}/auth", auth=(USERNAME, PASSWORD), timeout=10)
    _log(f"AUTH success: status={r.status_code} body={r.text}")
    assert r.status_code == 200
    assert r.json().get("access_token")


@pytest.mark.parametrize(
    "bad_user,bad_pass",
    [
        ("user", "pass"),
        (USERNAME, "wrong_pass"),
        ("wrong_user", PASSWORD),
    ],
)
def test_auth_invalid_credentials(session: requests.Session, bad_user: str, bad_pass: str):
    r = session.post(f"{BASE_URL}/auth", auth=(bad_user, bad_pass), timeout=10)
    _log(f"AUTH invalid: user={bad_user} status={r.status_code} body={r.text}")
    assert r.status_code == 401


def test_auth_wrong_method(session: requests.Session):
    r = session.get(f"{BASE_URL}/auth", timeout=10)
    _log(f"AUTH wrong method: status={r.status_code} body={r.text}")
    assert r.status_code == 405


# =========================
# CARS tests
# =========================

def test_cars_unauthorized(session: requests.Session):
    # Без Bearer у headers
    r = session.get(f"{BASE_URL}/cars", timeout=10)
    _log(f"CARS unauth: status={r.status_code} body={r.text}")
    # В залежності від реалізації може бути 401 або 422
    assert r.status_code in (401, 422)


def test_cars_default(authed_session: requests.Session):
    r = authed_session.get(f"{BASE_URL}/cars", timeout=10)
    _log(f"CARS default: status={r.status_code} body_prefix={r.text[:200]}")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    # у твоєму auto.py дефолт limit=25
    assert len(data) == 25


# ✅ параметризація (5-7 наборів) для limit
@pytest.mark.parametrize("limit", [1, 3, 5, 10, 25, 30, 50])
def test_cars_limit_parametrized(authed_session, limit):
    r = authed_session.get(f"{BASE_URL}/cars", params={"limit": limit}, timeout=10)
    _log(f"CARS limit={limit}: status={r.status_code} body_prefix={r.text[:200]}")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)

    # в API фактично максимум 25 записів
    expected = limit if limit <= 25 else 25
    assert len(data) == expected



# ✅ параметризація для sort_by
@pytest.mark.parametrize("sort_by", ["year", "price", "engine_volume"])
def test_cars_sorting_parametrized(authed_session: requests.Session, sort_by: str):
    r = authed_session.get(f"{BASE_URL}/cars", params={"sort_by": sort_by}, timeout=10)
    _log(f"CARS sort_by={sort_by}: status={r.status_code} body_prefix={r.text[:200]}")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 25
    _assert_sorted(data, sort_by)


# ✅ комбінація sort_by + limit
@pytest.mark.parametrize(
    "sort_by,limit",
    [
        ("price", 5),
        ("year", 7),
        ("engine_volume", 4),
    ],
)
def test_cars_sort_and_limit(authed_session: requests.Session, sort_by: str, limit: int):
    r = authed_session.get(
        f"{BASE_URL}/cars",
        params={"sort_by": sort_by, "limit": limit},
        timeout=10,
    )
    _log(f"CARS sort+limit sort_by={sort_by} limit={limit}: status={r.status_code} body_prefix={r.text[:200]}")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == limit
    _assert_sorted(data, sort_by)


def test_cars_invalid_sort_by_is_ignored(authed_session):
    r = authed_session.get(f"{BASE_URL}/cars", params={"sort_by": "bad_field"}, timeout=10)
    _log(f"CARS invalid sort_by (ignored): status={r.status_code} body_prefix={r.text[:200]}")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 25

