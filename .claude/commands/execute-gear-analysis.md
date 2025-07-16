# Execute Gear Analysis

## Description
생성된 PRP를 기반으로 감속기 분석 및 보고서 작성을 실행합니다.

## Usage
```
/execute-gear-analysis [prp_name]
```

## Parameters
- `prp_name`: 실행할 PRP 파일명 (확장자 제외)

## Script
```bash
#!/bin/bash

PRP_NAME=${1:-"gear_analysis"}
PRP_FILE="PRPs/${PRP_NAME}_prp.md"

if [ ! -f "$PRP_FILE" ]; then
    echo "❌ PRP 파일을 찾을 수 없습니다: $PRP_FILE"
    echo "💡 먼저 /generate-gear-report-prp $PRP_NAME 을 실행하세요"
    exit 1
fi

echo "🚀 감속기 분석 시작: $PRP_NAME"
echo "📋 PRP 파일: $PRP_FILE"

# Phase 1: Analysis Agent 실행
echo "🔍 Phase 1: 강도/강성 분석 중..."
python agents/analysis_agent.py --prp "$PRP_FILE" --phase "analysis"

# Phase 2: Calculation Agent 실행  
echo "🧮 Phase 2: 수치 계산 중..."
python agents/calculation_agent.py --prp "$PRP_FILE" --phase "calculation"

# Phase 3: Document Agent 실행
echo "📝 Phase 3: 보고서 작성 중..."
python agents/document_agent.py --prp "$PRP_FILE" --phase "documentation"

# Phase 4: Validation Agent 실행
echo "✅ Phase 4: 품질 검증 중..."
python agents/validation_agent.py --prp "$PRP_FILE" --phase "validation"

# 최종 결과 확인
if [ $? -eq 0 ]; then
    echo "🎉 감속기 보고서 생성 완료!"
    echo "📄 결과 파일: reports/${PRP_NAME}_final_report.md"
else
    echo "❌ 처리 중 오류 발생. 로그를 확인하세요."
fi
```

## Validation Gates
각 단계별 검증 기준:

### Level 1: 기본 검증
- [ ] 파일 구문 오류 검사
- [ ] 필수 파라미터 존재 확인
- [ ] 계산 공식 문법 검증

### Level 2: 공학적 검증
- [ ] ISO 6336 표준 준수 확인
- [ ] 안전계수 요구사항 만족
- [ ] 단위 일관성 검사

### Level 3: 품질 검증
- [ ] 학술 논문 스타일 준수
- [ ] 참고문헌 완성도 확인
- [ ] 그래프/표 품질 검사

### Level 4: 통합 검증
- [ ] 전체 보고서 일관성
- [ ] 결론의 논리적 타당성
- [ ] 최종 품질 승인