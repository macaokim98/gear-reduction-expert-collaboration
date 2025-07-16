#!/bin/bash

# Git Worktree 상태 모니터링 및 보고서 생성
# 전문가 팀 진행 상황을 실시간으로 추적

set -e

echo "📊 Git Worktree 전문가 협업 상태 보고서"
echo "생성 시간: $(date)"
echo "============================================="

# 전체 워크트리 상태
echo ""
echo "🌳 워크트리 현황"
echo "----------------"
git worktree list | while read line; do
    path=$(echo "$line" | awk '{print $1}')
    branch=$(echo "$line" | awk '{print $2}' | tr -d '[]')
    
    if [ -d "$path" ]; then
        cd "$path"
        commits=$(git rev-list --count HEAD ^main 2>/dev/null || echo "0")
        last_commit=$(git log -1 --format="%h %s" 2>/dev/null || echo "No commits")
        
        echo "📁 $path"
        echo "   브랜치: $branch"
        echo "   커밋수: $commits"
        echo "   최신: $last_commit"
        echo ""
        cd - > /dev/null
    fi
done

# 전문가별 진행률 계산
echo ""
echo "👥 전문가별 진행 상황"
echo "-------------------"

experts=(
    "dr-analysis:Dr. Analysis:🔬"
    "prof-calculator:Prof. Calculator:🧮"
    "dr-writer:Dr. Writer:📝"
    "design-layout:Design Layout:🎨"
    "inspector-quality:Inspector Quality:✅"
    "director-manager:Director Manager:🏢"
)

total_progress=0
expert_count=0

for expert_info in "${experts[@]}"; do
    IFS=':' read -r expert_name expert_title expert_icon <<< "$expert_info"
    worktree_path="worktrees/$expert_name"
    
    if [ -d "$worktree_path" ]; then
        cd "$worktree_path"
        
        # 진행률 계산 (커밋 수, 파일 수, README 체크리스트 기반)
        commits=$(git rev-list --count HEAD ^main 2>/dev/null || echo "0")
        files=$(find . -name "*.md" -o -name "*.py" -o -name "*.txt" | wc -l)
        
        # README의 체크리스트 진행률 계산
        if [ -f "README.md" ]; then
            total_tasks=$(grep -c "- \[ \]" README.md 2>/dev/null || echo "0")
            completed_tasks=$(grep -c "- \[x\]" README.md 2>/dev/null || echo "0")
            if [ "$total_tasks" -gt 0 ]; then
                checklist_progress=$((completed_tasks * 100 / total_tasks))
            else
                checklist_progress=0
            fi
        else
            checklist_progress=0
        fi
        
        # 종합 진행률 (가중 평균)
        # 커밋수(40%) + 파일수(30%) + 체크리스트(30%)
        commit_score=$((commits > 5 ? 100 : commits * 20))
        file_score=$((files > 10 ? 100 : files * 10))
        
        overall_progress=$(((commit_score * 40 + file_score * 30 + checklist_progress * 30) / 100))
        
        # 진행률 바 생성
        progress_bar=""
        filled=$((overall_progress / 10))
        empty=$((10 - filled))
        
        for ((i=1; i<=filled; i++)); do
            progress_bar+="█"
        done
        for ((i=1; i<=empty; i++)); do
            progress_bar+="░"
        done
        
        # 상태 판정
        if [ $overall_progress -ge 90 ]; then
            status="✅ 완료"
        elif [ $overall_progress -ge 70 ]; then
            status="🔄 진행중"
        elif [ $overall_progress -ge 30 ]; then
            status="🟡 시작됨"
        else
            status="⚪ 대기중"
        fi
        
        echo "$expert_icon $expert_title"
        echo "   진행률: [$progress_bar] $overall_progress% $status"
        echo "   활동: 커밋 $commits개, 파일 $files개, 완료 작업 $completed_tasks/$total_tasks"
        
        # 최근 활동
        if [ $commits -gt 0 ]; then
            last_activity=$(git log -1 --format="%cr" 2>/dev/null || echo "No activity")
            echo "   최근: $last_activity"
        fi
        
        echo ""
        
        total_progress=$((total_progress + overall_progress))
        expert_count=$((expert_count + 1))
        
        cd - > /dev/null
    else
        echo "$expert_icon $expert_title"
        echo "   상태: ❌ 워크트리 없음"
        echo ""
    fi
done

# 전체 프로젝트 진행률
if [ $expert_count -gt 0 ]; then
    project_progress=$((total_progress / expert_count))
    echo "🎯 전체 프로젝트 진행률: $project_progress%"
    
    # 프로젝트 단계 판정
    if [ $project_progress -ge 90 ]; then
        project_phase="🚀 릴리즈 준비"
    elif [ $project_progress -ge 70 ]; then
        project_phase="🔄 통합 단계"
    elif [ $project_progress -ge 40 ]; then
        project_phase="⚙️ 개발 단계"
    else
        project_phase="🌱 초기 단계"
    fi
    
    echo "📈 현재 단계: $project_phase"
fi

echo ""

# 통합 상태 확인
echo "🔄 통합 상태"
echo "------------"

integration_phases=(
    "phase-1:Phase 1 (분석+계산)"
    "phase-2:Phase 2 (문서+디자인)"
    "phase-3:Phase 3 (품질검증)"
)

