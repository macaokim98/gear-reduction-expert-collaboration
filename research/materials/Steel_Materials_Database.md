# 기어용 강재 데이터베이스
**Steel Materials Database for Gear Applications**

## 🔬 기어용 합금강 물성

### SCM440 (Cr-Mo 합금강)
**화학성분 (JIS G 4105)**
```
C: 0.38-0.43%    Si: 0.15-0.35%    Mn: 0.60-0.90%
Cr: 0.90-1.20%   Mo: 0.15-0.30%    P≤0.030%  S≤0.030%
```

#### 기계적 성질
| 조건 | 항복강도 | 인장강도 | 신율 | 단면수축률 | 경도 |
|------|----------|----------|------|-----------|------|
| 담금질뜨임 | 785 MPa | 930 MPa | 17% | 58% | 28-35 HRC |
| 침탄담금질(표면) | - | - | - | - | 58-62 HRC |
| 침탄담금질(심부) | 590 MPa | 780 MPa | 20% | 60% | 30-40 HRC |

#### 피로특성
$$\sigma_{-1} = 0.4 \times \sigma_B = 0.4 \times 930 = 372 \text{ MPa}$$

**굽힘 피로한도**: $\sigma_{F,all} = 480$ MPa (침탄품)  
**접촉 피로한도**: $\sigma_{H,all} = 1300$ MPa (침탄품)

### SNCM420 (Ni-Cr-Mo 합금강)
**화학성분 (JIS G 4103)**
```
C: 0.17-0.23%    Si: 0.15-0.35%    Mn: 0.45-0.75%
Ni: 1.65-2.00%   Cr: 0.40-0.65%    Mo: 0.15-0.30%
```

#### 기계적 성질
| 조건 | 항복강도 | 인장강도 | 신율 | 단면수축률 | 경도 |
|------|----------|----------|------|-----------|------|
| 담금질뜨임 | 880 MPa | 1080 MPa | 15% | 55% | 32-39 HRC |
| 침탄담금질(표면) | - | - | - | - | 58-64 HRC |
| 침탄담금질(심부) | 690 MPa | 880 MPa | 18% | 58% | 35-42 HRC |

#### 피로특성
**굽힘 피로한도**: $\sigma_{F,all} = 520$ MPa (침탄품)  
**접촉 피로한도**: $\sigma_{H,all} = 1400$ MPa (침탄품)

### S45C (탄소강)
**화학성분 (JIS G 4051)**
```
C: 0.42-0.48%    Si: 0.15-0.35%    Mn: 0.60-0.90%
P≤0.030%        S≤0.035%
```

#### 기계적 성질
| 조건 | 항복강도 | 인장강도 | 신율 | 단면수축률 | 경도 |
|------|----------|----------|------|-----------|------|
| 정규화 | 345 MPa | 570 MPa | 20% | 40% | 170-220 HB |
| 담금질뜨임 | 490 MPa | 686 MPa | 17% | 40% | 201-269 HB |

#### 피로특성
**굽힘 피로한도**: $\sigma_{F,all} = 280$ MPa (담금질뜨임)  
**접촉 피로한도**: $\sigma_{H,all} = 900$ MPa (담금질뜨임)

## 🏠 하우징용 주철 데이터

### FC250 (회주철)
**화학성분 (JIS G 5501)**
```
C: 2.9-3.7%     Si: 1.4-2.3%     Mn: 0.5-1.0%
P≤0.15%         S≤0.12%
```

#### 기계적 성질
| 항목 | 값 | 단위 |
|------|----|----- |
| 인장강도 | 250 | MPa |
| 압축강도 | 900 | MPa |
| 굽힘강도 | 400 | MPa |
| 탄성계수 | 100 | GPa |
| 밀도 | 7.2 | g/cm³ |

### FCD450 (구상흑연주철)
**화학성분 (JIS G 5502)**
```
C: 3.4-3.8%     Si: 2.2-2.8%     Mn: 0.3-0.7%
```

#### 기계적 성질
| 항목 | 값 | 단위 |
|------|----|----- |
| 인장강도 | 450 | MPa |
| 항복강도 | 310 | MPa |
| 신율 | 10 | % |
| 경도 | 150-230 | HB |

## 🔥 열처리 조건

### 침탄 담금질 (Carburizing)
**적용재료**: SCM440, SNCM420

#### 공정조건
1. **침탄**: 920-930°C, 6-8시간, CP분위기
   - 침탄깊이: 0.8-1.2mm
   - 표면탄소농도: 0.8-1.0%

2. **직접담금질**: 820-850°C → 유냉
   - 냉각속도: >30°C/min
   - Ms점: 약 200°C

3. **뜨임**: 150-180°C, 2시간
   - 잔류응력 제거
   - 치수안정화

#### 품질관리
- **경도시험**: HRC (표면), HV (단면)
- **침탄깊이**: 0.5%C 기준으로 측정
- **미세조직**: 마르텐사이트 + 잔류오스테나이트

### 담금질 뜨임 (Quench & Tempering)
**적용재료**: S45C, SCM440

#### 공정조건
1. **담금질**: 830-870°C → 유냉/수냉
2. **뜨임**: 600-650°C, 2시간 → 공냉

## 📊 재료 선정 기준

### 토크별 권장재료
$$T_{max} = \frac{\sigma_{F,all} \cdot m^3 \cdot Z \cdot Y \cdot b}{K_{total}}$$

| 입력토크 | 권장재료 | 열처리 | 비고 |
|----------|---------|--------|------|
| <50 Nm | S45C | 담금질뜨임 | 경제적 |
| 50-200 Nm | SCM440 | 침탄담금질 | 표준적 |
| >200 Nm | SNCM420 | 침탄담금질 | 고강도 |

### 속도별 권장사양
| 피치선속도 | 표면조도 | 정밀도등급 | 윤활방식 |
|-----------|----------|-----------|---------|
| <5 m/s | Ra 3.2 | JIS 8급 | 그리스 |
| 5-15 m/s | Ra 1.6 | JIS 7급 | 오일침지 |
| >15 m/s | Ra 0.8 | JIS 6급 | 강제순환 |

---

**데이터 출처**: JIS G 4051/4103/4105, AGMA 2001-D04  
**최종수정**: 2025-07-15  
**검토자**: Materials Engineer