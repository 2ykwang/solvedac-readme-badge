from typing import Dict, List
from urllib.parse import urljoin

import requests


class SolvedacFetcher:
    def __init__(self, api_host: str, timeout: int = 30):
        self.api_host = api_host
        self.api_url = f"https://{api_host}/api/v3/"
        self.timeout = timeout

    def get_user_info(self, user_name: str) -> Dict[str, any]:
        r"""유저 정보를 가져옵니다.

        :param user_name: (str): 정보를 불러 올 사용자명
        :return: `dict` 유저 정보 json
        :rtype: dict
        :raises: TimeoutError
        """
        uri = self.__url_wrapping(f"/user/show?handle={user_name}")
        try:
            response = requests.get(uri, timeout=self.timeout)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("유저 정보를 불러올 수 없습니다.", user_name)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"get_user_info {self.timeout}s 타임아웃", user_name)

    def get_user_problem_stat(self, user_name: str) -> List[Dict[str, any]]:
        r"""사용자가 푼 문제 개수를 문제 수준별로 가져옵니다.

        :param user_name: (str): 정보를 불러 올 사용자명
        :return: `dict` 문제 정보 json
        :rtype: dict
        :raises: TimeoutError
        """
        uri = self.__url_wrapping(f"/user/problem_stats?handle={user_name}")
        try:
            response = requests.get(uri, timeout=self.timeout)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("유저 문제풀이 정보를 불러올 수 없습니다.", user_name)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"get_user_problem_stat {self.timeout}s 타임아웃", user_name)

    def __url_wrapping(self, path: str):
        if path[0] == "/":
            path = path[1:]
        return urljoin(self.api_url, path)
