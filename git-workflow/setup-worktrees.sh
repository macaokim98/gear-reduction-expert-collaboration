#!/bin/bash

# Git Worktree 설정 스크립트
# 6명 전문가 협업을 위한 워크트리 구조 자동 생성

set -e

echo "🚀 Git Worktree 전문가 협업 환경 설정 시작..."

# 현재 위치 확인
if [ ! -d ".git" ]; then
    echo "❌ Git 저장소가 아닙니다. git init 먼저 실행하세요."
    exit 1
fi

# 워크트리 디렉토리 생성
echo "📁 워크트리 디렉토리 구조 생성..."
mkdir -p worktrees
mkdir -p reports
mkdir -p logs

# 전문가별 브랜치 생성 및 워크트리 설정
echo "👥 전문가별 워크트리 생성..."

experts=(
    "dr-analysis:Dr. Analysis 강도해석 전용 워크스페이스"
    "prof-calculator:Prof. Calculator 계산검증 전용 워크스페이스"
    "dr-writer:Dr. Writer 문서작성 전용 워크스페이스"
    "design-layout:Design Layout 시각화 전용 워크스페이스"
    "inspector-quality:Inspector Quality 품질검증 전용 워크스페이스"
    "director-manager:Director Manager 프로젝트관리 전용 워크스페이스"
)

for expert_info in "${experts[@]}"; do
    IFS=':' read -r expert_name expert_desc <<< "$expert_info"
    
    echo "  🔬 $expert_name 워크트리 생성 중..."
    
    # 브랜치가 이미 존재하는지 확인
    if git show-ref --verify --quiet refs/heads/expert/$expert_name; then
        echo "    ⚠️  브랜치 expert/$expert_name 이미 존재함"
        # 기존 워크트리 제거 후 재생성
        if [ -d "worktrees/$expert_name" ]; then
            git worktree remove "worktrees/$expert_name" 2>/dev/null || true
        fi
        git worktree add "worktrees/$expert_name" expert/$expert_name
    else
        # 새 브랜치로 워크트리 생성
        git worktree add "worktrees/$expert_name" -b expert/$expert_name
    fi
    
    # 각 전문가 워크트리에 전용 작업 공간 설정
    cd "worktrees/$expert_name"
    
    # 전문가별 작업 디렉토리 생성
    case $expert_name in
        "dr-analysis")
            mkdir -p analysis calculations results
            echo "# Dr. Analysis 작업 공간

## 담당 업무
- ISO 6336 기반 기어 강도 해석
- 시스템 강성 분석
- 안전계수 계산 및 검증

## 작업 디렉토리
- analysis/: 해석 모델 및 설정
- calculations/: 계산 결과 파일
- results/: 최종 해석 결과

## 진행 상황
- [ ] 기어 형상 모델링
- [ ] 하중 조건 설정
- [ ] 강도 해석 수행
- [ ] 강성 해석 수행
- [ ] 결과 검증 및 정리

$expert_desc" > README.md
            ;;
        "prof-calculator")
            mkdir -p calculations verification uncertainty
            echo "# Prof. Calculator 작업 공간

## 담당 업무
- 정밀 수치 계산
- 다중 방법론 교차 검증
- 불확실성 정량화

## 작업 디렉토리
- calculations/: 정밀 계산 스크립트
- verification/: 검증 결과
- uncertainty/: 불확실성 분석

## 진행 상황
- [ ] 계산 방법론 설정
- [ ] 정밀 계산 수행
- [ ] 교차 검증 실행
- [ ] 불확실성 분석
- [ ] 최종 검증 완료

$expert_desc" > README.md
            ;;
        "dr-writer")
            mkdir -p drafts references templates
            echo "# Dr. Writer 작업 공간

## 담당 업무
- 학술 논문 수준 보고서 작성
- IEEE/ASME 스타일 적용
- 문헌 조사 및 인용 관리

## 작업 디렉토리
- drafts/: 보고서 초안
- references/: 참고문헌 관리
- templates/: 문서 템플릿

## 진행 상황
- [ ] 문헌 조사 완료
- [ ] 보고서 구조 설계
- [ ] 초안 작성
- [ ] 편집 및 교정
- [ ] 최종 검토

$expert_desc" > README.md
            ;;
        "design-layout")
            mkdir -p charts diagrams layouts
            echo "# Design Layout 작업 공간

## 담당 업무
- 전문적 차트 및 그래프 생성
- 문서 레이아웃 디자인
- 시각적 일관성 확보

## 작업 디렉토리
- charts/: 데이터 시각화
- diagrams/: 기술 도면
- layouts/: 레이아웃 디자인

## 진행 상황
- [ ] 시각화 계획 수립
- [ ] 차트 및 그래프 생성
- [ ] 레이아웃 디자인
- [ ] 시각적 일관성 검토
- [ ] 최종 디자인 완료

$expert_desc" > README.md
            ;;
        "inspector-quality")
            mkdir -p audits compliance risk-assessment
            echo "# Inspector Quality 작업 공간

## 담당 업무
- 종합 품질 감사
- 표준 준수 검증
- 위험 평가 및 관리

## 작업 디렉토리
- audits/: 품질 감사 결과
- compliance/: 표준 준수 검증
- risk-assessment/: 위험 평가

## 진행 상황
- [ ] 감사 체크리스트 준비
- [ ] 품질 감사 수행
- [ ] 표준 준수 검증
- [ ] 위험 평가 실시
- [ ] 최종 품질 인증

$expert_desc" > README.md
            ;;
        "director-manager")
            mkdir -p planning coordination monitoring
            echo "# Director Manager 작업 공간

