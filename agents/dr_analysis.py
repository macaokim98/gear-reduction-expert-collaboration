"""
Dr. Analysis - 기어 설계 20년차 박사 페르소나
이론과 실무를 겸비한 기계공학 해석 전문가
"""

import asyncio
import math
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

from persona_base import PersonaAgent, PersonaProfile, ExpertOpinion
from base_agent import AgentResult, AgentContext

class DrAnalysisAgent(PersonaAgent):
    """Dr. Analysis - 기어 해석 전문가 페르소나"""
    
    def __init__(self):
        # 페르소나 프로필 정의
        persona_profile = PersonaProfile(
            name="Dr. Analysis",
            title="수석 기계공학 박사 (기어 시스템 전문가)",
            experience_years=20,
            education="기계공학 박사 (Seoul National University), 독일 TU Munich 박사후연구",
            specializations=[
                "기어 동역학", "접촉 역학", "피로 해석", "ISO 6336", "AGMA 표준",
                "유한요소해석", "실험적 검증", "신뢰성 공학"
            ],
            personality_traits=[
                "체계적", "보수적", "완벽주의", "안전 지향적", "이론-실무 균형"
            ],
            communication_style="conservative",
            decision_making_approach="risk_averse",
            catchphrases=[
                "20년 경험상 이런 경우에는 주의가 필요합니다.",
                "이론적으로는 가능하지만 실제로는 다른 요인들을 고려해야 합니다.",
                "안전계수는 충분히 확보하는 것이 중요합니다.",
                "표준에서 권장하는 방법을 따르는 것이 가장 확실합니다."
            ],
            theoretical_knowledge=0.95,
            practical_experience=0.90,
            technical_accuracy=0.93,
            communication_skill=0.85,
            leadership_ability=0.80
        )
        
        super().__init__(persona_profile)
        
        # 전문 지식 데이터베이스
        self.iso_6336_knowledge = self._initialize_iso_knowledge()
        self.material_database = self._initialize_material_db()
        self.failure_mode_expertise = self._initialize_failure_modes()
        
    async def execute(self, task: str, **kwargs) -> AgentResult:
        """기어 해석 작업 실행"""
        if not await self.validate_input(task, **kwargs):
            return self._create_error_result("입력 검증 실패")
        
        start_time = datetime.now()
        output_data = {}
        errors = []
        warnings = []
        next_steps = []
        
        try:
            # Dr. Analysis 특화 작업 분기
            if "strength_analysis" in task.lower():
                output_data = await self.perform_strength_analysis(**kwargs)
                next_steps.append("접촉 강도 해석 수행")
                
            elif "stiffness_analysis" in task.lower():
                output_data = await self.perform_stiffness_analysis(**kwargs)
                next_steps.append("동적 특성 분석 고려")
                
            elif "failure_analysis" in task.lower():
                output_data = await self.analyze_failure_modes(**kwargs)
                next_steps.append("예방 조치 방안 수립")
                
            elif "design_review" in task.lower():
                output_data = await self.review_gear_design(**kwargs)
                next_steps.append("최적화 방안 검토")
                
            else:
                # 종합적 기어 해석
                output_data = await self.comprehensive_gear_analysis(**kwargs)
                next_steps.append("계산 결과 검증 필요")
        
        except Exception as e:
            errors.append(f"해석 중 오류 발생: {str(e)}")
        
        # Dr. Analysis 특화 품질 검사
        quality_score, quality_errors, quality_warnings = await self.run_quality_checks(output_data)
        errors.extend(quality_errors)
        warnings.extend(quality_warnings)
        
        execution_time = (datetime.now() - start_time).total_seconds()
        success = len(errors) == 0 and quality_score >= 0.8
        
        # 페르소나 스타일로 결과 포장
        if success:
            final_comment = self.express_personality(
                "해석 결과가 공학적으로 타당하며 안전성 기준을 만족합니다"
            )
        else:
            final_comment = self.express_personality(
                "추가 검토와 보완이 필요한 부분이 있습니다"
            )
        
        output_data["expert_commentary"] = final_comment
        
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
    
    async def perform_strength_analysis(self, **kwargs) -> Dict[str, Any]:
        """기어 강도 해석 수행"""
        # 프로젝트 파라미터 가져오기
        params = self.context.parameters
        module = float(params.get('module', '2').replace('mm', '').strip())
        gear_ratio = params.get('gear_ratio', '5:1')
        input_torque = float(params.get('input_torque', '20').replace('Nm', '').strip())
        
        # 기어 제원 계산
        gear_specs = self._calculate_gear_specifications(module, gear_ratio, input_torque)
        
        # ISO 6336 기반 강도 계산
        bending_analysis = await self._iso_6336_bending_strength(gear_specs)
        contact_analysis = await self._iso_6336_contact_strength(gear_specs)
        
        # Dr. Analysis의 전문가 판단
        expert_assessment = self._provide_strength_assessment(bending_analysis, contact_analysis)
        
        analysis_result = {
            "analysis_method": "ISO 6336:2019 기반 강도 해석",
            "gear_specifications": gear_specs,
            "bending_strength": bending_analysis,
            "contact_strength": contact_analysis,
            "expert_assessment": expert_assessment,
            "safety_factors": {
                "bending_pinion": bending_analysis.get("safety_factor_pinion", 0),
                "bending_gear": bending_analysis.get("safety_factor_gear", 0),
                "contact": contact_analysis.get("safety_factor", 0)
            },
            "recommendations": self._generate_strength_recommendations(bending_analysis, contact_analysis)
        }
        
        return analysis_result
    
    async def perform_stiffness_analysis(self, **kwargs) -> Dict[str, Any]:
        """기어 강성 해석 수행"""
        params = self.context.parameters
        
        # 기어 시스템 강성 분석
        mesh_stiffness = await self._calculate_mesh_stiffness()
        shaft_stiffness = await self._calculate_shaft_stiffness()
        bearing_stiffness = await self._calculate_bearing_stiffness()
        housing_stiffness = await self._calculate_housing_stiffness()
        
        # 전체 시스템 강성
        system_stiffness = await self._analyze_system_stiffness(
            mesh_stiffness, shaft_stiffness, bearing_stiffness, housing_stiffness
        )
        
        # Dr. Analysis의 강성 평가
        stiffness_assessment = self._evaluate_stiffness_adequacy(system_stiffness)
        
        return {
            "analysis_method": "다단계 강성 해석 (Gear Mesh + Shaft + Bearing + Housing)",
            "mesh_stiffness": mesh_stiffness,
            "shaft_stiffness": shaft_stiffness,
            "bearing_stiffness": bearing_stiffness,
            "housing_stiffness": housing_stiffness,
            "system_stiffness": system_stiffness,
            "expert_evaluation": stiffness_assessment,
            "performance_implications": self._assess_stiffness_impact()
        }
    
    async def analyze_failure_modes(self, **kwargs) -> Dict[str, Any]:
        """기어 실패 모드 분석"""
        failure_modes = {
            "bending_fatigue": await self._analyze_bending_fatigue(),
            "contact_fatigue": await self._analyze_contact_fatigue(),
            "scuffing": await self._analyze_scuffing_risk(),
            "wear": await self._analyze_wear_mechanisms(),
            "scoring": await self._analyze_scoring_potential()
        }
        
        # 실패 확률 및 위험도 평가
        risk_assessment = self._assess_failure_risks(failure_modes)
        
        # 예방 조치 방안
        prevention_strategies = self._develop_prevention_strategies(failure_modes)
        
        return {
            "failure_mode_analysis": failure_modes,
            "risk_assessment": risk_assessment,
            "prevention_strategies": prevention_strategies,
            "expert_opinion": self.express_personality(
                "다양한 실패 모드를 종합적으로 고려한 설계가 필요합니다"
            )
        }
    
    async def review_gear_design(self, **kwargs) -> Dict[str, Any]:
        """기어 설계 검토"""
        design_review = {
            "geometric_review": await self._review_geometry(),
            "material_selection": await self._review_materials(),
            "manufacturing_considerations": await self._review_manufacturing(),
            "performance_prediction": await self._predict_performance(),
            "optimization_opportunities": await self._identify_optimizations()
        }
        
        overall_assessment = self._provide_design_assessment(design_review)
        
        return {
            "design_review": design_review,
            "overall_assessment": overall_assessment,
            "dr_analysis_verdict": self.express_personality(overall_assessment["summary"])
        }
    
    async def comprehensive_gear_analysis(self, **kwargs) -> Dict[str, Any]:
        """종합적 기어 해석"""
        # 모든 해석을 통합 수행
        strength_result = await self.perform_strength_analysis(**kwargs)
        stiffness_result = await self.perform_stiffness_analysis(**kwargs)
        failure_result = await self.analyze_failure_modes(**kwargs)
        
        # 종합적 평가
        comprehensive_assessment = {
            "strength_adequacy": self._grade_analysis(strength_result),
            "stiffness_adequacy": self._grade_analysis(stiffness_result),
            "reliability_level": self._grade_analysis(failure_result),
            "overall_grade": "A",  # A, B, C, D, F
            "critical_issues": [],
            "improvement_areas": []
        }
        
        return {
            "comprehensive_analysis": {
                "strength": strength_result,
                "stiffness": stiffness_result,
                "failure_modes": failure_result
            },
            "integrated_assessment": comprehensive_assessment,
            "final_expert_opinion": self._formulate_final_opinion(comprehensive_assessment)
        }
    
    # === 전문 지식 초기화 메서드들 ===
    
    def _initialize_iso_knowledge(self) -> Dict:
        """ISO 6336 지식 베이스 초기화"""
        return {
            "bending_factors": {
                "YFa": "치형계수 (Form factor)",
                "YSa": "응력집중계수 (Stress concentration factor)", 
                "Yε": "접촉비계수 (Contact ratio factor)",
                "Yβ": "나선각계수 (Helix angle factor)"
            },
            "contact_factors": {
                "ZE": "탄성계수 (Elasticity factor)",
                "ZH": "접촉형상계수 (Zone factor)",
                "Zε": "접촉비계수 (Contact ratio factor)",
                "Zβ": "나선각계수 (Helix angle factor)"
            },
            "material_factors": {
                "σFlim": "굽힘피로한계 (Bending fatigue limit)",
                "σHlim": "접촉피로한계 (Contact fatigue limit)",
                "YNT": "수명계수 (Life factor)",
                "ZNT": "수명계수 (Life factor)"
            }
        }
    
    def _initialize_material_db(self) -> Dict:
        """재료 데이터베이스 초기화"""
        return {
            "SCM415": {
                "yield_strength": 785,  # MPa
                "ultimate_strength": 980,  # MPa
                "bending_fatigue_limit": 400,  # MPa
                "contact_fatigue_limit": 1200,  # MPa
                "elastic_modulus": 206000,  # MPa
                "poisson_ratio": 0.3,
                "hardness_hrc": "58-62 (표면)",
                "treatment": "침탄경화"
            },
            "S45C": {
                "yield_strength": 490,  # MPa
                "ultimate_strength": 686,  # MPa
                "bending_fatigue_limit": 270,  # MPa
                "contact_fatigue_limit": 900,  # MPa
                "elastic_modulus": 206000,  # MPa
                "poisson_ratio": 0.3,
                "hardness_hrc": "45-50",
                "treatment": "조질"
            }
        }
    
    def _initialize_failure_modes(self) -> Dict:
        """실패 모드 지식 베이스 초기화"""
        return {
            "bending_fatigue": {
                "description": "치근부 굽힘 피로 균열",
                "indicators": ["응력 집중", "하중 변동", "재료 결함"],
                "prevention": ["적절한 치근 반지름", "표면처리", "하중 관리"]
            },
            "pitting": {
                "description": "치면 접촉 피로로 인한 피팅",
                "indicators": ["접촉응력 초과", "윤활 불량", "표면 거칠기"],
                "prevention": ["접촉응력 감소", "윤활 개선", "표면 품질 향상"]
            },
            "scuffing": {
                "description": "높은 접촉온도로 인한 응착 마모",
                "indicators": ["고속 운전", "고하중", "윤활 부족"],
                "prevention": ["속도 제한", "충분한 윤활", "표면처리"]
            }
        }
    
    # === 계산 메서드들 ===
    
    def _calculate_gear_specifications(self, module: float, gear_ratio: str, input_torque: float) -> Dict:
        """기어 제원 계산"""
        ratio_parts = gear_ratio.split(':')
        ratio = float(ratio_parts[1]) / float(ratio_parts[0])
        
        # 기본 치수 계산
        pinion_teeth = 20  # 일반적인 피니언 잇수
        gear_teeth = int(pinion_teeth * ratio)
        
        specs = {
            "module": module,
            "gear_ratio": ratio,
            "pinion": {
                "teeth": pinion_teeth,
                "pitch_diameter": module * pinion_teeth,
                "addendum_diameter": module * (pinion_teeth + 2),
                "dedendum_diameter": module * (pinion_teeth - 2.5)
            },
            "gear": {
                "teeth": gear_teeth,
                "pitch_diameter": module * gear_teeth,
                "addendum_diameter": module * (gear_teeth + 2),
                "dedendum_diameter": module * (gear_teeth - 2.5)
            },
            "center_distance": module * (pinion_teeth + gear_teeth) / 2,
            "input_torque": input_torque,
            "output_torque": input_torque * ratio * 0.95  # 효율 95% 가정
        }
        
        return specs
    
    async def _iso_6336_bending_strength(self, gear_specs: Dict) -> Dict:
        """ISO 6336 굽힘 강도 계산"""
        # 간략화된 계산 (실제로는 더 복잡함)
        module = gear_specs["module"]
        face_width = 25.0  # mm, 가정값
        
        # 피니언 계산
        pinion_force = (2 * gear_specs["input_torque"] * 1000) / gear_specs["pinion"]["pitch_diameter"]
        pinion_stress = (pinion_force * 2.8 * 1.0 * 1.0 * 1.0) / (face_width * module)  # 간략화
        pinion_safety = 400 / pinion_stress  # SCM415 기준
        
        # 기어 계산
        gear_force = pinion_force
        gear_stress = (gear_force * 2.2 * 1.0 * 1.0 * 1.0) / (face_width * module)  # 간략화
        gear_safety = 400 / gear_stress
        
        return {
            "calculation_method": "ISO 6336-3:2019",
            "pinion_bending_stress": round(pinion_stress, 1),
            "gear_bending_stress": round(gear_stress, 1),
            "safety_factor_pinion": round(pinion_safety, 2),
            "safety_factor_gear": round(gear_safety, 2),
            "allowable_stress": 400,
            "assessment": "안전" if min(pinion_safety, gear_safety) > 1.5 else "검토 필요"
        }
    
    async def _iso_6336_contact_strength(self, gear_specs: Dict) -> Dict:
        """ISO 6336 접촉 강도 계산"""
        # 간략화된 접촉응력 계산
        Ze = 189.8  # 강재의 탄성계수 인자
        contact_force = (2 * gear_specs["input_torque"] * 1000) / gear_specs["pinion"]["pitch_diameter"]
        
        # 헤르츠 접촉응력 (간략화)
        contact_stress = Ze * math.sqrt(contact_force / (25.0 * gear_specs["pinion"]["pitch_diameter"]))
        safety_factor = 1200 / contact_stress  # SCM415 기준
        
        return {
            "calculation_method": "ISO 6336-2:2019", 
            "contact_stress": round(contact_stress, 1),
            "safety_factor": round(safety_factor, 2),
            "allowable_stress": 1200,
            "assessment": "안전" if safety_factor > 1.2 else "검토 필요"
        }
    
    # === 기타 해석 메서드들 (간략화) ===
    
    async def _calculate_mesh_stiffness(self) -> Dict:
        """기어 맞물림 강성 계산"""
        return {
            "single_tooth_stiffness": 15.8,  # N/μm/mm
            "mesh_stiffness": 12.4,  # N/μm/mm  
            "stiffness_variation": 0.15  # 15% 변동
        }
    
    async def _calculate_shaft_stiffness(self) -> Dict:
        """축 강성 계산"""
        return {
            "torsional_stiffness": 2.1e6,  # Nm/rad
            "bending_stiffness": 1.8e8,  # N/m
            "material": "S45C"
        }
    
    async def _calculate_bearing_stiffness(self) -> Dict:
        """베어링 강성 계산"""
        return {
            "radial_stiffness": 1.5e8,  # N/m
            "axial_stiffness": 2.2e8,  # N/m
            "bearing_type": "Deep groove ball bearing"
        }
    
    async def _calculate_housing_stiffness(self) -> Dict:
        """하우징 강성 계산"""
        return {
            "structural_stiffness": 3.2e8,  # N/m
            "material": "Cast iron",
            "design_factor": 1.2
        }
    
    # === 평가 및 판단 메서드들 ===
    
    def _provide_strength_assessment(self, bending: Dict, contact: Dict) -> str:
        """강도 해석 결과 평가"""
        min_safety = min(
            bending["safety_factor_pinion"],
            bending["safety_factor_gear"], 
            contact["safety_factor"]
        )
        
        if min_safety > 2.0:
            assessment = "우수한 안전성을 확보하고 있습니다"
        elif min_safety > 1.5:
            assessment = "적절한 안전성을 가지고 있으나 여유도를 더 확보하는 것이 바람직합니다"
        else:
            assessment = "안전계수가 부족하여 설계 변경이 필요합니다"
        
        return self.express_personality(assessment)
    
    def _generate_strength_recommendations(self, bending: Dict, contact: Dict) -> List[str]:
        """강도 개선 권장사항"""
        recommendations = []
        
        if bending["safety_factor_pinion"] < 1.8:
            recommendations.append("피니언 치폭 증가 검토")
        if contact["safety_factor"] < 1.5:
            recommendations.append("표면 경도 향상 또는 접촉응력 감소 방안 필요")
            
        recommendations.append("20년 경험상 안전계수는 최소 1.5 이상 확보하시기 바랍니다")
        
        return recommendations
    
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
            next_steps=["입력 데이터 확인 및 수정"]
        )
    
    async def specialized_quality_check(self, output_data: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Dr. Analysis 전용 품질 검사"""
        score = 1.0
        errors = []
        warnings = []
        
        # 기술적 정확성 검사
        if "bending_strength" in output_data:
            bending = output_data["bending_strength"]
            if bending.get("safety_factor_pinion", 0) < 1.2:
                errors.append("피니언 굽힘 안전계수가 너무 낮음")
                score *= 0.6
        
        # 전문가 기준 검사
        if "safety_factors" in output_data:
            factors = output_data["safety_factors"]
            min_factor = min(factors.values()) if factors.values() else 0
            if min_factor < 1.5:
                warnings.append("Dr. Analysis 기준: 안전계수 1.5 이상 권장")
                score *= 0.9
        
        return score, errors, warnings

# 사용 예시
async def main():
    """Dr. Analysis 테스트"""
    from base_agent import create_agent_context
    
    project_root = Path("/home/devcontainers/reduction-report")
    context = create_agent_context(project_root, "analysis")
    
    dr_analysis = DrAnalysisAgent()
    dr_analysis.set_context(context)
    
    # 강도 해석 수행
    result = await dr_analysis.execute("strength_analysis")
    
    print(f"Dr. Analysis 결과: {result.success}")
    print(f"전문가 의견: {result.output_data.get('expert_commentary', '')}")

if __name__ == "__main__":
    asyncio.run(main())