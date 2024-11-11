import docker

def test_is_container():
    client = docker.from_env()
    list_containers = client.images.list()
    condition = False
    for image in list_containers:
        if image.tags[0] == "azshoo/alaska:1.0":
            condition = True
    assert condition == True