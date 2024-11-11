import docker
def is_even(number):
    return number % 2 == 0

def test_is_even():
    assert is_even(2) == True  # 2 — чётное число
    assert is_even(3) == False  # 3 — нечётное число
    assert is_even(0) == True  # 0 — считается чётным числом
    assert is_even(-4) == True  # -4 — чётное число

def test_is_container():
    client = docker.from_env()
    list_containers = client.images.list()
    condition = False
    for image in list_containers:
        if image.tags[0] == "azshoo/alaska:1.0":
            condition = True
    assert condition == True