from typing import Dict


class User:
    def __init__(
        self,
        username: str = "",
        bio: str = "",
        tier: int = 0,
        user_class: int = 0,
        user_class_decoration: str = "",
        rating: int = 0,
        exp: int = 0,
        rank: int = 0,
    ):
        self.username: str = username
        self.bio: str = bio
        self.tier: int = tier
        self.user_class: int = user_class
        self.user_class_decoration: str = user_class_decoration
        self.rating: int = rating
        self.exp: int = exp
        self.rank: int = rank

        self.json_raw_data: dict = {}

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
