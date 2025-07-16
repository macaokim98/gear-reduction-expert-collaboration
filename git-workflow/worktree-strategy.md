# Git Worktree 브랜치 전략 - 전문가 협업

## 브랜치 전략 개요

6명의 전문가가 독립적으로 작업하고 최종적으로 통합하는 Git Worktree 기반 협업 전략

```
main (메인 브랜치)
├── expert/dr-analysis       - Dr. Analysis 작업 브랜치
├── expert/prof-calculator   - Prof. Calculator 작업 브랜치  
├── expert/dr-writer         - Dr. Writer 작업 브랜치
├── expert/design-layout     - Design Layout 작업 브랜치
├── expert/inspector-quality - Inspector Quality 작업 브랜치
├── expert/director-manager  - Director Manager 작업 브랜치
├── integration/phase-1      - 1단계 통합 브랜치 (분석+계산)
├── integration/phase-2      - 2단계 통합 브랜치 (문서+디자인)
├── integration/phase-3      - 3단계 통합 브랜치 (품질검증)
└── release/final-report     - 최종 릴리즈 브랜치
```

## Worktree 구조

```
reduction-report/                  # 메인 작업 디렉토리 (main 브랜치)
├── worktrees/
│   ├── dr-analysis/              # Dr. Analysis 전용 워크트리
│   ├── prof-calculator/          # Prof. Calculator 전용 워크트리
│   ├── dr-writer/                # Dr. Writer 전용 워크트리
│   ├── design-layout/            # Design Layout 전용 워크트리
│   ├── inspector-quality/        # Inspector Quality 전용 워크트리
│   ├── director-manager/         # Director Manager 전용 워크트리
│   ├── integration-phase1/       # 1단계 통합 워크트리
│   ├── integration-phase2/       # 2단계 통합 워크트리
│   ├── integration-phase3/       # 3단계 통합 워크트리
│   └── final-release/            # 최종 릴리즈 워크트리
└── reports/                      # 생성된 보고서 수집 디렉토리
```

## 워크플로우 단계

### Phase 0: 초기 설정
1. 메인 브랜치에서 모든 전문가 브랜치 생성
2. 각 전문가별 worktree 생성
3. 기본 템플릿 및 구조 배포

### Phase 1: 병렬 전문가 작업 (Day 1-3)
- `expert/dr-analysis`: 강도/강성 해석 수행
- `expert/prof-calculator`: 정밀 계산 및 검증
- `expert/dr-writer`: 문헌 조사 및 문서 구조 설계
- `expert/design-layout`: 시각화 계획 및 초기 레이아웃

### Phase 2: 1차 통합 (Day 4)
- `integration/phase-1`: Dr. Analysis + Prof. Calculator 결과 통합
- 기술적 검증 및 계산 결과 조율

### Phase 3: 2차 통합 (Day 5-6)
- `integration/phase-2`: Dr. Writer + Design Layout 통합
- 문서화 및 시각화 통합

### Phase 4: 품질 검증 (Day 6-7)
- `integration/phase-3`: Inspector Quality 품질 검증
- Director Manager 최종 검토

### Phase 5: 최종 릴리즈 (Day 7)
- `release/final-report`: 최종 보고서 릴리즈

## 명령어 참조

### 워크트리 생성
```bash
# 전문가 브랜치 생성 및 워크트리 설정
git worktree add worktrees/dr-analysis -b expert/dr-analysis
git worktree add worktrees/prof-calculator -b expert/prof-calculator
# ... (다른 전문가들)
```

### 통합 브랜치 관리
```bash
# 1단계 통합
git worktree add worktrees/integration-phase1 -b integration/phase-1
cd worktrees/integration-phase1
git merge expert/dr-analysis expert/prof-calculator
```

### 최종 통합
```bash
# 최종 릴리즈
git worktree add worktrees/final-release -b release/final-report
cd worktrees/final-release
git merge integration/phase-3
```

## 충돌 해결 전략

### 자동 해결 가능한 충돌
- 서로 다른 파일 수정
- 서로 다른 디렉토리 작업

### 수동 해결 필요한 충돌
- 동일 파일의 다른 섹션 수정
- 공통 설정 파일 수정
- 문서 구조 변경

### 충돌 해결 우선순위
1. Director Manager 최종 결정권
2. Inspector Quality 품질 기준 적용
3. 기술적 정확성 우선 (Dr. Analysis, Prof. Calculator)
4. 문서 일관성 유지 (Dr. Writer, Design Layout)

## 품질 게이트

### 각 브랜치 머지 전 체크리스트
- [ ] 코드 품질 검사 통과
- [ ] 문서 완성도 확인
- [ ] 테스트 통과 (해당하는 경우)
- [ ] 페어 리뷰 완료
- [ ] 표준 준수 확인

### 통합 단계별 검증
- **Phase 1**: 기술적 정확성 및 계산 검증
- **Phase 2**: 문서 품질 및 시각적 일관성
- **Phase 3**: 전체 품질 기준 및 표준 준수
- **Phase 5**: 최종 승인 및 릴리즈 준비

## 백업 및 복구 전략

### 정기 백업
- 각 워크트리별 일일 커밋
- 통합 단계별 태그 생성
- 원격 저장소 동기화

### 롤백 시나리오
```bash
# 특정 전문가 작업 롤백
git worktree remove worktrees/expert-name
git branch -d expert/expert-name
git worktree add worktrees/expert-name -b expert/expert-name

# 통합 단계 롤백
git reset --hard HEAD~1  # 마지막 머지 취소
```

## 모니터링 및 진행 상황 추적

### 브랜치별 진행률 확인
```bash
# 각 전문가 작업 상태
git log --oneline expert/dr-analysis
git diff main..expert/dr-analysis --stat

# 통합 상태 확인
git log --graph --oneline --all
```

### 자동화된 상태 보고
- Git hooks를 통한 자동 상태 업데이트
- 진행률 대시보드 생성
- 일일 진행 보고서 자동 생성

---

## 실행 스크립트

### setup-worktrees.sh
전체 워크트리 구조 자동 설정

### sync-experts.sh  
전문가 간 최신 변경사항 동기화

### integrate-phase.sh
단계별 통합 자동화

### quality-check.sh
품질 게이트 자동 검증

---

**작성일**: 2025-01-16  
**버전**: 1.0  
**적용 프로젝트**: 1단 감속기 설계 및 강도/강성 해석 보고서