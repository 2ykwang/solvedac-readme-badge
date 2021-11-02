
class User:
    def __init__(self):
        self.username = ""
        self.tier = 0


def get_user_from_dict(json_data: dict) -> User:
    result = User()
    result.username = json_data["handle"]
    result.tier = json_data["tier"]
    return result
