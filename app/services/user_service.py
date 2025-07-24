import logging
from typing import Optional
from app.solvedac import User, SolvedacFetcher, get_user_from_dict
from app import cache


class UserService:
    def __init__(self, api_host: str, timeout: int):
        self.api_host = api_host
        self.timeout = timeout
        self.fetcher = SolvedacFetcher(api_host, timeout)
        self.logger = logging.getLogger("uvicorn.error")

    def get_user(self, username: str) -> Optional[User]:
        """사용자 정보를 가져옵니다. 캐시를 우선 확인합니다."""
        if not username:
            return None

        try:
            # 캐시에서 먼저 확인
            cached_user = cache.get(username)
            if cached_user is not None:
                return cached_user

            # API에서 가져오기
            user = self._fetch_user_from_api(username)
            if user:
                cache[username] = user
                self.logger.info(f"데이터 불러옴: {username}")
            
            return user
        except Exception as e:
            self.logger.error(f"사용자 정보 가져오기 실패 - {username}: {e}")
            return None

    def _fetch_user_from_api(self, username: str) -> Optional[User]:
        """API에서 사용자 정보를 가져옵니다."""
        try:
            json_data = self.fetcher.get_user_info(username)
            return get_user_from_dict(json_data)
        except Exception as e:
            self.logger.error(f"API 호출 실패 - {username}: {e}")
            return None