for phase_info in "${integration_phases[@]}"; do
    IFS=':' read -r phase_name phase_desc <<< "$phase_info"
    branch_name="integration/$phase_name"
    worktree_path="worktrees/integration-$phase_name"
    
    if git show-ref --verify --quiet refs/heads/$branch_name; then
        if [ -d "$worktree_path" ]; then
            cd "$worktree_path"
            commits=$(git rev-list --count HEAD ^main 2>/dev/null || echo "0")
            
            if [ $commits -gt 0 ]; then
                echo "✅ $phase_desc: 완료 ($commits commits)"
                last_integration=$(git log -1 --format="%cr" 2>/dev/null)
                echo "   최근 통합: $last_integration"
            else
                echo "⚪ $phase_desc: 대기중"
            fi
            cd - > /dev/null
        else
            echo "⚠️  $phase_desc: 워크트리 없음"
        fi
    else
        echo "⚪ $phase_desc: 브랜치 없음"
    fi
done

# 최종 릴리즈 상태
if git show-ref --verify --quiet refs/heads/release/final-report; then
    if [ -d "worktrees/final-release" ]; then
        cd "worktrees/final-release"
        commits=$(git rev-list --count HEAD ^main 2>/dev/null || echo "0")
        
        if [ $commits -gt 0 ]; then
            echo "🚀 최종 릴리즈: 완료"
            release_time=$(git log -1 --format="%cr" 2>/dev/null)
            echo "   릴리즈: $release_time"
        else
            echo "⚪ 최종 릴리즈: 대기중"
        fi
        cd - > /dev/null
    else
        echo "⚠️  최종 릴리즈: 워크트리 없음"
    fi
else
    echo "⚪ 최종 릴리즈: 브랜치 없음"
fi

echo ""

# 품질 지표
echo "📋 품질 지표"
echo "------------"

# README 완성도 체크
readme_files=$(find worktrees -name "README.md" | wc -l)
echo "📄 README 파일: $readme_files개"

# 전체 커밋 활동
total_commits=$(git rev-list --count --all 2>/dev/null || echo "0")
echo "📝 총 커밋수: $total_commits개"

# 브랜치 상태
active_branches=$(git branch -a | grep -v "main" | wc -l)
echo "🌳 활성 브랜치: $active_branches개"

# 파일 통계
total_files=$(find . -name "*.md" -o -name "*.py" -o -name "*.sh" | grep -v ".git" | wc -l)
echo "📁 프로젝트 파일: $total_files개"

echo ""

# 다음 권장 액션
echo "🎯 권장 액션"
echo "------------"

if [ $project_progress -lt 30 ]; then
    echo "1. 각 전문가 워크트리에서 작업 시작"
    echo "2. 기본 템플릿 및 구조 완성"
    echo "3. 정기 커밋 및 진행 상황 업데이트"
elif [ $project_progress -lt 70 ]; then
    echo "1. 전문가별 핵심 작업 완료"
    echo "2. 단계별 통합 준비"
    echo "3. 1차 통합 실행: ./git-workflow/integrate-phase.sh phase-1"
elif [ $project_progress -lt 90 ]; then
    echo "1. 통합 단계 진행"
    echo "2. 품질 검증 수행"
    echo "3. 최종 통합: ./git-workflow/integrate-phase.sh final"
else
    echo "1. 최종 릴리즈 확인"
    echo "2. 문서 패키징"
    echo "3. 프로젝트 완료 선언"
fi

echo ""

# 잠재적 이슈 확인
echo "⚠️  잠재적 이슈"
echo "---------------"

issues_found=false

# 장기간 업데이트 없는 브랜치 확인
for expert_info in "${experts[@]}"; do
    IFS=':' read -r expert_name expert_title expert_icon <<< "$expert_info"
    worktree_path="worktrees/$expert_name"
    
    if [ -d "$worktree_path" ]; then
        cd "$worktree_path"
        
        # 최근 커밋이 48시간 이상 전인지 확인
        if git log -1 --format="%ct" 2>/dev/null >/dev/null; then
            last_commit_time=$(git log -1 --format="%ct" 2>/dev/null)
            current_time=$(date +%s)
            hours_since=$((( current_time - last_commit_time ) / 3600))
            
            if [ $hours_since -gt 48 ]; then
                echo "🟡 $expert_title: $((hours_since / 24))일 전 마지막 활동"
                issues_found=true
            fi
        fi
        
        cd - > /dev/null
    fi
done

# 빈 워크트리 확인
for expert_info in "${experts[@]}"; do
    IFS=':' read -r expert_name expert_title expert_icon <<< "$expert_info"
    worktree_path="worktrees/$expert_name"
    
    if [ ! -d "$worktree_path" ]; then
        echo "❌ $expert_title: 워크트리가 생성되지 않음"
        issues_found=true
    fi
done

if [ "$issues_found" = false ]; then
    echo "✅ 발견된 이슈 없음"
fi

echo ""
echo "============================================="
echo "보고서 생성 완료: $(date)"
echo ""
echo "💡 실시간 모니터링: watch -n 30 './git-workflow/status-report.sh'"
echo "🔄 자동 새로고침: ./git-workflow/status-report.sh > status.html"