#!/usr/bin/env python3
"""
리팩터링된 API를 테스트하는 스크립트
"""

import requests
import json
from urllib.parse import urlencode


def test_api_info(base_url: str = "http://localhost:8000"):
    """API 정보 엔드포인트를 테스트합니다."""
    print("=== API 정보 테스트 ===")
    try:
        response = requests.get(f"{base_url}/api/v1/info")
        if response.status_code == 200:
            data = response.json()
            print("✅ API 정보 조회 성공")
            print(f"사용 가능한 크기: {data['available_sizes']}")
            print(f"사용 가능한 테마: {data['available_themes']}")
            print(f"설명: {data['description']}")
        else:
            print(f"❌ API 정보 조회 실패: {response.status_code}")
    except Exception as e:
        print(f"❌ API 정보 조회 중 오류: {e}")


def test_badge_generation(base_url: str = "http://localhost:8000"):
    """Badge 생성 API를 테스트합니다."""
    print("\n=== Badge 생성 테스트 ===")
    
    # 테스트 케이스들
    test_cases = [
        {
            "name": "기본 Badge 생성",
            "params": {"user": "test_user", "theme": "white", "size": "small"}
        },
        {
            "name": "커스텀 색상 Badge",
            "params": {
                "user": "test_user", 
                "theme": "dark", 
                "size": "medium",
                "common_color": "FF6B6B",
                "sub_color": "4ECDC4"
            }
        },
        {
            "name": "컴팩트 모드 Badge",
            "params": {
                "user": "test_user", 
                "theme": "github-dark", 
                "size": "large",
                "compact": "true"
            }
        }
    ]
    
    for test_case in test_cases:
        print(f"\n--- {test_case['name']} ---")
        try:
            url = f"{base_url}/api/v1/badge?{urlencode(test_case['params'])}"
            response = requests.get(url)
            
            if response.status_code == 200:
                print("✅ Badge 생성 성공")
                print(f"Content-Type: {response.headers.get('content-type')}")
                print(f"Content-Length: {len(response.content)} bytes")
                
                # SVG 내용 확인
                content = response.text
                if content.startswith("<svg"):
                    print("✅ 유효한 SVG 응답")
                else:
                    print("❌ SVG가 아닌 응답")
            else:
                print(f"❌ Badge 생성 실패: {response.status_code}")
                if response.headers.get('content-type') == 'application/json':
                    error_data = response.json()
                    print(f"오류: {error_data}")
        except Exception as e:
            print(f"❌ Badge 생성 중 오류: {e}")


def test_legacy_compatibility(base_url: str = "http://localhost:8000"):
    """레거시 API 호환성을 테스트합니다."""
    print("\n=== 레거시 API 호환성 테스트 ===")
    
    legacy_params = {
        "user": "test_user",
        "theme": "white",
        "size": "small",
        "use_shadow": "true",
        "compact": "true"
    }
    
    try:
        url = f"{base_url}/api/v1/generate/api?{urlencode(legacy_params)}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print("✅ 레거시 API 호환성 확인")
            print(f"Content-Type: {response.headers.get('content-type')}")
        else:
            print(f"❌ 레거시 API 호환성 실패: {response.status_code}")
    except Exception as e:
        print(f"❌ 레거시 API 테스트 중 오류: {e}")


def main():
    """메인 테스트 함수"""
    print("🚀 리팩터링된 API 테스트 시작")
    
    # 서버가 실행 중인지 확인
    try:
        response = requests.get("http://localhost:8000/docs")
        if response.status_code != 200:
            print("⚠️  서버가 실행되지 않은 것 같습니다. 서버를 먼저 시작해주세요.")
            print("   실행 명령: uvicorn app:create_app --reload")
            return
    except:
        print("⚠️  서버에 연결할 수 없습니다. 서버를 먼저 시작해주세요.")
        print("   실행 명령: uvicorn app:create_app --reload")
        return
    
    # 테스트 실행
    test_api_info()
    test_badge_generation()
    test_legacy_compatibility()
    
    print("\n🎉 모든 테스트 완료!")


if __name__ == "__main__":
    main()