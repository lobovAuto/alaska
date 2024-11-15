import pytest, docker, time, requests

EMERGENCY_DOCKER_ID = None

@pytest.fixture(scope="session")
def docker_id():
    # Хранение параметров в словаре
    return {"docker_id": "default_value"}


@pytest.fixture(scope="function")
def setup_alaska(delay_time, docker_port, docker_id):
    client = docker.from_env()
    answer = client.containers.run("azshoo/alaska:1.0", detach=True, remove=True, ports = {f'8091/tcp': docker_port})
    global EMERGENCY_DOCKER_ID
    docker_id["docker_id"] = EMERGENCY_DOCKER_ID = answer.id
    time.sleep(int(delay_time))
    yield

@pytest.fixture(scope="function")
def teardown_alaska(delay_time, docker_id):
    yield
    client = docker.from_env()
    alaska = client.containers.get(docker_id["docker_id"])
    alaska.stop()
    time.sleep(int(delay_time))

def pytest_keyboard_interrupt(excinfo):
    print(" catched keyboard interrupt!")
    global EMERGENCY_DOCKER_ID
    try:
        client = docker.from_env()
        alaska = client.containers.get(EMERGENCY_DOCKER_ID)
        alaska.stop()
    except:
        None

"""Фикстура, которая поднимает пустой контейнер. Завершает и удаляет экземпляр после прохождения теста"""    
@pytest.fixture(scope="function")
def bare_alaska(setup_alaska, teardown_alaska):
    yield

@pytest.fixture(scope="function")
def alaska_with_first_data_block(setup_alaska, teardown_alaska, test_param_fixt, post_bear_addr):
    test_param = test_param_fixt
    bear_types = ["BROWN", "BLACK", "POLAR"]
    for bear in bear_types:
        test_param["bear_type"] = bear
        requests.post(url=post_bear_addr, json=test_param)
    yield

@pytest.fixture
def base_url(docker_port):
    return f'http://localhost:{docker_port}'

@pytest.fixture
def post_bear_addr(base_url):
    return base_url+'/bear'

@pytest.fixture
def test_param_fixt():
    return {"bear_type":"none","bear_name":"MISHA","bear_age":13}

@pytest.fixture
def test_answ_fixt():
    return {"bear_id":1,"bear_type":"none","bear_name":"MISHA","bear_age":13}

def pytest_addoption(parser):
    parser.addoption("--docker_port", action="store", default="8091", help="Порт для проброса в контейнер")
    parser.addoption("--delay_time", action="store", default="1", help="Время задержки между запуском\остановкой контейнера и самим тестом")

@pytest.fixture
def docker_port(request):
    return request.config.getoption("--docker_port")

@pytest.fixture
def delay_time(request):
    return request.config.getoption("--delay_time")