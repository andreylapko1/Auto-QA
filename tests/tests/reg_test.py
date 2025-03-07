from tests.pages.reg_tests_class import ReqresApi

base_url = "https://reqres.in/api"
api = ReqresApi(base_url)

def test_get_user_by_id_valid():
    user_data = api.get_user_by_id(2)
    print(user_data)

    assert user_data['id'] == 2

    assert user_data['email'].endswith('reqres.in')
    assert user_data['first_name'], "Username is empty!"
    assert user_data['first_name'].isalpha(), "Username contains non-alphabetic characters!"


def test_6_users_and_end_email():
    userlist = api.get_userlist()
    print(userlist)
    assert all(q['email'].endswith('reqres.in') for q in userlist)

def test_ends_avatar_with_id():
    userlist = api.get_userlist()
    assert all(q['avatar'].endswith(f'{q['id']}-image.jpg') for q in userlist)

def test_success_reg():
    response_data = api.register("eve.holt@reqres.in", "pistol")
    print(response_data)
    assert response_data['id'] == 4

def test_unsuccessful_register():
    response_data = api.register("eve.ho1lt@reqres.in", "pistol")
    assert response_data['error'] == "Note: Only defined users succeed registration"