from .user import User


def get_user_from_dict(json_data: dict) -> User:
    result = User()
    result.username = json_data["handle"]
    result.tier = json_data["tier"]
    return result
