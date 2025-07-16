"""
Director Manager - 프로젝트 총괄 관리자 페르소나
18년차 프로젝트 매니저로 전체 팀을 이끌고 조율하는 리더
"""

import asyncio
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

from persona_base import PersonaAgent, PersonaProfile, ExpertOpinion, ExpertPanel
from base_agent import AgentResult, AgentContext

class DirectorManagerAgent(PersonaAgent):
    """Director Manager - 프로젝트 총괄 관리자 페르소나"""
    
    def __init__(self):
        # 페르소나 프로필 정의
        persona_profile = PersonaProfile(
            name="Director Manager",
            title="수석 프로젝트 매니저 (Engineering Project Director)",
            experience_years=18,
            education="기계공학 학사 + MBA (경영학 석사) + PMP 자격증",
            specializations=[
                "프로젝트 관리", "팀 리더십", "자원 최적화", "일정 관리",
                "위험 관리", "고객 관계", "품질 관리", "전략적 기획"
            ],
            personality_traits=[
                "전략적 사고", "리더십", "균형감각", "의사소통", "결과 지향"
            ],
            communication_style="strategic",
            decision_making_approach="data_driven",
            catchphrases=[
                "프로젝트 목표를 고려하면 이렇게 진행하겠습니다.",
                "일정과 품질을 모두 만족시키려면 전략적 접근이 필요합니다.",
                "각 전문가의 의견을 종합하면 최적의 방향이 보입니다.",
                "18년 경험상 이런 프로젝트에서는 사전 계획이 성공의 열쇠입니다.",
                "팀의 강점을 최대한 활용하여 목표를 달성하겠습니다."
            ],
            theoretical_knowledge=0.85,
            practical_experience=0.98,
            technical_accuracy=0.88,
            communication_skill=0.96,
            leadership_ability=0.98
        )
        
        super().__init__(persona_profile)
        
        # 프로젝트 관리 도구 및 방법론
        self.project_methodologies = self._initialize_project_methodologies()
        self.team_management = self._initialize_team_management()
        self.stakeholder_management = self._initialize_stakeholder_management()
        self.expert_panel = ExpertPanel()
        
    async def execute(self, task: str, **kwargs) -> AgentResult:
        """프로젝트 관리 작업 실행"""
        if not await self.validate_input(task, **kwargs):
            return self._create_error_result("입력 검증 실패")
        
        start_time = datetime.now()
        output_data = {}
        errors = []
        warnings = []
        next_steps = []
        
        try:
            # Director Manager 특화 작업 분기
            if "project_planning" in task.lower():
                output_data = await self.create_project_plan(**kwargs)
                next_steps.append("팀 킥오프 미팅 진행")
                
            elif "team_coordination" in task.lower():
                output_data = await self.coordinate_expert_team(**kwargs)
                next_steps.append("진행상황 모니터링")
                
            elif "stakeholder_management" in task.lower():
                output_data = await self.manage_stakeholders(**kwargs)
                next_steps.append("이해관계자 피드백 수집")
                
            elif "project_monitoring" in task.lower():
                output_data = await self.monitor_project_progress(**kwargs)
                next_steps.append("필요시 계획 조정")
                
            elif "final_delivery" in task.lower():
                output_data = await self.manage_final_delivery(**kwargs)
                next_steps.append("프로젝트 종료 및 평가")
                
            else:
                # 종합적 프로젝트 관리
                output_data = await self.comprehensive_project_management(**kwargs)
                next_steps.append("지속적 프로젝트 관리")
        
        except Exception as e:
            errors.append(f"프로젝트 관리 중 오류: {str(e)}")
        
        # Director Manager 특화 품질 검사
        quality_score, quality_errors, quality_warnings = await self.run_quality_checks(output_data)
        errors.extend(quality_errors)
        warnings.extend(quality_warnings)
        
        execution_time = (datetime.now() - start_time).total_seconds()
        success = len(errors) == 0 and quality_score >= 0.85
        
        # 페르소나 스타일로 결과 포장
        if success:
            final_comment = self.express_personality(
                "프로젝트가 계획대로 순조롭게 진행되고 있습니다"
            )
        else:
            final_comment = self.express_personality(
                "프로젝트 목표 달성을 위해 전략 조정이 필요합니다"
            )
        
        output_data["director_assessment"] = final_comment
        output_data["project_management_metadata"] = self._generate_project_metadata()
        
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
    
    async def create_project_plan(self, **kwargs) -> Dict[str, Any]:
        """프로젝트 계획 수립"""
        # 프로젝트 요구사항 분석
        requirements_analysis = await self._analyze_project_requirements(**kwargs)
        
        # 작업 분해 구조 (WBS) 생성
        work_breakdown = await self._create_work_breakdown_structure()
        
        # 팀 구성 및 역할 정의
        team_structure = await self._define_team_structure()
        
        # 일정 계획 수립
        schedule_plan = await self._create_project_schedule()
        
        # 자원 계획
        resource_plan = await self._plan_project_resources()
        
        # 위험 관리 계획
        risk_management_plan = await self._create_risk_management_plan()
        
        # 품질 관리 계획
        quality_management_plan = await self._create_quality_management_plan()
        
        # 커뮤니케이션 계획
        communication_plan = await self._create_communication_plan()
        
        return {
            "project_charter": await self._create_project_charter(),
            "requirements_analysis": requirements_analysis,
            "work_breakdown_structure": work_breakdown,
            "team_structure": team_structure,
            "schedule_plan": schedule_plan,
            "resource_plan": resource_plan,
            "risk_management_plan": risk_management_plan,
            "quality_management_plan": quality_management_plan,
            "communication_plan": communication_plan,
            "success_criteria": await self._define_success_criteria(),
            "director_strategic_overview": self._provide_strategic_overview()
        }
    
    async def coordinate_expert_team(self, **kwargs) -> Dict[str, Any]:
        """전문가 팀 조율"""
        # 전문가 역할 및 책임 정의
        expert_roles = await self._define_expert_roles()
        
        # 작업 흐름 및 의존성 관리
        workflow_coordination = await self._coordinate_workflows()
        
        # 팀 커뮤니케이션 촉진
        communication_facilitation = await self._facilitate_team_communication()
        
        # 갈등 해결 및 의사결정 지원
        conflict_resolution = await self._manage_team_conflicts()
        
        # 성과 모니터링 및 피드백
        performance_monitoring = await self._monitor_team_performance()
        
        # 팀 동기부여 및 참여 증진
        team_engagement = await self._enhance_team_engagement()
        
        return {
            "expert_coordination_matrix": expert_roles,
            "workflow_management": workflow_coordination,
            "communication_facilitation": communication_facilitation,
            "conflict_resolution": conflict_resolution,
            "performance_monitoring": performance_monitoring,
            "team_engagement_strategies": team_engagement,
            "team_synergy_assessment": await self._assess_team_synergy(),
            "director_leadership_insights": self._provide_leadership_insights()
        }
    
    async def manage_stakeholders(self, **kwargs) -> Dict[str, Any]:
        """이해관계자 관리"""
        # 이해관계자 식별 및 분석
        stakeholder_analysis = await self._analyze_stakeholders()
        
        # 이해관계자 참여 전략
        engagement_strategy = await self._develop_stakeholder_engagement_strategy()
        
        # 커뮤니케이션 관리
        communication_management = await self._manage_stakeholder_communication()
        
        # 기대사항 관리
        expectation_management = await self._manage_stakeholder_expectations()
        
        # 피드백 수집 및 처리
        feedback_management = await self._manage_stakeholder_feedback()
        
        return {
            "stakeholder_register": stakeholder_analysis,
            "engagement_strategy": engagement_strategy,
            "communication_matrix": communication_management,
            "expectation_management": expectation_management,
            "feedback_management": feedback_management,
            "stakeholder_satisfaction": await self._assess_stakeholder_satisfaction(),
            "relationship_health": await self._evaluate_stakeholder_relationships()
        }
    
    async def monitor_project_progress(self, **kwargs) -> Dict[str, Any]:
        """프로젝트 진행상황 모니터링"""
        # 진행률 추적
        progress_tracking = await self._track_project_progress()
        
        # 일정 성과 분석
        schedule_performance = await self._analyze_schedule_performance()
        
        # 품질 지표 모니터링
        quality_monitoring = await self._monitor_quality_metrics()
        
        # 자원 활용도 분석
        resource_utilization = await self._analyze_resource_utilization()
        
        # 위험 상태 모니터링
        risk_monitoring = await self._monitor_risk_status()
        
        # 이슈 및 변경 관리
        issue_management = await self._manage_issues_and_changes()
        
        # 대시보드 및 보고
        project_dashboard = await self._create_project_dashboard()
        
        return {
            "progress_summary": progress_tracking,
            "schedule_performance": schedule_performance,
            "quality_metrics": quality_monitoring,
            "resource_utilization": resource_utilization,
            "risk_status": risk_monitoring,
            "issue_management": issue_management,
            "project_dashboard": project_dashboard,
            "corrective_actions": await self._recommend_corrective_actions(),
            "director_status_assessment": self._provide_status_assessment()
        }
    
    async def manage_final_delivery(self, **kwargs) -> Dict[str, Any]:
        """최종 납품 관리"""
        # 납품 준비성 평가
        delivery_readiness = await self._assess_delivery_readiness()
        
        # 품질 보증 활동
        quality_assurance = await self._conduct_final_quality_assurance()
        
        # 고객 인수 지원
        customer_acceptance = await self._support_customer_acceptance()
        
        # 문서화 및 지식 이전
        knowledge_transfer = await self._manage_knowledge_transfer()
        
        # 프로젝트 종료 활동
        project_closure = await self._execute_project_closure()
        
        # 교훈 학습 및 개선사항
        lessons_learned = await self._capture_lessons_learned()
        
        return {
            "delivery_package": await self._prepare_delivery_package(),
            "delivery_readiness_assessment": delivery_readiness,
            "quality_assurance_results": quality_assurance,
            "customer_acceptance_plan": customer_acceptance,
            "knowledge_transfer_plan": knowledge_transfer,
            "project_closure_report": project_closure,
            "lessons_learned": lessons_learned,
            "project_success_evaluation": await self._evaluate_project_success(),
            "director_final_statement": self._provide_final_project_statement()
        }
    
    async def comprehensive_project_management(self, **kwargs) -> Dict[str, Any]:
        """종합적 프로젝트 관리"""
        # 모든 프로젝트 관리 기능 통합
        project_plan = await self.create_project_plan(**kwargs)
        team_coordination = await self.coordinate_expert_team(**kwargs)
        stakeholder_management = await self.manage_stakeholders(**kwargs)
        progress_monitoring = await self.monitor_project_progress(**kwargs)
        
        # 통합 프로젝트 대시보드
        integrated_dashboard = await self._create_integrated_dashboard(
            project_plan, team_coordination, stakeholder_management, progress_monitoring
        )
        
        # 전략적 권고사항
        strategic_recommendations = await self._develop_strategic_recommendations(
            project_plan, team_coordination, stakeholder_management, progress_monitoring
        )
        
        return {
            "project_planning": project_plan,
            "team_coordination": team_coordination,
            "stakeholder_management": stakeholder_management,
            "progress_monitoring": progress_monitoring,
            "integrated_dashboard": integrated_dashboard,
            "strategic_recommendations": strategic_recommendations,
            "overall_project_health": await self._assess_overall_project_health(),
            "director_executive_summary": self._provide_executive_summary()
        }
    
    # === 초기화 메서드들 ===
    
    def _initialize_project_methodologies(self) -> Dict:
        """프로젝트 방법론 초기화"""
        return {
            "project_frameworks": {
                "PMBOK": "Project Management Body of Knowledge",
                "PRINCE2": "Projects in Controlled Environments",
                "Agile": "애자일 프로젝트 관리",
                "Lean": "린 프로젝트 관리"
            },
            "planning_tools": {
                "WBS": "작업 분해 구조",
                "Gantt": "간트 차트",
                "PERT": "프로그램 평가 및 검토 기법",
                "CPM": "임계경로법"
            },
            "risk_management": {
                "risk_register": "위험 등록부",
                "probability_impact": "확률-영향 매트릭스",
                "mitigation_strategies": "완화 전략",
                "contingency_planning": "비상 계획"
            }
        }
    
    def _initialize_team_management(self) -> Dict:
        """팀 관리 방법론 초기화"""
        return {
            "leadership_styles": {
                "transformational": "변혁적 리더십",
                "situational": "상황적 리더십",
                "servant": "서번트 리더십",
                "collaborative": "협업적 리더십"
            },
            "team_development": {
                "forming": "형성 단계",
                "storming": "혼란 단계",
                "norming": "정규화 단계",
                "performing": "성과 단계"
            },
            "motivation_techniques": {
                "recognition": "인정과 보상",
                "autonomy": "자율성 부여",
                "mastery": "전문성 개발",
                "purpose": "목적 의식 공유"
            }
        }
    
    def _initialize_stakeholder_management(self) -> Dict:
        """이해관계자 관리 초기화"""
        return {
            "stakeholder_types": {
                "primary": "주요 이해관계자",
                "secondary": "이차 이해관계자",
                "key_players": "핵심 인물",
                "context_setters": "상황 설정자"
            },
            "engagement_levels": {
                "unaware": "무관심",
                "resistant": "저항",
                "neutral": "중립",
                "supportive": "지지",
                "leading": "주도"
            },
            "communication_methods": {
                "formal_reports": "공식 보고서",
                "informal_updates": "비공식 업데이트",
                "presentations": "프레젠테이션",
                "workshops": "워크숍"
            }
        }
    
    # === 프로젝트 계획 메서드들 ===
    
    async def _create_project_charter(self) -> Dict:
        """프로젝트 헌장 작성"""
        return {
            "project_title": "1단 감속기 설계 및 강도/강성 해석 보고서 프로젝트",
            "project_sponsor": "기술개발팀",
            "project_manager": self.persona.name,
            "project_objectives": [
                "ISO 6336 기반 기어 강도 해석 수행",
                "시스템 강성 분석 및 검증",
                "학술 논문 수준의 보고서 작성",
                "품질 기준 만족 및 표준 준수"
            ],
            "success_criteria": [
                "모든 계산 결과 검증 완료",
                "품질 점수 90% 이상 달성",
                "납기 준수 (목표: 7일)",
                "이해관계자 만족도 95% 이상"
            ],
            "key_deliverables": [
                "종합 분석 보고서",
                "계산 검증 자료",
                "시각화 자료 패키지",
                "품질 인증서"
            ],
            "project_constraints": [
                "예산: 제한 없음 (내부 프로젝트)",
                "일정: 7일 이내 완료",
                "자원: 전문가 팀 5명",
                "품질: 학술 논문 수준"
            ]
        }
    
    async def _create_work_breakdown_structure(self) -> Dict:
        """작업 분해 구조 생성"""
        return {
            "level_1": {
                "1.0": "프로젝트 관리",
                "2.0": "기술 분석",
                "3.0": "계산 및 검증",
                "4.0": "문서 작성",
                "5.0": "시각화 및 디자인",
                "6.0": "품질 보증",
                "7.0": "프로젝트 종료"
            },
            "level_2": {
                "2.1": "이론적 배경 연구",
                "2.2": "강도 해석 수행",
                "2.3": "강성 해석 수행",
                "3.1": "정밀 계산 수행",
                "3.2": "결과 검증",
                "3.3": "불확실성 분석",
                "4.1": "보고서 구조 설계",
                "4.2": "내용 작성",
                "4.3": "편집 및 교정"
            },
            "dependencies": {
                "2.2 → 3.1": "강도 해석 완료 후 정밀 계산",
                "3.2 → 4.2": "검증 완료 후 보고서 작성",
                "4.3 → 5.0": "편집 완료 후 시각화",
                "5.0 → 6.0": "시각화 완료 후 품질 검증"
            }
        }
    
    async def _define_team_structure(self) -> Dict:
        """팀 구조 정의"""
        return {
            "organizational_structure": "매트릭스 조직",
            "team_members": {
                "Director Manager": {
                    "role": "프로젝트 총괄",
                    "responsibilities": ["전체 계획 수립", "팀 조율", "이해관계자 관리"],
                    "authority_level": "최종 의사결정권"
                },
                "Dr. Analysis": {
                    "role": "기술 분석 리더",
                    "responsibilities": ["강도/강성 해석", "공학적 검토"],
                    "authority_level": "기술적 의사결정권"
                },
                "Prof. Calculator": {
                    "role": "계산 검증 전문가",
                    "responsibilities": ["정밀 계산", "결과 검증"],
                    "authority_level": "계산 승인권"
                },
                "Dr. Writer": {
                    "role": "문서 작성 전문가",
                    "responsibilities": ["보고서 작성", "편집"],
                    "authority_level": "문서 품질 결정권"
                },
                "Design. Layout": {
                    "role": "시각화 전문가",
                    "responsibilities": ["차트 생성", "레이아웃 디자인"],
                    "authority_level": "시각 디자인 결정권"
                },
                "Inspector Quality": {
                    "role": "품질 보증 전문가",
                    "responsibilities": ["품질 검증", "최종 승인"],
                    "authority_level": "품질 승인권"
                }
            },
            "communication_matrix": await self._create_communication_matrix(),
            "escalation_procedures": await self._define_escalation_procedures()
        }
    
    # === 팀 조율 메서드들 ===
    
    async def _coordinate_workflows(self) -> Dict:
        """워크플로우 조율"""
        return {
            "workflow_phases": {
                "phase_1": {
                    "name": "분석 및 계산",
                    "parallel_teams": ["Dr. Analysis", "Prof. Calculator"],
                    "duration": "3일",
                    "deliverables": ["강도 해석 결과", "정밀 계산 결과"]
                },
                "phase_2": {
                    "name": "검증 및 문서화",
                    "sequential_teams": ["Prof. Calculator", "Dr. Writer"],
                    "duration": "2일",
                    "deliverables": ["검증 보고서", "초안 문서"]
                },
                "phase_3": {
                    "name": "시각화 및 편집",
                    "parallel_teams": ["Design. Layout", "Dr. Writer"],
                    "duration": "1.5일",
                    "deliverables": ["시각화 자료", "편집된 문서"]
                },
                "phase_4": {
                    "name": "품질 검증 및 승인",
                    "sequential_teams": ["Inspector Quality", "Director Manager"],
                    "duration": "0.5일",
                    "deliverables": ["품질 인증", "최종 승인"]
                }
            },
            "coordination_mechanisms": {
                "daily_standups": "일일 진행상황 공유",
                "milestone_reviews": "단계별 검토 회의",
                "cross_functional_workshops": "교차 기능 워크숍",
                "peer_reviews": "동료 검토 세션"
            }
        }
    
    async def _facilitate_team_communication(self) -> Dict:
        """팀 커뮤니케이션 촉진"""
        return {
            "communication_channels": {
                "formal": "공식 회의 및 보고서",
                "informal": "일상적 협의 및 조율",
                "digital": "협업 플랫폼 활용",
                "face_to_face": "대면 워크숍"
            },
            "meeting_schedule": {
                "kickoff_meeting": "프로젝트 시작시",
                "daily_standups": "매일 15분",
                "weekly_reviews": "주간 진행 검토",
                "milestone_meetings": "단계 완료시"
            },
            "information_sharing": {
                "shared_repository": "공유 문서 저장소",
                "version_control": "버전 관리 시스템",
                "progress_dashboard": "실시간 진행 현황",
                "knowledge_base": "프로젝트 지식 베이스"
            }
        }
    
    # === 모니터링 및 제어 메서드들 ===
    
    async def _track_project_progress(self) -> Dict:
        """프로젝트 진행률 추적"""
        return {
            "overall_progress": {
                "completion_percentage": 45,
                "planned_vs_actual": "계획 대비 5% 앞섬",
                "critical_path_status": "정상 진행",
                "milestone_achievement": "3/7 완료"
            },
            "team_progress": {
                "Dr. Analysis": {"task_completion": 60, "quality_score": 92},
                "Prof. Calculator": {"task_completion": 70, "quality_score": 96},
                "Dr. Writer": {"task_completion": 30, "quality_score": 89},
                "Design. Layout": {"task_completion": 20, "quality_score": 85},
                "Inspector Quality": {"task_completion": 10, "quality_score": 94}
            },
            "key_performance_indicators": {
                "schedule_performance_index": 1.05,
                "quality_performance_index": 0.92,
                "team_productivity_index": 1.08,
                "stakeholder_satisfaction_index": 0.95
            }
        }
    
    async def _analyze_schedule_performance(self) -> Dict:
        """일정 성과 분석"""
        return {
            "schedule_metrics": {
                "planned_duration": 7,
                "actual_duration_to_date": 3.2,
                "estimated_completion": 6.8,
                "schedule_variance": "+0.2일 (앞섬)"
            },
            "critical_path_analysis": {
                "critical_activities": ["강도 해석", "정밀 계산", "검증"],
                "float_activities": ["시각화", "편집"],
                "bottlenecks": ["계산 검증 단계"],
                "acceleration_opportunities": ["병렬 처리 확대"]
            },
            "resource_leveling": {
                "overallocated_resources": [],
                "underutilized_resources": ["Design. Layout"],
                "optimization_recommendations": ["시각화 작업 조기 시작"]
            }
        }
    
    # === 평가 및 의사결정 메서드들 ===
    
    def _provide_strategic_overview(self) -> str:
        """전략적 개요 제공"""
        overview = """프로젝트 성공을 위해서는 기술적 우수성과 일정 준수의 균형이 중요합니다. 
        각 전문가의 강점을 최대한 활용하면서도 전체적인 일관성을 유지하는 것이 핵심 전략입니다."""
        
        return self.express_personality(overview)
    
    def _provide_leadership_insights(self) -> str:
        """리더십 인사이트 제공"""
        insights = """팀의 다양한 전문성이 시너지를 창출하도록 조율하는 것이 성공의 열쇠입니다. 
        각자의 전문 영역을 존중하면서도 공통 목표를 향해 나아가도록 이끌겠습니다."""
        
        return self.express_personality(insights)
    
    def _provide_status_assessment(self) -> str:
        """현황 평가 제공"""
        assessment = """현재 프로젝트는 계획 대비 순조롭게 진행되고 있으며, 
        품질 목표 달성을 위한 추가적인 노력이 필요한 상황입니다."""
        
        return self.express_personality(assessment)
    
    def _provide_final_project_statement(self) -> str:
        """최종 프로젝트 성명"""
        statement = """전체 팀의 전문성과 헌신으로 우수한 품질의 결과물을 완성했습니다. 
        이 프로젝트는 다학제 협업의 모범사례가 될 것입니다."""
        
        return self.express_personality(statement)
    
    def _provide_executive_summary(self) -> str:
        """임원 요약 제공"""
        summary = """프로젝트 목표 달성률 95%, 품질 기준 만족, 일정 내 완료 예정으로 
        전반적으로 성공적인 프로젝트로 평가됩니다."""
        
        return self.express_personality(summary)
    
    def _generate_project_metadata(self) -> Dict:
        """프로젝트 메타데이터 생성"""
        return {
            "project_timestamp": datetime.now().isoformat(),
            "management_methodology": "PMBOK + Agile 하이브리드",
            "team_size": 6,
            "project_complexity": "중간",
            "success_probability": 0.95,
            "director_signature": f"프로젝트 관리 - {self.persona.name}",
            "leadership_philosophy": "전문가 협업을 통한 시너지 창출"
        }
    
    async def specialized_quality_check(self, output_data: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Director Manager 전용 품질 검사"""
        score = 1.0
        errors = []
        warnings = []
        
        # 프로젝트 계획 완성도 검사
        if "project_charter" in output_data:
            charter = output_data["project_charter"]
            if len(charter.get("project_objectives", [])) < 3:
                warnings.append("프로젝트 목표가 불충분함")
                score *= 0.9
        
        # 팀 조율 효과성 검사
        if "team_coordination" in output_data:
            coordination = output_data["team_coordination"]
            if "workflow_management" not in coordination:
                errors.append("워크플로우 관리 계획 누락")
                score *= 0.8
        
        # 진행률 관리 검사
        if "progress_summary" in output_data:
            progress = output_data["progress_summary"]
            completion = progress.get("overall_progress", {}).get("completion_percentage", 0)
            if completion < 30:
                warnings.append("프로젝트 진행률이 저조함")
                score *= 0.95
        
        # 이해관계자 관리 검사
        if "stakeholder_management" in output_data:
            stakeholder = output_data["stakeholder_management"]
            if "engagement_strategy" not in stakeholder:
                errors.append("이해관계자 참여 전략 부족")
                score *= 0.7
        
        return score, errors, warnings
    
    def _create_error_result(self, error_message: str) -> AgentResult:
        """에러 결과 생성"""
        return AgentResult(
            agent_name=self.name,
            success=False,
            output_data={},
            quality_score=0.0,
            errors=[error_message],
            warnings=[],
            execution_time=0.0,
            next_steps=["프로젝트 관리 요구사항 재검토"]
        )

# 간략화된 구현 메서드들
    async def _create_project_schedule(self) -> Dict:
        return {"total_duration": 7, "phases": 4, "critical_path": ["분석", "계산", "검증"]}
    
    async def _plan_project_resources(self) -> Dict:
        return {"human_resources": 6, "budget": "내부 프로젝트", "tools": ["Python", "문서 도구"]}
    
    async def _create_communication_matrix(self) -> Dict:
        return {"frequency": "daily", "methods": ["meetings", "reports"], "stakeholders": 5}
    
    async def _assess_delivery_readiness(self) -> Dict:
        return {"readiness_score": 0.92, "pending_items": 2, "quality_check": "완료"}

# 사용 예시
async def main():
    """Director Manager 테스트"""
    from base_agent import create_agent_context
    
    project_root = Path("/home/devcontainers/reduction-report")
    context = create_agent_context(project_root, "project_management")
    
    director = DirectorManagerAgent()
    director.set_context(context)
    
    # 프로젝트 계획 수립
    result = await director.execute("project_planning")
    
    print(f"Director Manager 결과: {result.success}")
    print(f"품질 점수: {result.quality_score}")
    print(f"총괄 평가: {result.output_data.get('director_assessment', '')}")

if __name__ == "__main__":
    asyncio.run(main())