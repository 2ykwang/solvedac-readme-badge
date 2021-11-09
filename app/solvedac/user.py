from typing import Dict


class User:
    def __init__(self):
        self.username: str = ""
        """solved.ac 유저 ID"""
        self.bio: str = ""
        """solved.ac 유저 Biography"""
        self.tier: int = 0
        """solved.ac 유저 티어 (0-31)"""
        self.user_class: int = 0
        """solved.ac 유저 클래스 (0-10)"""
        self.user_class_decoration: str = ""
        """solved.ac 유저 클래스 데코레이션 (none, silver, gold)"""
        self.rating: int = 0
        """solved.ac 유저 레이팅"""
        self.exp: int = 0
        """solved.ac 유저가 획득한 경험치"""
        self.rank: int = 0
        """solved.ac 유저 순위"""

        self.json_raw_data: dict = {}
        """solved.ac api 유저 raw data"""
    def __str__(self):
        return str(self.json_raw_data)


def get_user_from_dict(json_data: Dict[str, any]) -> User:
    result = User()

    result.username = json_data["handle"]
    result.bio = json_data["bio"]
    result.tier = json_data["tier"]
    result.user_class = json_data["class"]
    result.user_class_decoration = json_data["classDecoration"]
    result.rating = json_data["rating"]
    result.exp = json_data["exp"]
    result.rank = json_data["rank"]

    result.json_raw_data = json_data

    return result
