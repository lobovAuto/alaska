import requests, pytest

"""Чтение удаленного медведя из БД"""
@pytest.mark.read_incorrect
def test_read_deleted_bear(alaska_with_first_data_block, post_bear_addr):
    response = requests.get(url=post_bear_addr)
    len_base = len(response.json()) 
    response = requests.get(url=post_bear_addr+f"/{len_base}")
    assert response.text != "EMPTY"
    response = requests.delete(url=post_bear_addr+f"/{len_base}")
    response = requests.get(url=post_bear_addr+f"/{len_base}")
    assert response.text == "EMPTY"