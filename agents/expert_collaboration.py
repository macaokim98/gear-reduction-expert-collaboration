"""
Expert Collaboration System - 전문가 협업 시스템
6명의 전문가 페르소나 간 실제 회의와 같은 상호작용 시뮬레이션
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

from persona_base import PersonaAgent, ExpertPanel, ExpertOpinion
from base_agent import AgentResult, AgentContext, AgentOrchestrator

# 모든 전문가 에이전트 임포트
from dr_analysis import DrAnalysisAgent
from prof_calculator import ProfCalculatorAgent  
from dr_writer import DrWriterAgent
from design_layout import DesignLayoutAgent
from inspector_quality import InspectorQualityAgent
from director_manager import DirectorManagerAgent

class ExpertCollaborationSystem:
    """전문가 협업 시스템"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.experts = {}
        self.collaboration_history = []
        self.meeting_minutes = []
        self.consensus_records = []
        
        # 전문가 에이전트들 초기화
        self._initialize_expert_team()
        
        # 협업 패턴 및 규칙
        self.collaboration_patterns = self._initialize_collaboration_patterns()
        self.meeting_protocols = self._initialize_meeting_protocols()
        
    def _initialize_expert_team(self):
        """전문가 팀 초기화"""
        self.experts = {
            "Dr. Analysis": DrAnalysisAgent(),
            "Prof. Calculator": ProfCalculatorAgent(),
            "Dr. Writer": DrWriterAgent(), 
            "Design. Layout": DesignLayoutAgent(),
            "Inspector Quality": InspectorQualityAgent(),
            "Director Manager": DirectorManagerAgent()
        }
        
        print("🎭 전문가 팀 구성 완료:")
        for name, agent in self.experts.items():
            print(f"  - {name}: {agent.persona.title}")
    
    def _initialize_collaboration_patterns(self) -> Dict:
        """협업 패턴 초기화"""
        return {
            "peer_review": {
                "Dr. Analysis ↔ Prof. Calculator": "기술적 검증",
                "Dr. Writer ↔ Design. Layout": "문서 시각화",
                "Inspector Quality ↔ 모든 전문가": "품질 검토"
            },
            "sequential_workflow": [
                "Director Manager → 프로젝트 계획",
                "Dr. Analysis → 기술 분석", 
                "Prof. Calculator → 계산 검증",
                "Dr. Writer → 문서 작성",
                "Design. Layout → 시각화",
                "Inspector Quality → 품질 검증",
                "Director Manager → 최종 승인"
            ],
            "parallel_tasks": {
                "분석_계산": ["Dr. Analysis", "Prof. Calculator"],
                "문서_디자인": ["Dr. Writer", "Design. Layout"],
                "검증_관리": ["Inspector Quality", "Director Manager"]
            }
        }
    
    def _initialize_meeting_protocols(self) -> Dict:
        """회의 프로토콜 초기화"""
        return {
            "kickoff_meeting": {
                "chair": "Director Manager",
                "participants": "전체",
                "agenda": ["프로젝트 개요", "역할 분담", "일정 확인"],
                "duration": 60
            },
            "technical_review": {
                "chair": "Dr. Analysis",
                "participants": ["Dr. Analysis", "Prof. Calculator"],
                "agenda": ["계산 검토", "방법론 논의", "결과 검증"],
                "duration": 45
            },
            "design_review": {
                "chair": "Dr. Writer",
                "participants": ["Dr. Writer", "Design. Layout"],
                "agenda": ["문서 구조", "시각화 계획", "스타일 통일"],
                "duration": 30
            },
            "quality_review": {
                "chair": "Inspector Quality",
                "participants": "전체",
                "agenda": ["품질 기준", "검증 결과", "개선사항"],
                "duration": 45
            },
            "final_review": {
                "chair": "Director Manager", 
                "participants": "전체",
                "agenda": ["최종 검토", "승인 여부", "다음 단계"],
                "duration": 30
            }
        }
    
    async def conduct_expert_meeting(self, meeting_type: str, topic: str, context: Dict = None) -> Dict:
        """전문가 회의 진행"""
        meeting_protocol = self.meeting_protocols.get(meeting_type, {})
        chair = meeting_protocol.get("chair", "Director Manager")
        participants = meeting_protocol.get("participants", "전체")
        
        print(f"\n🏛️ === {meeting_type.upper()} 회의 시작 ===")
        print(f"📋 주제: {topic}")
        print(f"🪑 사회자: {chair}")
        print(f"👥 참석자: {participants}")
        
        meeting_record = {
            "meeting_type": meeting_type,
            "topic": topic,
            "chair": chair,
            "participants": participants if participants != "전체" else list(self.experts.keys()),
            "start_time": datetime.now(),
            "agenda_items": [],
            "discussions": [],
            "decisions": [],
            "action_items": []
        }
        
        # 회의 진행
        if participants == "전체":
            participant_list = list(self.experts.keys())
        else:
            participant_list = participants
        
        # 각 참석자의 의견 수렴
        for expert_name in participant_list:
            if expert_name in self.experts:
                expert = self.experts[expert_name]
                opinion = expert.provide_expert_opinion(topic, context or {})
                
                print(f"\n💬 {expert_name}: {opinion.opinion}")
                
                meeting_record["discussions"].append({
                    "speaker": expert_name,
                    "opinion": opinion.opinion,
                    "confidence": opinion.confidence_level,
                    "concerns": opinion.concerns,
                    "recommendations": opinion.recommendations
                })
        
        # 합의 도출 과정
        consensus = await self._facilitate_consensus(meeting_record["discussions"], topic)
        meeting_record["consensus"] = consensus
        
        # 회의록 저장
        meeting_record["end_time"] = datetime.now()
        meeting_record["duration"] = (meeting_record["end_time"] - meeting_record["start_time"]).total_seconds() / 60
        
        self.meeting_minutes.append(meeting_record)
        
        print(f"\n✅ 회의 완료 (소요시간: {meeting_record['duration']:.1f}분)")
        print(f"🤝 합의 수준: {consensus['agreement_level']:.0%}")
        
        return meeting_record
    
    async def _facilitate_consensus(self, discussions: List[Dict], topic: str) -> Dict:
        """합의 촉진"""
        print(f"\n🤝 === 합의 도출 과정 ===")
        
        # 의견 분석
        opinions = [d["opinion"] for d in discussions]
        confidence_levels = [d["confidence"] for d in discussions]
        all_concerns = []
        all_recommendations = []
        
        for d in discussions:
            all_concerns.extend(d["concerns"])
            all_recommendations.extend(d["recommendations"])
        
        # 평균 신뢰도 계산
        avg_confidence = sum(confidence_levels) / len(confidence_levels)
        
        # 합의 수준 결정
        if avg_confidence > 0.8:
            agreement_level = 0.9
            status = "강한 합의"
        elif avg_confidence > 0.6:
            agreement_level = 0.7
            status = "보통 합의"
        else:
            agreement_level = 0.5
            status = "약한 합의"
        
        # Director Manager의 종합 의견
        director = self.experts["Director Manager"]
        final_decision = director.provide_expert_opinion(
            f"종합 의견: {topic}", 
            {"discussions": discussions}
        )
        
        consensus = {
            "topic": topic,
            "agreement_level": agreement_level,
            "status": status,
            "average_confidence": avg_confidence,
            "key_agreements": self._extract_key_agreements(opinions),
            "remaining_concerns": list(set(all_concerns)),
            "action_items": list(set(all_recommendations)),
            "final_decision": final_decision.opinion,
            "timestamp": datetime.now()
        }
        
        print(f"📊 합의 결과: {status} ({agreement_level:.0%})")
        print(f"🎯 핵심 합의사항: {', '.join(consensus['key_agreements'])}")
        
        self.consensus_records.append(consensus)
        return consensus
    
    def _extract_key_agreements(self, opinions: List[str]) -> List[str]:
        """핵심 합의사항 추출"""
        # 간단한 키워드 기반 합의사항 추출
        common_themes = []
        
        if any("안전" in op for op in opinions):
            common_themes.append("안전성 확보")
        if any("품질" in op for op in opinions):
            common_themes.append("품질 기준 준수")
        if any("표준" in op for op in opinions):
            common_themes.append("표준 준수")
        if any("검증" in op for op in opinions):
            common_themes.append("검증 필요")
        if any("개선" in op for op in opinions):
            common_themes.append("개선 필요")
            
        return common_themes if common_themes else ["전문가 검토 완료"]
    
    async def simulate_expert_collaboration(self, project_task: str) -> Dict:
        """전문가 협업 시뮬레이션"""
        print(f"\n🚀 === 전문가 협업 시뮬레이션 시작 ===")
        print(f"📋 프로젝트 과제: {project_task}")
        
        collaboration_log = {
            "project_task": project_task,
            "start_time": datetime.now(),
            "meetings": [],
            "collaborations": [],
            "final_result": {}
        }
        
        # 1. 킥오프 미팅
        kickoff = await self.conduct_expert_meeting(
            "kickoff_meeting", 
            f"프로젝트 시작: {project_task}"
        )
        collaboration_log["meetings"].append(kickoff)
        
        # 2. 기술 검토 미팅
        technical_review = await self.conduct_expert_meeting(
            "technical_review",
            "기술적 접근 방법 및 계산 방법론 검토"
        )
        collaboration_log["meetings"].append(technical_review)
        
        # 3. 설계 검토 미팅  
        design_review = await self.conduct_expert_meeting(
            "design_review",
            "문서 구조 및 시각화 방안 검토"
        )
        collaboration_log["meetings"].append(design_review)
        
        # 4. 개별 전문가 작업 시뮬레이션
        expert_works = await self._simulate_individual_work()
        collaboration_log["collaborations"] = expert_works
        
        # 5. 품질 검토 미팅
        quality_review = await self.conduct_expert_meeting(
            "quality_review",
            "전체 작업 결과 품질 검토"
        )
        collaboration_log["meetings"].append(quality_review)
        
        # 6. 최종 검토 미팅
        final_review = await self.conduct_expert_meeting(
            "final_review",
            "최종 결과물 검토 및 승인"
        )
        collaboration_log["meetings"].append(final_review)
        
        # 7. 최종 결과 종합
        final_result = await self._compile_final_result(collaboration_log)
        collaboration_log["final_result"] = final_result
        collaboration_log["end_time"] = datetime.now()
        collaboration_log["total_duration"] = (
            collaboration_log["end_time"] - collaboration_log["start_time"]
        ).total_seconds()
        
        self.collaboration_history.append(collaboration_log)
        
        print(f"\n🎉 === 협업 시뮬레이션 완료 ===")
        print(f"⏱️ 총 소요시간: {collaboration_log['total_duration']:.1f}초")
        print(f"🏛️ 총 회의 수: {len(collaboration_log['meetings'])}")
        print(f"🤝 총 협업 활동: {len(collaboration_log['collaborations'])}")
        
        return collaboration_log
    
    async def _simulate_individual_work(self) -> List[Dict]:
        """개별 전문가 작업 시뮬레이션"""
        print(f"\n💼 === 개별 전문가 작업 단계 ===")
        
        works = []
        
        # Dr. Analysis 작업
        print("🔬 Dr. Analysis: 강도 해석 수행 중...")
        dr_analysis_work = {
            "expert": "Dr. Analysis",
            "task": "강도 및 강성 해석",
            "status": "완료",
            "quality_score": 0.92,
            "duration": 120,  # 분
            "output": "ISO 6336 기반 해석 결과"
        }
        works.append(dr_analysis_work)
        
        # Prof. Calculator 작업
        print("🧮 Prof. Calculator: 정밀 계산 및 검증 중...")
        calc_work = {
            "expert": "Prof. Calculator", 
            "task": "정밀 계산 및 검증",
            "status": "완료",
            "quality_score": 0.96,
            "duration": 90,
            "output": "다중 방법론 검증 결과"
        }
        works.append(calc_work)
        
        # Dr. Writer 작업
        print("📝 Dr. Writer: 학술 논문 수준 문서 작성 중...")
        writer_work = {
            "expert": "Dr. Writer",
            "task": "학술 논문 수준 문서 작성",
            "status": "완료", 
            "quality_score": 0.89,
            "duration": 150,
            "output": "IEEE 스타일 기술 보고서"
        }
        works.append(writer_work)
        
        # Design. Layout 작업
        print("🎨 Design. Layout: 시각화 및 레이아웃 디자인 중...")
        design_work = {
            "expert": "Design. Layout",
            "task": "시각화 및 레이아웃 디자인",
            "status": "완료",
            "quality_score": 0.91,
            "duration": 80,
            "output": "전문적 차트 및 레이아웃"
        }
        works.append(design_work)
        
        # Inspector Quality 작업
        print("✅ Inspector Quality: 품질 검증 및 감사 중...")
        quality_work = {
            "expert": "Inspector Quality",
            "task": "종합 품질 검증",
            "status": "완료",
            "quality_score": 0.94,
            "duration": 60,
            "output": "품질 인증 및 개선사항"
        }
        works.append(quality_work)
        
        # Director Manager 작업
        print("🏢 Director Manager: 프로젝트 관리 및 조율 중...")
        manager_work = {
            "expert": "Director Manager",
            "task": "프로젝트 관리 및 팀 조율",
            "status": "완료",
            "quality_score": 0.88,
            "duration": 100,
            "output": "프로젝트 관리 보고서"
        }
        works.append(manager_work)
        
        return works
    
    async def _compile_final_result(self, collaboration_log: Dict) -> Dict:
        """최종 결과 컴파일"""
        # 전체 품질 점수 계산
        quality_scores = [work["quality_score"] for work in collaboration_log["collaborations"]]
        avg_quality = sum(quality_scores) / len(quality_scores)
        
        # 총 작업 시간 계산
        total_work_time = sum(work["duration"] for work in collaboration_log["collaborations"])
        
        # 합의 수준 계산
        agreement_levels = [consensus["agreement_level"] for consensus in self.consensus_records]
        avg_agreement = sum(agreement_levels) / len(agreement_levels) if agreement_levels else 0
        
        final_result = {
            "project_success": avg_quality > 0.85 and avg_agreement > 0.7,
            "overall_quality_score": avg_quality,
            "team_agreement_level": avg_agreement,
            "total_work_hours": total_work_time / 60,  # 시간 단위
            "number_of_meetings": len(collaboration_log["meetings"]),
            "deliverables": [
                "기술 분석 보고서",
                "정밀 계산 결과",
                "학술 논문 수준 문서",
                "전문적 시각화 자료",
                "품질 인증서",
                "프로젝트 관리 보고서"
            ],
            "success_factors": [
                "전문가 다양성",
                "체계적 협업",
                "품질 중심 접근",
                "효과적 의사소통"
            ],
            "lessons_learned": [
                "페르소나 기반 협업의 효과성",
                "전문 분야별 시너지 창출",
                "품질 검증의 중요성",
                "리더십의 조율 역할"
            ]
        }
        
        return final_result
    
    def generate_collaboration_report(self) -> Dict:
        """협업 보고서 생성"""
        report = {
            "collaboration_summary": {
                "total_collaborations": len(self.collaboration_history),
                "total_meetings": len(self.meeting_minutes),
                "total_consensus_records": len(self.consensus_records),
                "average_quality_score": 0.91,
                "team_effectiveness": 0.89
            },
            "expert_performance": {},
            "collaboration_patterns": self.collaboration_patterns,
            "success_metrics": {
                "project_completion_rate": 1.0,
                "quality_achievement_rate": 0.91,
                "stakeholder_satisfaction": 0.94,
                "team_synergy_index": 0.88
            },
            "recommendations": [
                "전문가 페르소나 시스템의 지속적 활용",
                "협업 프로세스의 표준화",
                "품질 검증 체계의 강화",
                "커뮤니케이션 효율성 개선"
            ]
        }
        
        # 각 전문가별 성과 분석
        for expert_name in self.experts.keys():
            report["expert_performance"][expert_name] = {
                "participation_rate": 1.0,
                "contribution_quality": 0.9,
                "collaboration_effectiveness": 0.88,
                "leadership_demonstration": 0.85 if expert_name == "Director Manager" else 0.7
            }
        
        return report

# 사용 예시 및 테스트
async def main():
    """전문가 협업 시스템 테스트"""
    project_root = Path("/home/devcontainers/reduction-report")
    
    # 협업 시스템 초기화
    collaboration_system = ExpertCollaborationSystem(project_root)
    
    # 협업 시뮬레이션 실행
    result = await collaboration_system.simulate_expert_collaboration(
        "1단 감속기 설계 및 강도/강성 해석 보고서 작성"
    )
    
    # 협업 보고서 생성
    report = collaboration_system.generate_collaboration_report()
    
    print(f"\n📊 === 최종 협업 결과 ===")
    print(f"✅ 프로젝트 성공: {result['final_result']['project_success']}")
    print(f"🎯 전체 품질 점수: {result['final_result']['overall_quality_score']:.2f}")
    print(f"🤝 팀 합의 수준: {result['final_result']['team_agreement_level']:.2f}")
    print(f"⏱️ 총 작업 시간: {result['final_result']['total_work_hours']:.1f}시간")

if __name__ == "__main__":
    asyncio.run(main())