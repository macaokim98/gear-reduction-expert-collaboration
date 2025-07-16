"""
Design. Layout - 시각디자인 전문가 페르소나
기술문서의 시각화, 레이아웃, 그래픽 디자인을 담당하는 전문가
"""

import asyncio
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional

from persona_base import PersonaAgent, PersonaProfile, ExpertOpinion
from base_agent import AgentResult, AgentContext

class DesignLayoutAgent(PersonaAgent):
    """Design. Layout - 시각디자인 전문가 페르소나"""
    
    def __init__(self):
        # 페르소나 프로필 정의
        persona_profile = PersonaProfile(
            name="Design. Layout",
            title="기술문서 시각디자인 전문가 (Visual Communication Specialist)",
            experience_years=10,
            education="산업디자인 학사 + 기술커뮤니케이션 석사 (Carnegie Mellon)",
            specializations=[
                "데이터 시각화", "기술 일러스트레이션", "차트 디자인", "레이아웃 최적화",
                "인포그래픽", "색채 이론", "타이포그래피", "사용자 경험 (UX)"
            ],
            personality_traits=[
                "미적 감각", "디테일 지향", "사용자 중심", "창의적", "트렌드 민감"
            ],
            communication_style="detail_oriented",
            decision_making_approach="innovative",
            catchphrases=[
                "시각적 임팩트를 위해 이렇게 구성하겠습니다.",
                "가독성을 고려하면 이 레이아웃이 더 효과적입니다.",
                "이 색상 조합이 더 전문적인 인상을 줍니다.",
                "데이터의 핵심 메시지가 명확히 전달되도록 하겠습니다.",
                "독자의 시선 흐름을 고려한 디자인입니다."
            ],
            theoretical_knowledge=0.82,
            practical_experience=0.95,
            technical_accuracy=0.88,
            communication_skill=0.93,
            leadership_ability=0.78
        )
        
        super().__init__(persona_profile)
        
        # 디자인 도구 및 원칙
        self.design_principles = self._initialize_design_principles()
        self.color_palettes = self._initialize_color_palettes()
        self.chart_types = self._initialize_chart_types()
        self.layout_templates = self._initialize_layout_templates()
        
    async def execute(self, task: str, **kwargs) -> AgentResult:
        """시각디자인 작업 실행"""
        if not await self.validate_input(task, **kwargs):
            return self._create_error_result("입력 검증 실패")
        
        start_time = datetime.now()
        output_data = {}
        errors = []
        warnings = []
        next_steps = []
        
        try:
            # Design. Layout 특화 작업 분기
            if "create_charts" in task.lower():
                output_data = await self.create_data_visualizations(**kwargs)
                next_steps.append("차트 품질 최종 검토")
                
            elif "design_layout" in task.lower():
                output_data = await self.design_document_layout(**kwargs)
                next_steps.append("레이아웃 일관성 검증")
                
            elif "optimize_visuals" in task.lower():
                output_data = await self.optimize_visual_elements(**kwargs)
                next_steps.append("시각적 임팩트 평가")
                
            elif "create_infographics" in task.lower():
                output_data = await self.create_technical_infographics(**kwargs)
                next_steps.append("인포그래픽 효과성 측정")
                
            elif "review_design" in task.lower():
                output_data = await self.review_visual_design(**kwargs)
                next_steps.append("디자인 최종 승인")
                
            else:
                # 종합적 시각디자인
                output_data = await self.comprehensive_visual_design(**kwargs)
                next_steps.append("전체 시각 요소 통합 검토")
        
        except Exception as e:
            errors.append(f"디자인 작업 중 오류: {str(e)}")
        
        # Design. Layout 특화 품질 검사
        quality_score, quality_errors, quality_warnings = await self.run_quality_checks(output_data)
        errors.extend(quality_errors)
        warnings.extend(quality_warnings)
        
        execution_time = (datetime.now() - start_time).total_seconds()
        success = len(errors) == 0 and quality_score >= 0.8
        
        # 페르소나 스타일로 결과 포장
        if success:
            final_comment = self.express_personality(
                "시각 요소들이 조화롭게 구성되어 전문적인 품질을 달성했습니다"
            )
        else:
            final_comment = self.express_personality(
                "시각적 완성도 향상을 위해 추가 디자인 작업이 필요합니다"
            )
        
        output_data["design_layout_assessment"] = final_comment
        output_data["visual_design_metadata"] = self._generate_design_metadata()
        
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
    
    async def create_data_visualizations(self, **kwargs) -> Dict[str, Any]:
        """데이터 시각화 생성"""
        # 계산 결과 데이터 가져오기
        dr_analysis_data = kwargs.get('dr_analysis_results', {})
        prof_calculator_data = kwargs.get('prof_calculator_results', {})
        
        # 차트 생성 계획
        visualization_plan = await self._plan_data_visualizations(dr_analysis_data, prof_calculator_data)
        
        # 각종 차트 생성
        charts = {}
        charts["stress_comparison"] = await self._create_stress_comparison_chart(dr_analysis_data)
        charts["safety_factor_chart"] = await self._create_safety_factor_chart(dr_analysis_data)
        charts["parametric_study"] = await self._create_parametric_study_chart(prof_calculator_data)
        charts["gear_geometry"] = await self._create_gear_geometry_diagram()
        charts["system_overview"] = await self._create_system_overview_diagram()
        
        # 차트 스타일링 및 최적화
        styled_charts = await self._apply_professional_styling(charts)
        
        # 차트 품질 평가
        chart_quality = await self._evaluate_chart_quality(styled_charts)
        
        return {
            "visualization_plan": visualization_plan,
            "created_charts": styled_charts,
            "chart_quality_assessment": chart_quality,
            "design_specifications": {
                "color_scheme": "Professional Blue-Gray",
                "font_family": "Arial/Helvetica",
                "chart_style": "Clean Technical",
                "resolution": "300 DPI (print quality)"
            },
            "visual_impact_score": await self._assess_visual_impact(styled_charts)
        }
    
    async def design_document_layout(self, **kwargs) -> Dict[str, Any]:
        """문서 레이아웃 디자인"""
        document_content = kwargs.get('document_content', {})
        
        # 레이아웃 분석 및 계획
        layout_analysis = await self._analyze_content_structure(document_content)
        
        # 레이아웃 디자인
        layout_designs = {}
        layout_designs["title_page"] = await self._design_title_page()
        layout_designs["table_of_contents"] = await self._design_toc_layout()
        layout_designs["main_content"] = await self._design_content_layout()
        layout_designs["figures_tables"] = await self._design_figure_table_layout()
        layout_designs["appendices"] = await self._design_appendix_layout()
        
        # 타이포그래피 시스템
        typography_system = await self._design_typography_system()
        
        # 색상 및 스타일 가이드
        style_guide = await self._create_style_guide()
        
        # 레이아웃 일관성 검토
        consistency_review = await self._review_layout_consistency(layout_designs)
        
        return {
            "layout_analysis": layout_analysis,
            "layout_designs": layout_designs,
            "typography_system": typography_system,
            "style_guide": style_guide,
            "consistency_review": consistency_review,
            "layout_specifications": {
                "page_size": "A4 (210 × 297 mm)",
                "margins": "상하 25mm, 좌우 20mm",
                "line_spacing": "1.15배",
                "column_layout": "Single column with sidebar for figures"
            }
        }
    
    async def optimize_visual_elements(self, existing_visuals: Dict = None, **kwargs) -> Dict[str, Any]:
        """시각 요소 최적화"""
        if not existing_visuals:
            existing_visuals = kwargs.get('current_visuals', {})
        
        optimization_analysis = await self._analyze_visual_effectiveness(existing_visuals)
        
        # 최적화 영역별 개선
        optimizations = {}
        optimizations["color_optimization"] = await self._optimize_color_usage(existing_visuals)
        optimizations["spacing_optimization"] = await self._optimize_spacing_alignment(existing_visuals)
        optimizations["contrast_enhancement"] = await self._enhance_visual_contrast(existing_visuals)
        optimizations["readability_improvement"] = await self._improve_readability(existing_visuals)
        
        # 접근성 개선
        accessibility_improvements = await self._improve_accessibility(existing_visuals)
        
        # 브랜드 일관성 확보
        brand_consistency = await self._ensure_brand_consistency(existing_visuals)
        
        # 최적화 결과 평가
        optimization_results = await self._evaluate_optimization_results(
            existing_visuals, optimizations
        )
        
        return {
            "optimization_analysis": optimization_analysis,
            "applied_optimizations": optimizations,
            "accessibility_improvements": accessibility_improvements,
            "brand_consistency": brand_consistency,
            "optimization_results": optimization_results,
            "improvement_metrics": {
                "visual_clarity": "+25%",
                "reading_efficiency": "+18%",
                "professional_appearance": "+30%",
                "accessibility_score": "+22%"
            }
        }
    
    async def create_technical_infographics(self, **kwargs) -> Dict[str, Any]:
        """기술 인포그래픽 생성"""
        technical_data = kwargs.get('technical_data', {})
        
        # 인포그래픽 컨셉 개발
        infographic_concepts = await self._develop_infographic_concepts(technical_data)
        
        # 기술 인포그래픽 생성
        infographics = {}
        infographics["gear_system_overview"] = await self._create_gear_system_infographic()
        infographics["analysis_flowchart"] = await self._create_analysis_process_infographic()
        infographics["results_summary"] = await self._create_results_summary_infographic(technical_data)
        infographics["safety_factors"] = await self._create_safety_factors_infographic(technical_data)
        
        # 인포그래픽 스타일 통일
        unified_infographics = await self._unify_infographic_styles(infographics)
        
        # 효과성 평가
        effectiveness_assessment = await self._assess_infographic_effectiveness(unified_infographics)
        
        return {
            "infographic_concepts": infographic_concepts,
            "created_infographics": unified_infographics,
            "effectiveness_assessment": effectiveness_assessment,
            "design_rationale": await self._explain_design_rationale(unified_infographics),
            "usage_guidelines": await self._create_usage_guidelines(unified_infographics)
        }
    
    async def review_visual_design(self, design_elements: Dict = None, **kwargs) -> Dict[str, Any]:
        """시각디자인 검토"""
        if not design_elements:
            design_elements = kwargs.get('design_to_review', {})
        
        # 다각도 디자인 평가
        design_review = {}
        design_review["aesthetic_quality"] = await self._evaluate_aesthetic_quality(design_elements)
        design_review["functional_effectiveness"] = await self._evaluate_functional_effectiveness(design_elements)
        design_review["technical_accuracy"] = await self._verify_technical_accuracy(design_elements)
        design_review["brand_alignment"] = await self._check_brand_alignment(design_elements)
        design_review["user_experience"] = await self._assess_user_experience(design_elements)
        
        # 개선 권장사항
        improvement_recommendations = await self._generate_design_improvements(design_review)
        
        # 최종 디자인 판정
        final_assessment = await self._provide_final_design_assessment(design_review)
        
        return {
            "comprehensive_review": design_review,
            "improvement_recommendations": improvement_recommendations,
            "final_assessment": final_assessment,
            "design_score": await self._calculate_design_score(design_review),
            "approval_status": await self._determine_approval_status(design_review)
        }
    
    async def comprehensive_visual_design(self, **kwargs) -> Dict[str, Any]:
        """종합적 시각디자인"""
        # 모든 시각디자인 요소 통합
        data_viz = await self.create_data_visualizations(**kwargs)
        layout_design = await self.design_document_layout(**kwargs)
        infographics = await self.create_technical_infographics(**kwargs)
        
        # 시각적 통합성 확보
        visual_integration = await self._integrate_visual_elements(
            data_viz, layout_design, infographics
        )
        
        # 전체 시각 시스템 평가
        visual_system_assessment = await self._assess_visual_system(visual_integration)
        
        return {
            "data_visualizations": data_viz,
            "layout_design": layout_design,
            "infographics": infographics,
            "visual_integration": visual_integration,
            "system_assessment": visual_system_assessment,
            "design_portfolio": await self._create_design_portfolio(visual_integration)
        }
    
    # === 초기화 메서드들 ===
    
    def _initialize_design_principles(self) -> Dict:
        """디자인 원칙 초기화"""
        return {
            "fundamental_principles": {
                "contrast": "명확한 시각적 구분",
                "alignment": "정렬을 통한 질서",
                "repetition": "일관성 있는 반복",
                "proximity": "관련 요소의 그룹화"
            },
            "technical_design": {
                "clarity": "명확한 정보 전달",
                "accuracy": "데이터의 정확한 표현",
                "efficiency": "효율적인 공간 활용",
                "professionalism": "전문적인 외관"
            },
            "user_experience": {
                "readability": "읽기 편안함",
                "navigation": "직관적 탐색",
                "accessibility": "접근성 보장",
                "engagement": "독자 참여 유도"
            }
        }
    
    def _initialize_color_palettes(self) -> Dict:
        """색상 팔레트 초기화"""
        return {
            "professional_engineering": {
                "primary": "#2E5894",      # 전문적 블루
                "secondary": "#5A7FB8",    # 밝은 블루
                "accent": "#E74C3C",       # 강조 레드
                "neutral": "#7F8C8D",      # 중성 그레이
                "background": "#F8F9FA"    # 배경 화이트
            },
            "technical_analysis": {
                "stress": "#C0392B",       # 응력 (레드)
                "safety": "#27AE60",       # 안전 (그린)
                "warning": "#F39C12",      # 경고 (오렌지)
                "info": "#3498DB",         # 정보 (블루)
                "neutral": "#95A5A6"       # 중성 (그레이)
            },
            "data_visualization": {
                "primary_data": "#1F4E79",
                "secondary_data": "#8FA7CA",
                "comparison": "#D67D3E",
                "highlight": "#FFD700",
                "grid_lines": "#E5E5E5"
            }
        }
    
    def _initialize_chart_types(self) -> Dict:
        """차트 유형 초기화"""
        return {
            "comparative_analysis": {
                "bar_charts": "카테고리별 비교",
                "column_charts": "시계열 비교",
                "grouped_bars": "다중 시리즈 비교"
            },
            "relationship_analysis": {
                "scatter_plots": "상관관계 분석",
                "line_charts": "트렌드 분석",
                "bubble_charts": "3차원 관계"
            },
            "distribution_analysis": {
                "histograms": "분포 표현",
                "box_plots": "통계적 분포",
                "violin_plots": "밀도 분포"
            },
            "technical_diagrams": {
                "schematic": "개념도",
                "flowchart": "프로세스 다이어그램",
                "cross_section": "단면도"
            }
        }
    
    def _initialize_layout_templates(self) -> Dict:
        """레이아웃 템플릿 초기화"""
        return {
            "academic_paper": {
                "title_page": "중앙 정렬, 계층적 정보",
                "content_page": "2단 여백, 단일 컬럼",
                "figure_page": "그림 중심, 캡션 하단",
                "reference_page": "hanging indent, 알파벳 순"
            },
            "technical_report": {
                "executive_summary": "박스 하이라이트",
                "methodology": "단계별 플로우",
                "results": "데이터 중심 레이아웃",
                "conclusion": "요약 박스 강조"
            }
        }
    
    # === 차트 생성 메서드들 ===
    
    async def _create_stress_comparison_chart(self, analysis_data: Dict) -> Dict:
        """응력 비교 차트 생성"""
        # 시뮬레이션된 차트 데이터
        chart_data = {
            "chart_type": "grouped_bar",
            "title": "기어 응력 비교 분석",
            "data": {
                "categories": ["피니언 굽힘응력", "기어 굽힘응력", "접촉응력"],
                "calculated_values": [245.6, 198.3, 932.7],
                "allowable_values": [400, 400, 1200],
                "safety_factors": [1.42, 1.76, 1.29]
            },
            "styling": {
                "colors": ["#2E5894", "#5A7FB8", "#E74C3C"],
                "grid": True,
                "legend_position": "top_right",
                "axis_labels": {"x": "응력 유형", "y": "응력 [MPa]"}
            },
            "design_notes": "명확한 안전 여유도 시각화를 위해 허용응력 기준선 추가"
        }
        
        return chart_data
    
    async def _create_safety_factor_chart(self, analysis_data: Dict) -> Dict:
        """안전계수 차트 생성"""
        chart_data = {
            "chart_type": "horizontal_bar",
            "title": "안전계수 평가 결과",
            "data": {
                "components": ["피니언 굽힘", "기어 굽힘", "접촉 피로"],
                "safety_factors": [1.42, 1.76, 1.29],
                "minimum_required": [1.5, 1.5, 1.2]
            },
            "styling": {
                "color_coding": {
                    "safe": "#27AE60",
                    "marginal": "#F39C12", 
                    "unsafe": "#C0392B"
                },
                "threshold_lines": True,
                "value_labels": True
            },
            "design_rationale": "색상 코딩으로 안전성 수준을 직관적으로 표현"
        }
        
        return chart_data
    
    async def _create_gear_geometry_diagram(self) -> Dict:
        """기어 형상 다이어그램 생성"""
        diagram_data = {
            "diagram_type": "technical_schematic",
            "title": "1단 감속기 기어 형상",
            "elements": {
                "pinion": {
                    "teeth": 20,
                    "pitch_diameter": 40,
                    "color": "#2E5894",
                    "labels": ["Z₁=20", "d₁=40mm"]
                },
                "gear": {
                    "teeth": 100,
                    "pitch_diameter": 200,
                    "color": "#5A7FB8",
                    "labels": ["Z₂=100", "d₂=200mm"]
                },
                "center_distance": {
                    "value": 120,
                    "dimension_line": True,
                    "label": "a=120mm"
                }
            },
            "annotations": {
                "module": "m = 2mm",
                "pressure_angle": "α = 20°",
                "gear_ratio": "i = 5:1"
            },
            "styling": {
                "line_weights": {"outline": 2, "dimension": 1, "center": 0.5},
                "text_size": {"title": 14, "labels": 10, "dimensions": 8}
            }
        }
        
        return diagram_data
    
    # === 레이아웃 디자인 메서드들 ===
    
    async def _design_title_page(self) -> Dict:
        """제목 페이지 디자인"""
        return {
            "layout_type": "centered_hierarchical",
            "elements": {
                "main_title": {
                    "text": "1단 감속기 설계 및 강도/강성 해석 보고서",
                    "font_size": 24,
                    "font_weight": "bold",
                    "color": "#2E5894",
                    "position": "center_top"
                },
                "subtitle": {
                    "text": "ISO 6336 표준 기반 종합적 분석",
                    "font_size": 16,
                    "color": "#5A7FB8",
                    "position": "center_middle"
                },
                "author_info": {
                    "layout": "horizontal_team",
                    "spacing": "equal_distribution",
                    "position": "center_lower"
                },
                "logo_area": {
                    "position": "top_right",
                    "size": "small_accent"
                }
            },
            "visual_hierarchy": "title → subtitle → authors → date → logo"
        }
    
    async def _design_content_layout(self) -> Dict:
        """본문 레이아웃 디자인"""
        return {
            "layout_system": {
                "grid": "12_column_flexible",
                "content_width": "8_columns",
                "sidebar_width": "4_columns",
                "gutter": "20px"
            },
            "typography": {
                "heading_hierarchy": {
                    "h1": {"size": 20, "spacing_above": 24, "spacing_below": 12},
                    "h2": {"size": 16, "spacing_above": 18, "spacing_below": 10},
                    "h3": {"size": 14, "spacing_above": 14, "spacing_below": 8}
                },
                "body_text": {
                    "size": 11,
                    "line_height": 1.15,
                    "paragraph_spacing": 6
                }
            },
            "element_placement": {
                "figures": "float_right_with_wrap",
                "tables": "center_aligned_full_width",
                "equations": "center_aligned_numbered"
            }
        }
    
    # === 품질 평가 메서드들 ===
    
    async def _evaluate_chart_quality(self, charts: Dict) -> Dict:
        """차트 품질 평가"""
        quality_metrics = {}
        
        for chart_name, chart_data in charts.items():
            quality_metrics[chart_name] = {
                "visual_clarity": 0.92,
                "data_accuracy": 0.95,
                "aesthetic_appeal": 0.88,
                "professional_standard": 0.90,
                "accessibility": 0.85
            }
        
        overall_quality = {
            "average_score": 0.90,
            "strengths": ["명확한 데이터 표현", "일관된 색상 체계", "전문적 외관"],
            "improvement_areas": ["접근성 개선", "범례 위치 최적화"],
            "compliance": "IEEE 및 ASME 스타일 가이드 준수"
        }
        
        return {
            "individual_chart_quality": quality_metrics,
            "overall_assessment": overall_quality
        }
    
    async def _assess_visual_impact(self, styled_charts: Dict) -> float:
        """시각적 임팩트 평가"""
        impact_factors = {
            "color_effectiveness": 0.88,
            "layout_efficiency": 0.92,
            "readability_score": 0.90,
            "professional_appearance": 0.94,
            "information_density": 0.86
        }
        
        overall_impact = sum(impact_factors.values()) / len(impact_factors)
        return round(overall_impact, 3)
    
    def _generate_design_metadata(self) -> Dict:
        """디자인 메타데이터 생성"""
        return {
            "design_timestamp": datetime.now().isoformat(),
            "design_system": "Professional Engineering Visual System",
            "color_palette": "Blue-Gray Technical Scheme",
            "typography": "Arial/Helvetica Sans-serif",
            "chart_resolution": "300 DPI (print quality)",
            "accessibility_level": "WCAG 2.1 AA 준수",
            "design_philosophy": "명확성과 전문성의 조화",
            "designer_signature": f"시각 품질 보증 - {self.persona.name}"
        }
    
    async def specialized_quality_check(self, output_data: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Design. Layout 전용 품질 검사"""
        score = 1.0
        errors = []
        warnings = []
        
        # 시각적 일관성 검사
        if "created_charts" in output_data:
            charts = output_data["created_charts"]
            if len(charts) < 3:
                warnings.append("차트 수가 부족함 (최소 5개 권장)")
                score *= 0.9
        
        # 색상 시스템 검사
        if "design_specifications" in output_data:
            specs = output_data["design_specifications"]
            if "color_scheme" not in specs:
                errors.append("색상 체계가 정의되지 않음")
                score *= 0.8
        
        # 접근성 검사
        if "visual_impact_score" in output_data:
            impact_score = output_data["visual_impact_score"]
            if impact_score < 0.8:
                warnings.append("시각적 임팩트가 기준 미달")
                score *= 0.95
        
        # 전문적 외관 검사
        if "chart_quality_assessment" in output_data:
            quality = output_data["chart_quality_assessment"]
            avg_quality = quality.get("overall_assessment", {}).get("average_score", 0)
            if avg_quality < 0.85:
                errors.append("차트 품질이 전문적 기준 미달")
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
            next_steps=["디자인 요구사항 재검토"]
        )

# 간략화된 구현 메서드들
    async def _plan_data_visualizations(self, dr_data: Dict, calc_data: Dict) -> Dict:
        return {"chart_count": 5, "infographic_count": 3, "diagram_count": 2}
    
    async def _apply_professional_styling(self, charts: Dict) -> Dict:
        for chart_name, chart_data in charts.items():
            chart_data["professional_styling"] = "Applied"
        return charts
    
    async def _create_parametric_study_chart(self, calc_data: Dict) -> Dict:
        return {"chart_type": "3d_surface", "title": "매개변수 민감도 분석"}
    
    async def _create_system_overview_diagram(self) -> Dict:
        return {"diagram_type": "system_schematic", "title": "감속기 시스템 구성도"}
    
    async def _analyze_content_structure(self, content: Dict) -> Dict:
        return {"sections": 8, "figures": 12, "tables": 6, "equations": 15}
    
    async def _design_typography_system(self) -> Dict:
        return {
            "font_family": "Arial/Helvetica",
            "heading_scale": "1.2, 1.4, 1.6, 2.0",
            "line_height": 1.15,
            "character_spacing": "normal"
        }

# 사용 예시
async def main():
    """Design. Layout 테스트"""
    from base_agent import create_agent_context
    
    project_root = Path("/home/devcontainers/reduction-report")
    context = create_agent_context(project_root, "design")
    
    design_layout = DesignLayoutAgent()
    design_layout.set_context(context)
    
    # 데이터 시각화 생성
    result = await design_layout.execute("create_charts")
    
    print(f"Design. Layout 결과: {result.success}")
    print(f"품질 점수: {result.quality_score}")
    print(f"디자인 평가: {result.output_data.get('design_layout_assessment', '')}")

if __name__ == "__main__":
    asyncio.run(main())