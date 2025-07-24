#!/bin/bash

echo "🚀 리팩터링된 API 테스트 시작"

# 서버가 실행 중인지 확인
if ! curl -s http://localhost:8000/docs > /dev/null; then
    echo "⚠️  서버가 실행되지 않은 것 같습니다. 서버를 먼저 시작해주세요."
    echo "   실행 명령: uvicorn app:create_app --reload"
    exit 1
fi

echo "✅ 서버 연결 확인"

# API 정보 테스트
echo -e "\n=== API 정보 테스트 ==="
curl -s "http://localhost:8000/api/v1/info" | jq '.' 2>/dev/null || echo "API 정보 조회 실패"

# Badge 생성 테스트
echo -e "\n=== Badge 생성 테스트 ==="
echo "기본 Badge 생성:"
curl -s "http://localhost:8000/api/v1/badge?user=test_user&theme=white&size=small" | head -c 100

echo -e "\n\n커스텀 색상 Badge:"
curl -s "http://localhost:8000/api/v1/badge?user=test_user&theme=dark&size=medium&common_color=FF6B6B&sub_color=4ECDC4" | head -c 100

echo -e "\n\n컴팩트 모드 Badge:"
curl -s "http://localhost:8000/api/v1/badge?user=test_user&theme=github-dark&size=large&compact=true" | head -c 100

# 레거시 API 호환성 테스트
echo -e "\n=== 레거시 API 호환성 테스트 ==="
curl -s "http://localhost:8000/api/v1/generate/api?user=test_user&theme=white&size=small&use_shadow=true&compact=true" | head -c 100

echo -e "\n🎉 테스트 완료!"