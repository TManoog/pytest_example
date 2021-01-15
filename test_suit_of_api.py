import pytest
import requests
import json
from get_data import GetTestData


class Tests(GetTestData):
    @classmethod
    def setup_class(cls):
        print('\nThe Api Test Suit Running')

    @pytest.fixture()
    def single_user(self):
        print('\nSingle user test case going to be Executed')

    def setup_method(self, method):
        if method == self.test_get_user_list:
            print('\nRunning test_get_user_list')
        elif method == self.test_get_second_user_date:
            print('\nRunning get_single_user_with')
        elif method == self.test_get_user_with_wrong_id:
            print('\nRunning test_get_user_with_wrong_id')
        else:
            print(f'\nRunning unknown method: {str(method)}')

    def teardown_method(self, method):
        if method == self.test_get_user_list:
            print('\nRunning of test_get_user_list over')
        elif method == self.test_get_second_user_date:
            print('\nRunning of test_get_second_user_date over')
        elif method == self.test_get_user_with_wrong_id:
            print('\nRunning of test_get_user_with_wrong_id over')
        else:
            print(f'\nRunning of unknown method is over: {str(method)}')

    def test_get_user_list(self):
        test_data = json.load(open('data/user_list.json', 'r'))
        user_list = self.get_user_list()
        assert test_data == user_list

    def test_get_user_with_wrong_id(self, single_user):
        test_data = 'User Not Found. Status Code: 404'
        user_data = self.get_single_user_with(user_id=23)
        assert test_data == user_data

    def test_get_second_user_date(self, single_user):
        test_data = json.load(open('data/single_user_id_2_data.json', 'r'))
        user_data = self.get_single_user_with(user_id=2)
        assert test_data == user_data

    @classmethod
    def teardown_class(cls):
        print('\nThe Api Test Suit Run Ends')
