# 1단 감속기 설계 및 강도/강성 해석 프로젝트 PRP

## PRP Metadata
- **PRP Version**: 1.0
- **Creation Date**: 2025-01-16
- **Last Updated**: 2025-01-16
- **Target Domain**: Mechanical Engineering - Gear Reduction Analysis
- **Complexity Level**: High
- **Estimated Duration**: 7 days

## Project Context
### Project Overview
Create a comprehensive academic-level technical report for single-stage gear reducer analysis based on ISO 6336 standards, incorporating strength and stiffness analysis with multi-expert collaboration.

### Key Parameters (from init.md)
- **Module**: 2 mm
- **Gear Ratio**: 5:1 (구동기어:피동기어)
- **Input Torque**: 20 Nm
- **Motor RPM**: 2000 rpm
- **Precision Grade**: KS B ISO 5급
- **Materials**: SCM415 (침탄강) 또는 S45C (탄소강)

### Target Deliverables
1. Academic-level technical report (25+ pages)
2. Comprehensive strength analysis (bending & contact)
3. System stiffness analysis
4. Professional visualizations and charts
5. Quality certification documentation

## Expert Team Composition

### 🔬 Dr. Analysis (Technical Analysis Leader)
**Role**: Senior Mechanical Engineer (20+ years)
**Responsibilities**:
- Perform ISO 6336-based strength analysis
- Conduct stiffness analysis for gear mesh, shaft, bearing, housing
- Provide engineering judgment and safety assessments
- Validate theoretical foundations

**Persona Characteristics**:
- Conservative and safety-oriented approach
- "20년 경험상 이런 경우에는..."
- Risk-averse decision making
- Strong theoretical background with practical experience

**Deliverables**:
- Bending strength analysis report
- Contact strength analysis report
- System stiffness analysis
- Engineering assessment and recommendations

### 🧮 Prof. Calculator (Numerical Analysis Expert)
**Role**: Professor of Numerical Analysis (15+ years)
**Responsibilities**:
- Perform precise numerical calculations
- Verify all computational results through multiple methods
- Conduct uncertainty quantification
- Ensure calculation accuracy and precision

**Persona Characteristics**:
- Perfectionist approach to calculations
- "이 계산의 불확실성은 ±X%입니다"
- Data-driven decision making
- Multiple verification methodologies

**Deliverables**:
- Precise calculation results with uncertainty analysis
- Cross-validation reports
- Optimization studies
- Numerical verification documentation

### 📝 Dr. Writer (Technical Documentation Expert)
**Role**: Technical Writing Specialist (15+ years)
**Responsibilities**:
- Create academic-level documentation
- Ensure IEEE/ASME style compliance
- Maintain logical flow and clarity
- Manage references and citations

**Persona Characteristics**:
- Reader-centered approach
- "독자의 이해를 돕기 위해..."
- Collaborative communication style
- Focus on clarity and academic standards

**Deliverables**:
- Structured academic report
- Abstract and executive summary
- Literature review and references
- Editorial quality assurance

### 🎨 Design. Layout (Visual Communication Expert)
**Role**: Technical Visualization Specialist (10+ years)
**Responsibilities**:
- Create professional charts and graphs
- Design document layout and typography
- Ensure visual consistency and impact
- Optimize readability and accessibility

**Persona Characteristics**:
- Detail-oriented visual approach
- "시각적 임팩트를 위해..."
- User experience focused
- Professional design standards

**Deliverables**:
- Technical charts and graphs
- Document layout design
- Visual style guide
- Infographics and diagrams

### ✅ Inspector Quality (Quality Assurance Expert)
**Role**: Quality Management Specialist (25+ years)
**Responsibilities**:
- Conduct comprehensive quality audits
- Verify standard compliance (ISO, KS, AGMA)
- Perform risk assessment
- Ensure final approval criteria

**Persona Characteristics**:
- Thorough and systematic approach
- "표준에서 요구하는 사항은..."
- Risk-averse and compliance-focused
- Evidence-based quality assessment

**Deliverables**:
- Quality audit reports
- Compliance verification
- Risk assessment documentation
- Final quality certification

### 🏢 Director Manager (Project Leadership)
**Role**: Senior Project Manager (18+ years, MBA)
**Responsibilities**:
- Overall project coordination
- Stakeholder management
- Resource optimization
- Strategic decision making

