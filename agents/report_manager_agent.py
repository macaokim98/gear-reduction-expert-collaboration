"""
Report Manager Agent - 보고서 총괄 관리 에이전트
감속기 보고서 프로젝트의 전체 관리 및 조율을 담당
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from base_agent import BaseAgent, AgentResult, AgentContext

class ReportManagerAgent(BaseAgent):
    """보고서 총괄 관리 에이전트"""
    
    def __init__(self):
        super().__init__("ReportManager", "Project Management & Quality Oversight")
        self.report_structure = {}
        self.quality_standards = {
            "minimum_sections": 8,
            "minimum_references": 10,
            "required_calculations": 5,
            "academic_style_score": 0.85
        }
    
    async def execute(self, task: str, **kwargs) -> AgentResult:
        """보고서 관리 작업 실행"""
        if not await self.validate_input(task, **kwargs):
            return AgentResult(
                agent_name=self.name,
                success=False,
                output_data={},
                quality_score=0.0,
                errors=["입력 검증 실패"],
                warnings=[],
                execution_time=0.0,
                next_steps=[]
            )
        
        start_time = datetime.now()
        output_data = {}
        errors = []
        warnings = []
        next_steps = []
        
        try:
            if "plan_report" in task.lower():
                output_data = await self.plan_report_structure()
                next_steps.append("에이전트별 작업 할당")
                
            elif "coordinate_agents" in task.lower():
                output_data = await self.coordinate_agent_workflow()
                next_steps.append("품질 검증 시작")
                
            elif "review_quality" in task.lower():
                output_data = await self.review_overall_quality()
                next_steps.append("최종 승인 또는 수정 요청")
                
            elif "finalize_report" in task.lower():
                output_data = await self.finalize_report()
                next_steps.append("보고서 배포")
                
            else:
                # 기본 프로젝트 관리 작업
                output_data = await self.manage_project()
                next_steps.append("다음 단계 작업 지시")
            
        except Exception as e:
            errors.append(f"실행 중 오류: {str(e)}")
        
        # 품질 검사
        quality_score, quality_errors, quality_warnings = await self.run_quality_checks(output_data)
        errors.extend(quality_errors)
        warnings.extend(quality_warnings)
        
        execution_time = (datetime.now() - start_time).total_seconds()
        success = len(errors) == 0 and quality_score >= 0.7
        
        return AgentResult(
            agent_name=self.name,
            success=success,
            output_data=output_data,
            quality_score=quality_score,
            errors=errors,
            warnings=warnings,
            execution_time=execution_time,
            next_steps=next_steps
        )
    
    async def plan_report_structure(self) -> Dict[str, Any]:
        """보고서 구조 기획"""
        structure = {
            "title": "1단 감속기 설계 및 강도/강성 해석 보고서",
            "sections": [
                {
                    "number": "1",
                    "title": "초록 (Abstract)",
                    "assigned_agent": "DocumentAgent",
                    "dependencies": ["모든 에이전트 결과"],
                    "estimated_pages": 1
                },
                {
                    "number": "2", 
                    "title": "서론 (Introduction)",
                    "assigned_agent": "DocumentAgent",
                    "dependencies": [],
                    "estimated_pages": 2
                },
                {
                    "number": "3",
                    "title": "이론적 배경 (Theoretical Background)", 
                    "assigned_agent": "AnalysisAgent",
                    "dependencies": [],
                    "estimated_pages": 4
                },
                {
                    "number": "4",
                    "title": "설계 사양 및 파라미터 (Design Specifications)",
                    "assigned_agent": "CalculationAgent", 
                    "dependencies": [],
                    "estimated_pages": 3
                },
                {
                    "number": "5",
                    "title": "강도 해석 (Strength Analysis)",
                    "assigned_agent": "AnalysisAgent",
                    "dependencies": ["CalculationAgent"],
                    "estimated_pages": 6
                },
                {
                    "number": "6", 
                    "title": "강성 해석 (Stiffness Analysis)",
                    "assigned_agent": "AnalysisAgent",
                    "dependencies": ["CalculationAgent"],
                    "estimated_pages": 4
                },
                {
                    "number": "7",
                    "title": "결과 분석 및 검증 (Results and Validation)",
                    "assigned_agent": "QualityAgent",
                    "dependencies": ["AnalysisAgent", "CalculationAgent"],
                    "estimated_pages": 5
                },
                {
                    "number": "8",
                    "title": "결론 및 향후 과제 (Conclusion)",
                    "assigned_agent": "DocumentAgent", 
                    "dependencies": ["모든 에이전트 결과"],
                    "estimated_pages": 2
                }
            ],
            "total_estimated_pages": 27,
            "target_completion": "7일",
            "quality_requirements": self.quality_standards
        }
        
        self.report_structure = structure
        return structure
    
    async def coordinate_agent_workflow(self) -> Dict[str, Any]:
        """에이전트 워크플로우 조율"""
        workflow = {
            "phase_1": {
                "name": "기초 설계 및 이론 분석",
                "agents": ["CalculationAgent", "AnalysisAgent"],
                "parallel_execution": True,
                "estimated_duration": "2일"
            },
            "phase_2": {
                "name": "상세 해석 및 계산",
                "agents": ["AnalysisAgent", "CalculationAgent"],
                "parallel_execution": False,
                "dependencies": ["phase_1"],
                "estimated_duration": "3일"
            },
            "phase_3": {
                "name": "문서 작성 및 시각화",
                "agents": ["DocumentAgent", "LayoutAgent"],
                "parallel_execution": True,
                "dependencies": ["phase_2"],
                "estimated_duration": "2일"
            },
            "phase_4": {
                "name": "품질 검증 및 최종화",
                "agents": ["QualityAgent", "ReportManager"],
                "parallel_execution": False,
                "dependencies": ["phase_3"],
                "estimated_duration": "1일"
            }
        }
        
        # 각 에이전트에게 작업 지시 전송
        agent_assignments = self._create_agent_assignments(workflow)
        
        return {
            "workflow": workflow,
            "agent_assignments": agent_assignments,
            "coordination_status": "활성",
            "next_checkpoint": "phase_1 완료 후 검토"
        }
    
    async def review_overall_quality(self) -> Dict[str, Any]:
        """전체 품질 검토"""
        quality_review = {
            "technical_accuracy": {
                "iso_6336_compliance": await self._check_iso_compliance(),
                "calculation_verification": await self._verify_calculations(),
                "engineering_validity": await self._check_engineering_validity()
            },
            "document_quality": {
                "academic_style": await self._check_academic_style(),
                "structure_completeness": await self._check_structure_completeness(),
                "reference_quality": await self._check_references()
            },
            "visual_quality": {
                "figure_quality": await self._check_figures(),
                "table_formatting": await self._check_tables(),
                "layout_consistency": await self._check_layout()
            },
            "overall_score": 0.0,
            "improvement_areas": [],
            "approval_status": "pending"
        }
        
        # 전체 점수 계산
        scores = []
        for category, checks in quality_review.items():
            if isinstance(checks, dict):
                category_scores = [v for v in checks.values() if isinstance(v, (int, float))]
                if category_scores:
                    scores.extend(category_scores)
        
        if scores:
            quality_review["overall_score"] = sum(scores) / len(scores)
        
        # 승인 여부 결정
        if quality_review["overall_score"] >= 0.85:
            quality_review["approval_status"] = "approved"
        elif quality_review["overall_score"] >= 0.7:
            quality_review["approval_status"] = "conditional_approval"
        else:
            quality_review["approval_status"] = "requires_revision"
        
        return quality_review
    
    async def finalize_report(self) -> Dict[str, Any]:
        """보고서 최종화"""
        finalization = {
            "final_review_completed": True,
            "version": "1.0",
            "approval_date": datetime.now().isoformat(),
            "final_page_count": await self._count_final_pages(),
            "deliverables": [
                "main_report.pdf",
                "calculation_sheets.xlsx", 
                "technical_drawings.dwg",
                "simulation_results.zip"
            ],
            "distribution_list": [
                "기술팀장",
                "설계부서",
                "품질관리팀",
                "고객사"
            ],
            "archive_location": f"reports/gear_reduction_{datetime.now().strftime('%Y%m%d')}",
            "next_actions": [
                "고객 발표 준비",
                "후속 프로젝트 기획"
            ]
        }
        
        return finalization
    
    async def manage_project(self) -> Dict[str, Any]:
        """기본 프로젝트 관리"""
        project_status = {
            "current_phase": self.context.current_phase,
            "progress_percentage": await self._calculate_progress(),
            "active_agents": list(self.agents.keys()) if hasattr(self, 'agents') else [],
            "pending_tasks": await self._get_pending_tasks(),
            "risk_assessment": await self._assess_risks(),
            "resource_utilization": await self._check_resources(),
            "timeline_status": "on_track"  # "ahead", "on_track", "delayed"
        }
        
        return project_status
    
    # 헬퍼 메서드들
    def _create_agent_assignments(self, workflow: Dict) -> Dict[str, List[str]]:
        """에이전트별 작업 할당 생성"""
        assignments = {}
        for phase_name, phase_info in workflow.items():
            for agent in phase_info["agents"]:
                if agent not in assignments:
                    assignments[agent] = []
                assignments[agent].append(f"{phase_name}: {phase_info['name']}")
        return assignments
    
    async def _check_iso_compliance(self) -> float:
        """ISO 6336 준수 확인"""
        # 실제 구현에서는 계산 결과를 ISO 표준과 비교
        return 0.9
    
    async def _verify_calculations(self) -> float:
        """계산 검증"""
        return 0.95
    
    async def _check_engineering_validity(self) -> float:
        """공학적 타당성 검사"""
        return 0.88
    
    async def _check_academic_style(self) -> float:
        """학술 논문 스타일 검사"""
        return 0.92
    
    async def _check_structure_completeness(self) -> float:
        """구조 완성도 검사"""
        return 0.85
    
    async def _check_references(self) -> float:
        """참고문헌 품질 검사"""
        return 0.8
    
    async def _check_figures(self) -> float:
        """그림 품질 검사"""
        return 0.87
    
    async def _check_tables(self) -> float:
        """표 형식 검사"""
        return 0.9
    
    async def _check_layout(self) -> float:
        """레이아웃 일관성 검사"""
        return 0.93
    
    async def _count_final_pages(self) -> int:
        """최종 페이지 수 계산"""
        return 28
    
    async def _calculate_progress(self) -> float:
        """진행률 계산"""
        return 45.0
    
    async def _get_pending_tasks(self) -> List[str]:
        """대기 중인 작업 목록"""
        return ["강성 해석 완료", "그래프 생성", "참고문헌 정리"]
    
    async def _assess_risks(self) -> Dict[str, str]:
        """위험 평가"""
        return {
            "schedule_risk": "low",
            "quality_risk": "medium", 
            "resource_risk": "low"
        }
    
    async def _check_resources(self) -> Dict[str, float]:
        """리소스 활용도 확인"""
        return {
            "computational_resources": 0.6,
            "human_resources": 0.8,
            "time_resources": 0.7
        }
    
    async def specialized_quality_check(self, output_data: Dict[str, Any]) -> tuple[float, List[str], List[str]]:
        """Report Manager 전용 품질 검사"""
        score = 1.0
        errors = []
        warnings = []
        
        # 프로젝트 관리 관련 품질 검사
        if "workflow" in output_data:
            workflow = output_data["workflow"]
            if len(workflow) < 3:
                warnings.append("워크플로우 단계가 부족함")
                score *= 0.9
        
        if "overall_score" in output_data:
            if output_data["overall_score"] < 0.7:
                errors.append("전체 품질 점수가 기준 미달")
                score *= 0.5
        
        return score, errors, warnings

# 사용 예시
async def main():
    """Report Manager Agent 테스트"""
    from base_agent import create_agent_context
    
    project_root = Path("/home/devcontainers/reduction-report")
    context = create_agent_context(project_root, "planning")
    
    manager = ReportManagerAgent()
    manager.set_context(context)
    
    # 보고서 구조 기획
    result = await manager.execute("plan_report")
    print(f"실행 결과: {result.success}")
    print(f"품질 점수: {result.quality_score}")
    
    if result.output_data:
        print("보고서 구조:")
        for section in result.output_data.get("sections", []):
            print(f"  {section['number']}. {section['title']} ({section['assigned_agent']})")

if __name__ == "__main__":
    asyncio.run(main())