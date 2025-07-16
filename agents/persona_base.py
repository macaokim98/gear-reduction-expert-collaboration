"""
Persona-Based Agent System for Expert Collaboration
전문가 페르소나 기반 에이전트 시스템
"""

import asyncio
import json
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from base_agent import BaseAgent, AgentResult, AgentContext

@dataclass
class PersonaProfile:
    """전문가 페르소나 프로필"""
    name: str
    title: str
    experience_years: int
    education: str
    specializations: List[str]
    personality_traits: List[str]
    communication_style: str
    decision_making_approach: str
    catchphrases: List[str]
    
    # 전문성 수준 (0.0 ~ 1.0)
    theoretical_knowledge: float
    practical_experience: float
    technical_accuracy: float
    communication_skill: float
    leadership_ability: float

@dataclass
class ExpertOpinion:
    """전문가 의견"""
    persona_name: str
    topic: str
    opinion: str
    confidence_level: float  # 0.0 ~ 1.0
    supporting_evidence: List[str]
    concerns: List[str]
    recommendations: List[str]
    timestamp: datetime = datetime.now()

class PersonaAgent(BaseAgent):
    """페르소나 기반 전문가 에이전트"""
    
    def __init__(self, persona_profile: PersonaProfile):
        super().__init__(persona_profile.name, persona_profile.title)
        self.persona = persona_profile
        self.expert_opinions: List[ExpertOpinion] = []
        self.collaboration_history: List[Dict] = []
        
    def express_personality(self, base_response: str) -> str:
        """페르소나 특성을 반영한 응답 생성"""
        personality_modifiers = {
            "conservative": ["신중하게 검토한 결과", "안전을 고려하면", "보수적 접근으로"],
            "perfectionist": ["정확한 계산을 위해", "완벽을 기하자면", "오차를 최소화하려면"],
            "collaborative": ["팀 전체를 고려하면", "다른 전문가와 협의하여", "통합적 관점에서"],
            "detail_oriented": ["세부사항을 살펴보면", "정밀한 분석 결과", "꼼꼼히 검토한 바에 따르면"],
            "strategic": ["전략적으로 접근하면", "프로젝트 목표를 고려할 때", "장기적 관점에서"]
        }
        
        # 페르소나별 표현 방식 적용
        if self.persona.communication_style in personality_modifiers:
            modifiers = personality_modifiers[self.persona.communication_style]
            prefix = random.choice(modifiers)
            enhanced_response = f"{prefix}, {base_response}"
        else:
            enhanced_response = base_response
        
        # 전문가 고유 표현 추가
        if self.persona.catchphrases:
            catchphrase = random.choice(self.persona.catchphrases)
            enhanced_response += f" {catchphrase}"
        
        return enhanced_response
    
    def apply_expertise_filter(self, technical_content: str) -> str:
        """전문성 수준에 따른 내용 필터링"""
        if self.persona.theoretical_knowledge > 0.9:
            # 고수준 이론적 설명 추가
            return f"이론적 배경: {technical_content}\n\n고급 분석: 이 결과는 기존 연구와 일치하며..."
        elif self.persona.practical_experience > 0.9:
            # 실무 경험 기반 해석 추가
            return f"실무 관점: {technical_content}\n\n경험적 판단: {self.persona.experience_years}년 경험상..."
        else:
            return technical_content
    
    def make_expert_decision(self, options: List[Dict], criteria: str) -> Dict:
        """전문가 의사결정 과정"""
        decision_process = {
            "options_evaluated": len(options),
            "decision_criteria": criteria,
            "persona_bias": self.persona.decision_making_approach,
            "confidence_factors": []
        }
        
        # 페르소나별 의사결정 접근법
        if self.persona.decision_making_approach == "data_driven":
            # 데이터 기반 의사결정
            best_option = max(options, key=lambda x: x.get('technical_score', 0))
            decision_process["rationale"] = "기술적 데이터를 종합적으로 분석한 결과"
            
        elif self.persona.decision_making_approach == "risk_averse":
            # 위험 회피적 의사결정
            best_option = min(options, key=lambda x: x.get('risk_factor', 1))
            decision_process["rationale"] = "안전성과 신뢰성을 최우선으로 고려"
            
        elif self.persona.decision_making_approach == "innovative":
            # 혁신적 접근
            best_option = max(options, key=lambda x: x.get('innovation_score', 0))
            decision_process["rationale"] = "혁신적이고 창의적인 접근법 선택"
            
        else:
            # 균형잡힌 접근
            best_option = options[0]  # 기본값
            decision_process["rationale"] = "종합적 검토를 통한 균형잡힌 선택"
        
        decision_process["selected_option"] = best_option
        decision_process["confidence_level"] = self._calculate_decision_confidence(best_option)
        
        return decision_process
    
    def provide_expert_opinion(self, topic: str, context: Dict) -> ExpertOpinion:
        """전문가 의견 제공"""
        # 전문성 수준에 따른 의견 신뢰도 계산
        confidence = self._calculate_opinion_confidence(topic)
        
        # 페르소나별 의견 스타일
        opinion_content = self._generate_opinion_content(topic, context)
        
        # 지원 근거 생성
        evidence = self._generate_supporting_evidence(topic)
        
        # 우려사항 및 권고사항
        concerns = self._identify_concerns(topic, context)
        recommendations = self._generate_recommendations(topic, context)
        
        expert_opinion = ExpertOpinion(
            persona_name=self.persona.name,
            topic=topic,
            opinion=opinion_content,
            confidence_level=confidence,
            supporting_evidence=evidence,
            concerns=concerns,
            recommendations=recommendations
        )
        
        self.expert_opinions.append(expert_opinion)
        return expert_opinion
    
    def collaborate_with_peer(self, peer_agent: 'PersonaAgent', topic: str) -> Dict:
        """동료 전문가와의 협업"""
        collaboration = {
            "participants": [self.persona.name, peer_agent.persona.name],
            "topic": topic,
            "collaboration_type": self._determine_collaboration_type(peer_agent),
            "interaction_quality": self._assess_interaction_quality(peer_agent),
            "outcome": None,
            "timestamp": datetime.now()
        }
        
        # 협업 시뮬레이션
        my_opinion = self.provide_expert_opinion(topic, {})
        peer_opinion = peer_agent.provide_expert_opinion(topic, {})
        
        # 의견 통합 과정
        consensus = self._reach_consensus(my_opinion, peer_opinion)
        collaboration["outcome"] = consensus
        
        # 협업 기록 저장
        self.collaboration_history.append(collaboration)
        peer_agent.collaboration_history.append(collaboration)
        
        return collaboration
    
    def _calculate_opinion_confidence(self, topic: str) -> float:
        """의견 신뢰도 계산"""
        base_confidence = (
            self.persona.theoretical_knowledge * 0.3 +
            self.persona.practical_experience * 0.4 +
            self.persona.technical_accuracy * 0.3
        )
        
        # 주제별 전문성 보정
        if any(spec in topic.lower() for spec in self.persona.specializations):
            base_confidence = min(1.0, base_confidence + 0.2)
        
        return base_confidence
    
    def _calculate_decision_confidence(self, option: Dict) -> float:
        """의사결정 신뢰도 계산"""
        return min(1.0, self.persona.technical_accuracy + 
                  random.uniform(-0.1, 0.1))  # 약간의 변동성 추가
    
    def _generate_opinion_content(self, topic: str, context: Dict) -> str:
        """페르소나별 의견 내용 생성"""
        base_content = f"{self.persona.experience_years}년의 경험을 바탕으로 {topic}에 대해 분석하면"
        
        if self.persona.theoretical_knowledge > 0.8:
            base_content += ", 이론적 관점에서 매우 중요한 요소들이 있습니다."
        elif self.persona.practical_experience > 0.8:
            base_content += ", 실무에서 자주 접하는 케이스입니다."
        
        return self.express_personality(base_content)
    
    def _generate_supporting_evidence(self, topic: str) -> List[str]:
        """지원 근거 생성"""
        evidence = []
        
        if self.persona.theoretical_knowledge > 0.7:
            evidence.append("관련 이론 및 연구 문헌")
        if self.persona.practical_experience > 0.7:
            evidence.append(f"{self.persona.experience_years}년간의 실무 경험")
        if "ISO" in self.persona.specializations:
            evidence.append("국제 표준 규격 준수")
        
        return evidence
    
    def _identify_concerns(self, topic: str, context: Dict) -> List[str]:
        """우려사항 식별"""
        concerns = []
        
        # 페르소나별 우려 포인트
        if self.persona.decision_making_approach == "risk_averse":
            concerns.append("안전성 검증 필요")
        if self.persona.communication_style == "perfectionist":
            concerns.append("계산 정확도 재검토 요구")
        
        return concerns
    
    def _generate_recommendations(self, topic: str, context: Dict) -> List[str]:
        """권고사항 생성"""
        recommendations = []
        
        if self.persona.leadership_ability > 0.7:
            recommendations.append("팀 전체 검토 회의 소집")
        if self.persona.technical_accuracy > 0.8:
            recommendations.append("독립적 검증 수행")
        
        return recommendations
    
    def _determine_collaboration_type(self, peer_agent: 'PersonaAgent') -> str:
        """협업 유형 결정"""
        if self.persona.specializations == peer_agent.persona.specializations:
            return "peer_review"
        elif len(set(self.persona.specializations) & set(peer_agent.persona.specializations)) > 0:
            return "interdisciplinary"
        else:
            return "cross_functional"
    
    def _assess_interaction_quality(self, peer_agent: 'PersonaAgent') -> float:
        """상호작용 품질 평가"""
        my_comm = self.persona.communication_skill
        peer_comm = peer_agent.persona.communication_skill
        return (my_comm + peer_comm) / 2
    
    def _reach_consensus(self, my_opinion: ExpertOpinion, peer_opinion: ExpertOpinion) -> Dict:
        """의견 합의 도출"""
        consensus = {
            "agreement_level": self._calculate_agreement(my_opinion, peer_opinion),
            "integrated_opinion": self._integrate_opinions(my_opinion, peer_opinion),
            "remaining_disagreements": [],
            "action_items": []
        }
        
        # 합의 수준에 따른 후속 조치
        if consensus["agreement_level"] > 0.8:
            consensus["status"] = "strong_consensus"
        elif consensus["agreement_level"] > 0.6:
            consensus["status"] = "moderate_consensus"
            consensus["action_items"].append("추가 검토 필요")
        else:
            consensus["status"] = "disagreement"
            consensus["action_items"].append("제3자 중재 필요")
        
        return consensus
    
    def _calculate_agreement(self, opinion1: ExpertOpinion, opinion2: ExpertOpinion) -> float:
        """의견 일치도 계산"""
        # 신뢰도와 전문성을 고려한 일치도 계산
        conf_similarity = 1 - abs(opinion1.confidence_level - opinion2.confidence_level)
        return conf_similarity  # 단순화된 계산
    
    def _integrate_opinions(self, opinion1: ExpertOpinion, opinion2: ExpertOpinion) -> str:
        """의견 통합"""
        return f"{opinion1.persona_name}과 {opinion2.persona_name}의 종합 의견: " \
               f"두 전문가 모두 {opinion1.topic}에 대해 신중한 접근이 필요하다고 판단"

