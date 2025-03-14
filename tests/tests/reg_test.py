import allure
import requests

from tests.pages.reg_tests_class import ReqresApi

base_url = "https://reqres.in/api"
api = ReqresApi(base_url)

@allure.title("get user by id")
@allure.id('test_1')
def test_get_user_by_id_valid():
    user_data = api.get_user_by_id(2)
    print(user_data)

    assert user_data['id'] == 2

    assert user_data['email'].endswith('reqres.in')
    assert user_data['first_name'], "Username is empty!"
    assert user_data['first_name'].isalpha(), "Username contains non-alphabetic characters!"

@allure.title("get 6 user and user email")
@allure.id('test_2')
def test_6_users_and_end_email():
    userlist = api.get_userlist()
    print(userlist)
    assert all(q['email'].endswith('reqres.in') for q in userlist)


@allure.story('Test end of avatar')
@allure.severity(allure.severity_level.MINOR)
@allure.title("Check end avatar")
@allure.description("Checking that Avatar ends on ID, which corresponds to user")
@allure.id('test_2')
def test_ends_avatar_with_id():
    userlist = api.get_userlist()
    assert all(q['avatar'].endswith(f'{q['id']}-image.jpg') for q in userlist)


@allure.title("Successful registration")
@allure.description("Registration with valid credentials")
@allure.id('test_reg')
def test_success_reg():
    with allure.step('Register user with LOGIN: "eve.holt@reqres.in", PASSWORD: "pistol"'):
        response_data = api.register("eve.holt@reqres.in", "pistol")
    print(response_data)
    with allure.step('Check data ID == 4'):
        assert response_data['id'] == 4



def test_unsuccessful_register():
    response_data = api.register("eve.ho1lt@reqres.in", "pistol")
    assert response_data['error'] == "Note: Only defined users succeed registration"


