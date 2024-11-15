import requests, pytest


"""Запись неполного медведя"""
@pytest.mark.post_incorrect_data
def test_post_not_full_bear(bare_alaska, post_bear_addr):
    test_param = {"bear_type":"POLAR","bear_name":"MISHA"}
    response = requests.post(url=post_bear_addr, json=test_param) 
    assert response.text == "Error. Pls fill all parameters"