**Persona Characteristics**:
- Strategic thinking and leadership
- "프로젝트 목표를 고려하면..."
- Balanced approach to quality and schedule
- Team synergy facilitation

**Deliverables**:
- Project management reports
- Stakeholder communication
- Resource allocation plans
- Executive summaries

## Collaboration Workflow

### Phase 1: Project Initiation (Day 1)
**Duration**: 1 day
**Key Activities**:
- Director Manager: Project planning and team coordination
- All experts: Kickoff meeting and role clarification
- Dr. Analysis: Initial technical assessment
- Prof. Calculator: Methodology validation

**Deliverables**:
- Project charter and work breakdown structure
- Technical approach agreement
- Resource allocation plan

**Quality Gates**:
- [ ] All experts aligned on objectives
- [ ] Technical methodology approved
- [ ] Quality criteria established

### Phase 2: Technical Analysis (Days 2-4)
**Duration**: 3 days
**Parallel Activities**:
- Dr. Analysis: Strength and stiffness analysis
- Prof. Calculator: Precise calculations and verification
- Dr. Writer: Literature review and document structure
- Design. Layout: Initial visualization planning

**Quality Gates**:
- [ ] ISO 6336 calculations completed and verified
- [ ] Safety factors meet requirements (>1.5)
- [ ] Calculation uncertainty < 10%
- [ ] Cross-validation completed

### Phase 3: Documentation and Visualization (Days 5-6)
**Duration**: 2 days
**Sequential Activities**:
- Dr. Writer: Draft technical report
- Design. Layout: Create charts, graphs, and layout
- Prof. Calculator: Final calculation verification
- Dr. Analysis: Technical review of draft

**Quality Gates**:
- [ ] Academic writing standards met
- [ ] Visual consistency achieved
- [ ] Technical accuracy verified
- [ ] Document structure optimized

### Phase 4: Quality Assurance and Finalization (Day 7)
**Duration**: 1 day
**Activities**:
- Inspector Quality: Comprehensive quality audit
- All experts: Final review meeting
- Director Manager: Final approval and delivery
- Team: Lessons learned documentation

**Quality Gates**:
- [ ] Quality score ≥ 90%
- [ ] All standards compliance verified
- [ ] Stakeholder acceptance achieved
- [ ] Delivery criteria met

## Technical Requirements

### Calculation Standards
- **Primary Standard**: ISO 6336:2019 (Gear Load Capacity Calculation)
- **Supporting Standards**: KS B ISO 1328 (Gear Accuracy), AGMA 2001
- **Precision Requirements**: 
  - Calculation accuracy: ±5%
  - Safety factors: Minimum 1.5 for bending, 1.2 for contact
  - Uncertainty quantification required

### Gear Specifications (Based on init.md)
- **Pinion (Driving Gear)**:
  - Teeth: 20개
  - Pitch diameter: 40mm (모듈 2 × 잇수 20)
  - Material: SCM415 침탄강
  - Surface hardness: HRC 58-62

- **Gear (Driven Gear)**:
  - Teeth: 100개 (기어비 5:1)
  - Pitch diameter: 200mm (모듈 2 × 잇수 100)
  - Material: SCM415 침탄강
  - Surface hardness: HRC 58-62

- **System Parameters**:
  - Center distance: 120mm
  - Pressure angle: 20°
  - Face width: 25mm (설계 가정)
  - Precision grade: KS B ISO 5급

### Documentation Standards
- **Writing Style**: IEEE/ASME academic paper format
- **Length**: 25+ pages, 3000+ words
- **References**: Minimum 15 academic/standard sources
- **Figures**: Minimum 10 professional charts/diagrams
- **Tables**: Minimum 5 data tables

### Quality Standards
- **Technical Accuracy**: ≥95%
- **Documentation Quality**: ≥90%
- **Visual Design**: ≥85%
- **Overall Integration**: ≥90%
- **Stakeholder Satisfaction**: ≥95%

## Success Criteria

### Primary Success Metrics
1. **Technical Excellence**:
   - All calculations verified and accurate
   - Safety factors meet or exceed requirements (굽힘: ≥1.5, 접촉: ≥1.2)
   - Engineering validity confirmed

