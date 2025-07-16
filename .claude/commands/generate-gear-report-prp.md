# Generate Gear Report PRP

## Description
감속기 보고서 작성을 위한 PRP(Product Requirements Prompt)를 생성합니다.

## Usage
```
/generate-gear-report-prp [feature_name]
```

## Parameters
- `feature_name`: 생성할 보고서 기능명 (예: strength_analysis, stiffness_calculation)

## Script
```bash
#!/bin/bash

FEATURE_NAME=${1:-"gear_analysis"}
PRP_FILE="PRPs/${FEATURE_NAME}_prp.md"

# PRP 템플릿 복사
cp "PRPs/templates/gear_report_base.md" "$PRP_FILE"

# init.md에서 파라미터 읽기
PARAMETERS=$(cat init.md)

# PRP 파일에 파라미터 삽입
cat << EOF >> "$PRP_FILE"

## Project Parameters (from init.md)
$PARAMETERS

## Generated: $(date)
EOF

echo "✅ PRP 생성 완료: $PRP_FILE"
echo "📝 다음 단계: /execute-gear-analysis $FEATURE_NAME"
```

## Context Engineering Integration
이 커맨드는 Context-Engineering-Intro 방법론을 적용하여:
1. 프로젝트 컨텍스트 통합
2. 표준화된 PRP 구조 적용
3. 자동화된 워크플로우 지원
4. 품질 검증 게이트 포함