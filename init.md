# 1단 감속기 보고서 파라미터

## 기본 설계 파라미터
- **모듈**: 2 mm
- **기어비**: 5:1 (구동기어:피동기어)
- **입력토크**: 20 Nm
- **모터회전수**: 2000 rpm
- **기어 규격**: KS B ISO 5급

## 계산용 파라미터
- **출력토크**: 100 Nm (기어비 × 입력토크 × 효율)
- **출력회전수**: 400 rpm (입력회전수 ÷ 기어비)
- **기어 효율**: 0.95 (가정)

## 강도 계산 필요 항목
1. 굽힘강도 (Bending Strength)
2. 접촉강도 (Contact Strength)  
3. 피팅강도 (Pitting Resistance)
4. 비틀림강도 (Torsional Strength)

## 강성 계산 필요 항목
1. 기어 치면강성 (Gear Mesh Stiffness)
2. 축 비틀림강성 (Shaft Torsional Stiffness)
3. 베어링 강성 (Bearing Stiffness)
4. 하우징 강성 (Housing Stiffness)

## 추가 설계 고려사항
- 재료: SCM415 (침탄강) 또는 S45C (탄소강)
- 열처리: 침탄/담금질/템퍼링
- 정밀도: KS B ISO 5급
- 윤활: 기어오일 또는 그리스

## 보고서 작성 스타일 가이드

### 학술 논문 수준 작성 지침
본 감속기 보고서는 학술 논문 수준의 체계적이고 전문적인 문체로 작성되어야 합니다.

#### 기본 문체 원칙
- **객관적 서술**: 1인칭 사용 금지, 수동태 선호
- **정확한 기술 용어**: AGMA, ISO, KS 표준 용어 사용
- **정량적 표현**: 수치, 공식, 그래프를 통한 정확한 설명
- **논리적 전개**: 가설 → 방법론 → 결과 → 고찰 순서

#### 보고서 구조
```
1. 초록 (Abstract)
2. 서론 (Introduction)
3. 이론적 배경 (Theoretical Background)
4. 설계 및 해석 방법론 (Design and Analysis Methodology)
5. 결과 및 분석 (Results and Analysis)
6. 고찰 (Discussion)
7. 결론 (Conclusion)
8. 참고문헌 (References)
```

#### 문장 구조 특징
- 전문적이고 정확한 기술 용어 사용
- 수식과 계산 과정의 명확한 설명
- 표와 그래프를 활용한 정량적 분석
- 국제 표준 및 관련 연구 문헌 인용

#### 품질 기준
- 모든 계산에 ISO 6336, AGMA, KS 표준 적용
- 안전계수 및 허용응력 명시
- 설계 타당성 검증 포함
- 참고문헌 및 표준 문서 인용

**상세 작성 가이드**: `/research/papers/Academic_Writing_Style_Guide.md` 참조