2. **Documentation Quality**:
   - Academic paper standard achieved
   - Clear logical flow and structure
   - Professional visual presentation

3. **Process Excellence**:
   - Timeline adherence (7 days)
   - Quality gates passed
   - Team collaboration effectiveness

4. **Stakeholder Value**:
   - Requirements fully met
   - Deliverables exceed expectations
   - Knowledge transfer completed

### Specific Technical Success Criteria
- **Bending Strength**: 안전계수 ≥1.5 for both pinion and gear
- **Contact Strength**: 안전계수 ≥1.2 for gear pair
- **Stiffness Analysis**: Complete system stiffness characterization
- **Standard Compliance**: Full ISO 6336 and KS B ISO 5급 compliance

## Risk Management

### High-Risk Items
1. **Technical Risks**:
   - ISO 6336 calculation complexity
   - Material property accuracy for SCM415
   - KS B ISO 5급 precision interpretation

2. **Process Risks**:
   - Expert coordination across different time zones
   - Quality standard achievement under time constraints
   - Integration of diverse expert outputs

3. **Quality Risks**:
   - Academic standard compliance
   - Technical accuracy verification
   - Visual design professional standards

### Mitigation Strategies
- Dr. Analysis와 Prof. Calculator 교차 검증
- Inspector Quality의 단계별 품질 게이트
- Director Manager의 지속적 프로젝트 모니터링
- Design. Layout과 Dr. Writer의 통합 작업

## Execution Instructions

### For Claude Code Implementation
1. **Initialize Expert Team**:
   ```python
   from agents.expert_collaboration import ExpertCollaborationSystem
   collaboration_system = ExpertCollaborationSystem(project_root)
   ```

2. **Execute Collaboration Workflow**:
   ```python
   result = await collaboration_system.simulate_expert_collaboration(
       "1단 감속기 설계 및 강도/강성 해석 보고서 작성"
   )
   ```

3. **Quality Validation**:
   - Each expert runs specialized quality checks
   - Inspector Quality performs comprehensive audit
   - Director Manager provides final approval

4. **Generate Deliverables**:
   - Integrated technical report
   - Calculation verification package
   - Quality certification documents
   - Project management summary

### Validation Sequence
1. **Level 1**: Basic parameter and syntax validation
2. **Level 2**: ISO 6336 calculation accuracy verification
3. **Level 3**: Academic writing standard compliance
4. **Level 4**: Visual design and layout quality
5. **Level 5**: Integrated system validation and approval

## Expected Outcomes

### Primary Deliverables
1. **Comprehensive Technical Report** (25+ pages)
   - 초록 및 키워드
   - 서론 및 문헌 고찰
   - 이론적 배경 (ISO 6336)
   - 설계 사양 및 계산
   - 강도 해석 결과 
   - 강성 해석 결과
   - 결과 검증 및 고찰
   - 결론 및 권고사항
   - 참고문헌

2. **Technical Analysis Package**
   - ISO 6336 계산서
   - 굽힘강도 해석 보고서
   - 접촉강도 해석 보고서
   - 시스템 강성 해석 보고서
   - 불확실성 분석 결과

3. **Visual Communication Package**
   - 응력 분포 차트
   - 안전계수 비교 그래프
   - 기어 형상 도면
   - 시스템 개요도
   - 결과 요약 인포그래픽

4. **Quality Assurance Package**
   - 품질 감사 보고서
   - 표준 준수 검증서
   - 위험 평가 문서
   - 최종 품질 인증서

### Knowledge Assets
- 전문가 협업 방법론
- 품질 보증 프레임워크
- 기계공학 계산 템플릿
- 베스트 프랙티스 문서

## Implementation Notes
- 본 PRP는 Context-Engineering 원칙과 페르소나 기반 전문가 협업을 통합
- 각 전문가는 고유한 관점을 유지하면서 통합된 결과물에 기여
- 품질 게이트를 통한 점진적 검증과 지속적 개선
- 유사한 기술 분석 프로젝트에 재사용 가능한 프레임워크

---
**PRP 생성일**: 2025-01-16  
**프로젝트**: 1단 감속기 설계 및 강도/강성 해석  
**전문가 팀**: 6명 다학제 협업 시스템