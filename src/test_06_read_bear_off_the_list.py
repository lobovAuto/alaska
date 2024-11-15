import requests, pytest

"""Чтение заведомо несуществующего медведя из БД"""
@pytest.mark.read_incorrect
def test_read_bear_off_the_list(alaska_with_first_data_block, post_bear_addr):
    response = requests.get(url=(post_bear_addr+"/100"))
    assert response.text == "EMPTY"