import requests, pytest


"""Запись неверного медведя"""
@pytest.mark.post_incorrect_data
def test_post_wrong_type(bare_alaska, post_bear_addr, test_param_fixt):
    test_param = test_param_fixt
    test_param["bear_type"] = "DUMMY"
    response = requests.post(url=post_bear_addr, json=test_param) 
    assert response.status_code == 500