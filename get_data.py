import requests


class GetTestData:
    url = "https://reqres.in/"
    user_list_api = f'{url}api/users?page=2'
    single_user_api = f'{url}api/users/'

    def get_user_list(self):
        return requests.request("GET", self.user_list_api).json()

    def get_single_user_with(self, user_id=2):
        user_info = requests.request("GET", self.single_user_api + str(user_id))
        if len(user_info.json()) is not 0:
            return user_info.json()
        else:
            return f"User Not Found. Status Code: {user_info.status_code}"

