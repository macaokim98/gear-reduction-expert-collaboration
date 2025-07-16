"""
ISO 6336 기어 강도 계산 엔진
실제 수치 계산 및 상세 과정 기록을 위한 라이브러리
"""

import math
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass

@dataclass
class GearGeometry:
    """기어 기하학적 제원"""
    module: float           # 모듈 (mm)
    teeth_pinion: int      # 구동기어 잇수
    teeth_gear: int        # 피동기어 잇수
    face_width: float      # 치폭 (mm)
    pressure_angle: float  # 압력각 (도)
    
    @property
    def gear_ratio(self) -> float:
        return self.teeth_gear / self.teeth_pinion
    
    @property
    def pitch_diameter_pinion(self) -> float:
        return self.module * self.teeth_pinion
    
    @property
    def pitch_diameter_gear(self) -> float:
        return self.module * self.teeth_gear
    
    @property
    def center_distance(self) -> float:
        return (self.pitch_diameter_pinion + self.pitch_diameter_gear) / 2

@dataclass
class LoadConditions:
    """하중 조건"""
    input_torque: float    # 입력 토크 (Nm)
    input_speed: float     # 입력 회전수 (rpm)
    power: float          # 전달 동력 (kW)

@dataclass
class MaterialProperties:
    """재료 특성"""
    name: str                    # 재료명
    allowable_bending: float     # 허용 굽힘응력 (MPa)
    allowable_contact: float     # 허용 접촉응력 (MPa)
    elastic_modulus: float       # 탄성계수 (GPa)
    poisson_ratio: float         # 포아송비
    density: float               # 밀도 (kg/m³)

@dataclass
class CalculationStep:
    """계산 단계 기록"""
    step_number: int
    description: str
    formula: str
    variables: Dict[str, Any]
    calculation: str
    result: float
    unit: str
    notes: str = ""