## 담당 업무
- 전체 프로젝트 관리
- 팀 조율 및 의사결정
- 이해관계자 관리

## 작업 디렉토리
- planning/: 프로젝트 계획
- coordination/: 팀 조율 활동
- monitoring/: 진행 상황 모니터링

## 진행 상황
- [ ] 프로젝트 계획 수립
- [ ] 팀 조율 체계 구축
- [ ] 진행 상황 모니터링
- [ ] 이해관계자 관리
- [ ] 최종 승인 및 전달

$expert_desc" > README.md
            ;;
    esac
    
    # 기본 파일 생성
    touch .gitkeep
    
    # 초기 커밋
    git add .
    git commit -m "Initial setup for $expert_name workspace

- Created dedicated directory structure
- Added README with responsibilities
- Set up workflow tracking

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>" 2>/dev/null || echo "    ℹ️  No changes to commit for $expert_name"
    
    cd ../..
    echo "    ✅ $expert_name 워크트리 설정 완료"
done

# 통합 브랜치 및 워크트리 생성
echo "🔄 통합 단계 워크트리 생성..."

integration_phases=(
    "phase-1:1단계 통합 (분석+계산)"
    "phase-2:2단계 통합 (문서+디자인)"  
    "phase-3:3단계 통합 (품질검증)"
)

for phase_info in "${integration_phases[@]}"; do
    IFS=':' read -r phase_name phase_desc <<< "$phase_info"
    
    echo "  🔄 integration-$phase_name 워크트리 생성 중..."
    
    if git show-ref --verify --quiet refs/heads/integration/$phase_name; then
        echo "    ⚠️  브랜치 integration/$phase_name 이미 존재함"
        if [ -d "worktrees/integration-$phase_name" ]; then
            git worktree remove "worktrees/integration-$phase_name" 2>/dev/null || true
        fi
        git worktree add "worktrees/integration-$phase_name" integration/$phase_name
    else
        git worktree add "worktrees/integration-$phase_name" -b integration/$phase_name
    fi
    
    cd "worktrees/integration-$phase_name"
    
    mkdir -p integrated-results logs
    echo "# Integration Phase: $phase_desc

## 통합 대상
$(case $phase_name in
    "phase-1") echo "- expert/dr-analysis
- expert/prof-calculator" ;;
    "phase-2") echo "- expert/dr-writer  
- expert/design-layout
- integration/phase-1 (병합된 분석 결과)" ;;
    "phase-3") echo "- expert/inspector-quality
- expert/director-manager
- integration/phase-2 (문서화된 결과)" ;;
esac)

## 통합 절차
1. 각 전문가 브랜치 최신 상태 확인
2. 충돌 사항 식별 및 해결
3. 품질 검증 수행
4. 통합 테스트 실행
5. 다음 단계로 승인

## 진행 상황
- [ ] 브랜치 상태 점검
- [ ] 충돌 해결
- [ ] 통합 실행
- [ ] 품질 검증
- [ ] 승인 완료" > README.md
    
    touch .gitkeep
    git add .
    git commit -m "Setup integration $phase_name workspace

$phase_desc

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>" 2>/dev/null || echo "    ℹ️  No changes to commit for integration-$phase_name"
    
    cd ../..
    echo "    ✅ integration-$phase_name 워크트리 설정 완료"
done

# 최종 릴리즈 워크트리 생성
echo "🚀 최종 릴리즈 워크트리 생성..."

if git show-ref --verify --quiet refs/heads/release/final-report; then
    echo "  ⚠️  브랜치 release/final-report 이미 존재함"
    if [ -d "worktrees/final-release" ]; then
        git worktree remove "worktrees/final-release" 2>/dev/null || true
    fi
    git worktree add "worktrees/final-release" release/final-report
else
    git worktree add "worktrees/final-release" -b release/final-report
fi

cd "worktrees/final-release"

mkdir -p final-report documentation deliverables
echo "# 최종 릴리즈 워크스페이스

## 최종 결과물
- 종합 기술 보고서 (25+ 페이지)
- 계산 검증 패키지
- 품질 인증 문서
- 시각화 자료 집합

## 릴리즈 체크리스트
- [ ] 모든 통합 단계 완료
- [ ] 품질 기준 만족 확인
- [ ] 최종 검토 및 승인
- [ ] 문서 패키징
- [ ] 릴리즈 노트 작성

## 승인 사인오프
- [ ] Dr. Analysis (기술적 정확성)
- [ ] Prof. Calculator (계산 검증)
- [ ] Dr. Writer (문서 품질)
- [ ] Design Layout (시각적 품질)
- [ ] Inspector Quality (품질 인증)
- [ ] Director Manager (최종 승인)" > README.md

touch .gitkeep
git add .
git commit -m "Setup final release workspace

Ready for final integration and delivery

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>" 2>/dev/null || echo "  ℹ️  No changes to commit for final-release"

cd ../..

# 워크트리 상태 요약
echo ""
echo "📊 Git Worktree 설정 완료!"
echo ""
echo "생성된 워크트리 목록:"
git worktree list

echo ""
echo "브랜치 구조:"
git branch -a

echo ""
echo "🎯 다음 단계:"
echo "1. 각 전문가는 자신의 워크트리에서 작업"
echo "   cd worktrees/[expert-name]"
echo ""
echo "2. 단계별 통합 실행"
echo "   ./git-workflow/integrate-phase.sh phase-1"
echo ""
echo "3. 최종 릴리즈"
echo "   ./git-workflow/integrate-phase.sh final"
echo ""
echo "4. 진행 상황 모니터링"
echo "   ./git-workflow/status-report.sh"

echo ""
echo "✅ Git Worktree 전문가 협업 환경 설정 완료!"