class ExpertPanel:
    """전문가 패널 관리"""
    
    def __init__(self):
        self.experts: Dict[str, PersonaAgent] = {}
        self.panel_discussions: List[Dict] = []
    
    def add_expert(self, expert: PersonaAgent):
        """전문가 추가"""
        self.experts[expert.persona.name] = expert
    
    def conduct_panel_discussion(self, topic: str, moderator: str = None) -> Dict:
        """패널 토론 진행"""
        discussion = {
            "topic": topic,
            "moderator": moderator,
            "participants": list(self.experts.keys()),
            "opinions": [],
            "consensus": None,
            "timestamp": datetime.now()
        }
        
        # 각 전문가 의견 수집
        for expert in self.experts.values():
            opinion = expert.provide_expert_opinion(topic, {})
            discussion["opinions"].append(opinion)
        
        # 합의 도출 과정
        discussion["consensus"] = self._facilitate_consensus(discussion["opinions"])
        
        self.panel_discussions.append(discussion)
        return discussion
    
    def _facilitate_consensus(self, opinions: List[ExpertOpinion]) -> Dict:
        """합의 촉진"""
        avg_confidence = sum(op.confidence_level for op in opinions) / len(opinions)
        
        return {
            "overall_confidence": avg_confidence,
            "consensus_reached": avg_confidence > 0.7,
            "key_agreements": ["표준 준수 필요", "품질 검증 중요"],
            "remaining_issues": ["세부 구현 방법", "일정 조정"]
        }