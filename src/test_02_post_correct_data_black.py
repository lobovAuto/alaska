import requests, pytest

"""Запись корректного черного медведя"""
@pytest.mark.post_correct_data
def test_post_correct_data_black(bare_alaska, post_bear_addr, test_param_fixt, test_answ_fixt):
    test_param = test_param_fixt
    test_answ  = test_answ_fixt
    test_param["bear_type"] = test_answ["bear_type"] = "BLACK"
    response = requests.post(url=post_bear_addr, json=test_param)
    assert response.status_code == 200
    response = requests.get(url=post_bear_addr)
    assert response.json() == [test_answ]
