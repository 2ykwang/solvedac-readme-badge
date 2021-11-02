from urllib.parse import urljoin
import requests
import json


class SolvedacFetcher:
    def __init__(self, api_host: str):
        self.api_host = api_host
        self.api_url = f'https://{api_host}/api/v3/'

    def get_user_info(self, user_name: str) -> dict:
        response = requests.get(self.__url_wrapping(f"/user/show?handle={user_name}"))
        result = {}

        if response.status_code == 200:
            result = response.json()

        return result

    def get_user_problem_stat(self, user_name: str) -> dict:
        response = requests.get(self.__url_wrapping(f"/user/problem_stats?handle={user_name}"))
        result = {}

        if response.status_code == 200:
            result = response.json()

        return result

    def __url_wrapping(self, path: str):
        if path[0] == '/':
            path = path[1:]
        return urljoin(self.api_url, path)
