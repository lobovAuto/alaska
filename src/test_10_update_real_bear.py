import requests, pytest

"""Правильное обновление существующего медведя"""
@pytest.mark.data_update
def test_update_real_bear(alaska_with_first_data_block, post_bear_addr):
    response = requests.get(url=post_bear_addr+"/1")
    old_bear_type = response.json()["bear_type"]
    updated_bear_data = {"bear_type":response.json()["bear_type"],
                         "bear_name":response.json()["bear_name"],
                         "bear_age":response.json()["bear_age"]}
    if updated_bear_data["bear_type"] == "BLACK":
        updated_bear_data["bear_type"] = "BROWN"
    else:
        updated_bear_data["bear_type"] = "BLACK"
    updated_bear_data["bear_name"] = "NEW_NAME"
    updated_bear_data["bear_age"] = "999"
    response = requests.post(url=post_bear_addr+"/1", json=updated_bear_data)
    assert response.status_code == 200, "Сервер вернул ошибку при попытке обновления данных о медведе"
    response = requests.get(url=post_bear_addr+f"/1")
    assert response.json()["bear_type"] != old_bear_type, "Изменение типа медведя не сработало"
    assert response.json()["bear_name"] == "NEW_NAME", "Изменение имени медведя не сработало"
    assert response.json()["bear_age"] == 999, "Изменение возраста медведя не сработало"