import requests, pytest

"""Неправильное обновление существующего медведя"""
@pytest.mark.data_update
def test_wrong_update_real_bear(alaska_with_first_data_block, post_bear_addr):
    response = requests.get(url=post_bear_addr+"/1")
    updated_bear_data = {"bear_type":response.json()["bear_type"],
                         "bear_name":response.json()["bear_name"],
                         "bear_age":response.json()["bear_age"]}
    updated_bear_data["bear_type"] = "BROWN"
    response = requests.post(url=post_bear_addr+"/1", json=updated_bear_data)
    assert response.status_code == 404, "Сервер вернул ошибку при попытке обновления данных о несуществующем медведе"