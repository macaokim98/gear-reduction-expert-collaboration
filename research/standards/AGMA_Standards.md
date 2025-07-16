# AGMA Standards Database
**American Gear Manufacturers Association 표준 데이터베이스**

## 📋 주요 AGMA 표준

### AGMA 2001-D04: Fundamental Rating Factors and Calculation Methods
**기어 기본 설계 인자 및 계산법**

#### 루이스 굽힘 응력 공식
$$\sigma_b = \frac{F_t}{bmY} \cdot K_v \cdot K_s \cdot K_m \cdot K_B$$

**여기서:**
- $\sigma_b$ = 굽힘 응력 (MPa)
- $F_t$ = 전달하중 (N)  
- $b$ = 치폭 (mm)
- $m$ = 모듈 (mm)
- $Y$ = 루이스 폼 팩터
- $K_v$ = 동하중 계수
- $K_s$ = 크기 계수  
- $K_m$ = 하중분배 계수
- $K_B$ = 림 두께 계수

#### 동하중 계수 (Kv) 계산
$$K_v = \left(\frac{A + \sqrt{v}}{A}\right)^B$$

**여기서:**
- $v$ = 피치선속도 (m/s)
- $A$ = 50 + 56(1-B)
- $B$ = 0.25(12-Q_v)^{2/3}$
- $Q_v$ = 기어 품질지수

### AGMA 2101-D04: Fundamental Rating Factors for Contact Stress
**접촉 응력 기본 설계 인자**

#### 헤르츠 접촉 응력 공식
$$\sigma_H = Z_E \sqrt{\frac{F_t}{bd_1} \cdot \frac{Z_R}{Z_I} \cdot K_v \cdot K_s \cdot K_m \cdot K_H}$$

**여기서:**
- $\sigma_H$ = 접촉 응력 (MPa)
- $Z_E$ = 탄성계수 인자
- $d_1$ = 피니언 피치원 직경 (mm)
- $Z_R$ = 곡률 인자
- $Z_I$ = 기하 인자
- $K_H$ = 하중분배 계수

#### 탄성계수 인자 (ZE)
$$Z_E = \sqrt{\frac{1}{\pi \left[\frac{1-\nu_1^2}{E_1} + \frac{1-\nu_2^2}{E_2}\right]}}$$

**일반적인 값 (강재):**
- $Z_E = 191$ (MPa)^{1/2}

## 📊 허용응력 기준

### 굽힘 피로강도
| 재료 | 열처리 | 표면경도 | $\sigma_{F,all}$ (MPa) |
|------|--------|----------|----------------------|
| SCM440 | 침탄담금질 | 58-62 HRC | 480-520 |
| SNCM420 | 침탄담금질 | 58-62 HRC | 520-560 |
| S45C | 담금질뜨임 | 28-35 HRC | 280-320 |

### 접촉 피로강도  
| 재료 | 열처리 | 표면경도 | $\sigma_{H,all}$ (MPa) |
|------|--------|----------|----------------------|
| SCM440 | 침탄담금질 | 58-62 HRC | 1200-1400 |
| SNCM420 | 침탄담금질 | 58-62 HRC | 1300-1500 |
| S45C | 담금질뜨임 | 28-35 HRC | 800-1000 |

## 🔧 설계 가이드라인

### 기어비 권장범위
- **1단 감속**: 3:1 ~ 8:1
- **다단 감속**: 각 단 6:1 이하

### 모듈 선정 기준
$$m \geq \sqrt[3]{\frac{T_1 \cdot K}{Z_1 \cdot \sigma_{F,all} \cdot Y}}$$

**여기서:**
- $T_1$ = 입력토크 (Nm)
- $K$ = 종합 하중계수 (1.5-2.5)
- $Z_1$ = 피니언 잇수

### 중심거리 계산
$$a = \frac{m(Z_1 + Z_2)}{2}$$

## 📐 품질 기준

### 기어 정밀도 등급 (AGMA)
| 등급 | 용도 | 피치선속도 | 소음수준 |
|------|------|-----------|---------|
| Q6-Q8 | 고정밀 | >25 m/s | <55 dB |
| Q9-Q11 | 일반정밀 | 5-25 m/s | 55-65 dB |
| Q12-Q14 | 저정밀 | <5 m/s | >65 dB |

---

**참조**: AGMA 2001-D04, AGMA 2101-D04, AGMA 915-1-A02  
**최종수정**: 2025-07-15  
**검토자**: Research Engineer