class ISO6336Calculator:
    """ISO 6336 표준 기어 강도 계산기"""
    
    def __init__(self):
        self.calculation_steps: List[CalculationStep] = []
        self.step_counter = 0
    
    def add_calculation_step(self, description: str, formula: str, 
                           variables: Dict[str, Any], calculation: str, 
                           result: float, unit: str, notes: str = "") -> None:
        """계산 단계 기록"""
        self.step_counter += 1
        step = CalculationStep(
            step_number=self.step_counter,
            description=description,
            formula=formula,
            variables=variables,
            calculation=calculation,
            result=result,
            unit=unit,
            notes=notes
        )
        self.calculation_steps.append(step)
    
    def calculate_tangential_force(self, geometry: GearGeometry, 
                                 load: LoadConditions) -> float:
        """접선력 계산 (ISO 6336-1)"""
        
        # 단계 1: 피치원 반경 계산
        r_pinion = geometry.pitch_diameter_pinion / 2
        self.add_calculation_step(
            description="구동기어 피치원 반경 계산",
            formula="r₁ = d₁/2 = (mn × z₁)/2",
            variables={
                "mn": geometry.module,
                "z₁": geometry.teeth_pinion,
                "d₁": geometry.pitch_diameter_pinion
            },
            calculation=f"r₁ = {geometry.pitch_diameter_pinion}/2",
            result=r_pinion,
            unit="mm",
            notes="피치원 반경은 토크를 접선력으로 변환하는 기준"
        )
        
        # 단계 2: 접선력 계산  
        Ft = (load.input_torque * 1000) / r_pinion  # Nm을 Nmm로 변환
        self.add_calculation_step(
            description="접선력 계산 (기본 동력 전달 관계)",
            formula="Ft = T/r₁",
            variables={
                "T": load.input_torque,
                "r₁": r_pinion
            },
            calculation=f"Ft = ({load.input_torque} × 1000)/{r_pinion}",
            result=Ft,
            unit="N",
            notes="접선력은 기어 치에 작용하는 주요 하중"
        )
        
        return Ft
    
    def calculate_form_factor(self, teeth: int) -> float:
        """치형계수 Y_Fa 계산 (ISO 6336-3)"""
        
        # Lewis 치형계수 근사식 (20도 압력각)
        if teeth < 12:
            Y_Fa = 0.18 + 0.15 * teeth / 12
        elif teeth <= 25:
            Y_Fa = 0.154 - 0.912/teeth
        elif teeth <= 100:
            Y_Fa = 0.175 - 0.841/teeth  
        else:
            Y_Fa = 0.175 - 84.1/teeth
            
        self.add_calculation_step(
            description=f"치형계수 Y_Fa 계산 ({teeth}치 기어)",
            formula="Y_Fa = f(z) [ISO 6336-3 Table]" if teeth <= 25 else "Y_Fa = 0.175 - 84.1/z (z>25)",
            variables={
                "z": teeth
            },
            calculation=f"Y_Fa = 0.175 - 84.1/{teeth}" if teeth > 25 else f"표준값 조회 (z={teeth})",
            result=Y_Fa,
            unit="-",
            notes="치형계수는 치의 형상에 따른 응력 집중 계수"
        )
        
        return Y_Fa
    
    def calculate_stress_correction_factor(self, teeth: int) -> float:
        """응력보정계수 Y_Sa 계산 (ISO 6336-3)"""
        
        # 표준 20도 압력각에 대한 근사식
        if teeth <= 25:
            Y_Sa = 1.2 + 0.13 * math.log(teeth)
        else:
            Y_Sa = 1.5 + 0.25 * math.log(teeth/25)
            
        self.add_calculation_step(
            description=f"응력보정계수 Y_Sa 계산 ({teeth}치)",
            formula="Y_Sa = 1.2 + 0.13×ln(z) (z≤25)" if teeth <= 25 else "Y_Sa = 1.5 + 0.25×ln(z/25) (z>25)",
            variables={
                "z": teeth
            },
            calculation=f"Y_Sa = 1.2 + 0.13×ln({teeth})" if teeth <= 25 else f"Y_Sa = 1.5 + 0.25×ln({teeth}/25)",
            result=Y_Sa,
            unit="-", 
            notes="응력보정계수는 치근부 응력 분포 보정값"
        )
        
        return Y_Sa
    
    def calculate_bending_stress(self, geometry: GearGeometry, 
                               load: LoadConditions, Ft: float) -> Tuple[float, float]:
        """굽힘응력 계산 (ISO 6336-3)"""
        
        # 구동기어 굽힘응력 계산
        Y_Fa_pinion = self.calculate_form_factor(geometry.teeth_pinion)
        Y_Sa_pinion = self.calculate_stress_correction_factor(geometry.teeth_pinion)
        
        # ISO 6336-3 굽힘응력 공식
        sigma_F_pinion = (Ft * Y_Fa_pinion * Y_Sa_pinion) / (geometry.face_width * geometry.module)
        
        self.add_calculation_step(
            description="구동기어 굽힘응력 계산 (ISO 6336-3)",
            formula="σF = (Ft × Y_Fa × Y_Sa)/(b × mn)",
            variables={
                "Ft": Ft,
                "Y_Fa": Y_Fa_pinion,
                "Y_Sa": Y_Sa_pinion,
                "b": geometry.face_width,
                "mn": geometry.module
            },
            calculation=f"σF = ({Ft:.1f} × {Y_Fa_pinion:.3f} × {Y_Sa_pinion:.3f})/({geometry.face_width} × {geometry.module})",
            result=sigma_F_pinion,
            unit="MPa",
            notes="구동기어는 일반적으로 더 높은 굽힘응력을 받음"
        )
        
        # 피동기어 굽힘응력 계산
        Y_Fa_gear = self.calculate_form_factor(geometry.teeth_gear)
        Y_Sa_gear = self.calculate_stress_correction_factor(geometry.teeth_gear)
        
        sigma_F_gear = (Ft * Y_Fa_gear * Y_Sa_gear) / (geometry.face_width * geometry.module)
        
        self.add_calculation_step(
            description="피동기어 굽힘응력 계산 (ISO 6336-3)",
            formula="σF = (Ft × Y_Fa × Y_Sa)/(b × mn)",
            variables={
                "Ft": Ft,
                "Y_Fa": Y_Fa_gear,
                "Y_Sa": Y_Sa_gear,
                "b": geometry.face_width,
                "mn": geometry.module
            },
            calculation=f"σF = ({Ft:.1f} × {Y_Fa_gear:.3f} × {Y_Sa_gear:.3f})/({geometry.face_width} × {geometry.module})",
            result=sigma_F_gear,
            unit="MPa",
            notes="피동기어는 잇수가 많아 상대적으로 낮은 굽힘응력"
        )
        
        return sigma_F_pinion, sigma_F_gear
    
    def calculate_contact_stress(self, geometry: GearGeometry, 
                               material: MaterialProperties, Ft: float) -> float:
        """접촉응력 계산 (ISO 6336-2)"""
        
        # Zone factor ZH 계산 (외치차 기준)
        alpha_rad = math.radians(geometry.pressure_angle)
        Z_H = math.sqrt(2 * math.cos(alpha_rad) / math.sin(alpha_rad))
        
        self.add_calculation_step(
            description="구역계수 Z_H 계산",
            formula="Z_H = √(2×cos(αn)/sin(αn))",
            variables={
                "αn": geometry.pressure_angle,
                "cos(αn)": math.cos(alpha_rad),
                "sin(αn)": math.sin(alpha_rad)
            },
            calculation=f"Z_H = √(2×{math.cos(alpha_rad):.3f}/{math.sin(alpha_rad):.3f})",
            result=Z_H,
            unit="-",
            notes="구역계수는 치면 접촉 형상에 따른 계수"
        )
        
        # Elastic coefficient Ze 계산 (강재 기준)
        Z_E = math.sqrt(1 / (math.pi * ((1 - 0.3**2)/material.elastic_modulus + 
                                       (1 - 0.3**2)/material.elastic_modulus)))
        
        self.add_calculation_step(
            description="탄성계수 Z_E 계산 (강재-강재)",
            formula="Z_E = √(1/(π×((1-ν₁²)/E₁ + (1-ν₂²)/E₂)))",
            variables={
                "ν": 0.3,
                "E": material.elastic_modulus,
                "π": math.pi
            },
            calculation=f"Z_E = √(1/(π×2×(1-0.3²)/{material.elastic_modulus}))",
            result=Z_E,
            unit="√MPa",
            notes="동일 재료이므로 탄성계수 동일 적용"
        )
        
        # Contact ratio factor Zε 계산 (표준 기어 기준)
        Z_epsilon = math.sqrt(0.9)  # 근사값 (표준 외치차)
        
        self.add_calculation_step(
            description="접촉비계수 Z_ε 계산",
            formula="Z_ε = √εα (εα ≈ 1.8 for standard gears)",
            variables={
                "εα": 1.8
            },
            calculation="Z_ε = √(1.8×0.5) = √0.9",
            result=Z_epsilon,
            unit="-",
            notes="표준 외치차 기어의 일반적인 접촉비 적용"
        )
        
        # Hertz 접촉응력 계산
        u = geometry.gear_ratio
        sigma_H = Z_H * Z_E * Z_epsilon * math.sqrt(
            (Ft * (u + 1)) / (geometry.face_width * geometry.pitch_diameter_pinion * u)
        )
        
        self.add_calculation_step(
            description="Hertz 접촉응력 계산 (ISO 6336-2)",
            formula="σH = Z_H × Z_E × Z_ε × √(Ft×(u+1)/(b×d₁×u))",
            variables={
                "Z_H": Z_H,
                "Z_E": Z_E,
                "Z_ε": Z_epsilon,
                "Ft": Ft,
                "u": u,
                "b": geometry.face_width,
                "d₁": geometry.pitch_diameter_pinion
            },
            calculation=f"σH = {Z_H:.2f}×{Z_E:.1f}×{Z_epsilon:.3f}×√({Ft:.1f}×{u+1:.1f}/({geometry.face_width}×{geometry.pitch_diameter_pinion}×{u:.1f}))",
            result=sigma_H,
            unit="MPa",
            notes="접촉응력은 두 기어에서 동일한 값"
        )
        
        return sigma_H
    
    def calculate_safety_factors(self, sigma_F_pinion: float, sigma_F_gear: float,
                               sigma_H: float, material: MaterialProperties) -> Tuple[float, float, float]:
        """안전계수 계산"""
        
        # 굽힘 안전계수 (구동기어)
        SF_pinion = material.allowable_bending / sigma_F_pinion
        self.add_calculation_step(
            description="구동기어 굽힘 안전계수 계산",
            formula="SF = σF,lim / σF",
            variables={
                "σF,lim": material.allowable_bending,
                "σF": sigma_F_pinion
            },
            calculation=f"SF = {material.allowable_bending}/{sigma_F_pinion:.1f}",
            result=SF_pinion,
            unit="-",
            notes="굽힘 안전계수는 1.5 이상 권장 (ISO 6336-3)"
        )
        
        # 굽힘 안전계수 (피동기어)  
        SF_gear = material.allowable_bending / sigma_F_gear
        self.add_calculation_step(
            description="피동기어 굽힘 안전계수 계산",
            formula="SF = σF,lim / σF",
            variables={
                "σF,lim": material.allowable_bending,
                "σF": sigma_F_gear
            },
            calculation=f"SF = {material.allowable_bending}/{sigma_F_gear:.1f}",
            result=SF_gear,
            unit="-",
            notes="피동기어는 일반적으로 더 높은 안전계수"
        )
        
        # 접촉 안전계수
        SH = material.allowable_contact / sigma_H
        self.add_calculation_step(
            description="접촉 안전계수 계산",
            formula="SH = σH,lim / σH",
            variables={
                "σH,lim": material.allowable_contact,
                "σH": sigma_H
            },
            calculation=f"SH = {material.allowable_contact}/{sigma_H:.1f}",
            result=SH,
            unit="-",
            notes="접촉 안전계수는 1.2 이상 권장 (ISO 6336-2)"
        )
        
        return SF_pinion, SF_gear, SH
    
    def generate_calculation_report(self) -> str:
        """상세 계산 과정 보고서 생성"""
        report = []
        report.append("# ISO 6336 기어 강도 계산 상세 과정\n")
        
        for i, step in enumerate(self.calculation_steps, 1):
            report.append(f"## 계산 단계 {step.step_number}: {step.description}\n")
            report.append(f"**적용 공식:** {step.formula}\n")
            report.append("**변수:**")
            for var, value in step.variables.items():
                if isinstance(value, float):
                    report.append(f"- {var} = {value:.3f}")
                else:
                    report.append(f"- {var} = {value}")
            report.append(f"\n**계산 과정:** {step.calculation}")
            report.append(f"**결과:** {step.result:.3f} {step.unit}")
            if step.notes:
                report.append(f"**참고:** {step.notes}")
            report.append("")  # 빈 줄
            
        return "\n".join(report)

def create_standard_gear_system(module: float, teeth_pinion: int, gear_ratio: float,
                               input_torque: float, input_speed: float) -> Tuple[GearGeometry, LoadConditions, MaterialProperties]:
    """표준 기어 시스템 생성"""
    
    teeth_gear = int(teeth_pinion * gear_ratio)
    
    geometry = GearGeometry(
        module=module,
        teeth_pinion=teeth_pinion,
        teeth_gear=teeth_gear,
        face_width=module * 10,  # 표준 치폭 = 10×모듈
        pressure_angle=20.0
    )
    
    power = input_torque * input_speed * 2 * math.pi / 60 / 1000  # kW
    
    load = LoadConditions(
        input_torque=input_torque,
        input_speed=input_speed,
        power=power
    )
    
    # SCM415 침탄강 표준 특성
    material = MaterialProperties(
        name="SCM415 침탄강",
        allowable_bending=280.0,  # MPa
        allowable_contact=750.0,  # MPa  
        elastic_modulus=206.0,   # GPa
        poisson_ratio=0.3,
        density=7850.0           # kg/m³
    )
    
    return geometry, load, material