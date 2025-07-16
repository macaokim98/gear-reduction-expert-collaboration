# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Gear Reduction Report Expert Collaboration System** - an advanced project that simulates 6 expert personas collaborating on mechanical engineering gear analysis reports using Git Worktree workflows. The system produces academic-level technical documentation for gear reduction systems.

### System Architecture

The project implements a **multi-agent expert collaboration system** with the following key components:

- **6 Expert Personas**: Dr. Analysis, Prof. Calculator, Dr. Writer, Design Layout, Inspector Quality, Director Manager
- **Git Worktree Integration**: Parallel development across multiple worktrees for each expert
- **Persona-Based AI System**: Each agent has specialized knowledge, personality, and working patterns
- **Context-Engineering Framework**: PRP-based systematic development methodology
- **Quality Gate System**: Multi-stage validation and verification processes

## Core Architecture

### Agent System Structure
```
agents/
├── base_agent.py              # Base agent class with orchestration
├── persona_base.py            # Persona framework and expert panel system
├── expert_collaboration.py    # Meeting simulation and consensus building
├── dr_analysis.py            # Mechanical engineering analysis expert
├── prof_calculator.py        # Numerical computation and verification expert
├── dr_writer.py             # Academic writing and documentation expert
├── design_layout.py         # Visualization and design expert
├── inspector_quality.py     # Quality assurance and compliance expert
└── director_manager.py       # Project management and coordination expert
```

### Git Worktree Structure
```
worktrees/
├── dr-analysis/              # Dr. Analysis workspace
├── prof-calculator/          # Prof. Calculator workspace
├── dr-writer/                # Dr. Writer workspace
├── design-layout/            # Design Layout workspace
├── inspector-quality/        # Inspector Quality workspace
├── director-manager/         # Director Manager workspace
├── integration-phase-1/      # Phase 1 integration (analysis + calculation)
├── integration-phase-2/      # Phase 2 integration (documentation + design)
├── integration-phase-3/      # Phase 3 integration (quality verification)
└── final-release/           # Final report release
```

## Common Development Commands

### Git Worktree Management
```bash
# Set up the complete worktree environment
./git-workflow/setup-worktrees.sh

# Check status across all worktrees
./git-workflow/status-report.sh

# Integrate specific phase
./git-workflow/integrate-phase.sh phase-1
./git-workflow/integrate-phase.sh phase-2
./git-workflow/integrate-phase.sh phase-3
./git-workflow/integrate-phase.sh final
```

### Working with Specific Expert Worktrees
```bash
# Work in a specific expert's workspace
cd worktrees/dr-analysis          # For strength analysis work
cd worktrees/prof-calculator      # For numerical calculations
cd worktrees/dr-writer           # For document writing
cd worktrees/design-layout       # For visualization work
cd worktrees/inspector-quality   # For quality assurance
cd worktrees/director-manager    # For project management

# Each expert workspace has dedicated directories:
# - analysis/, calculations/, results/ (dr-analysis)
# - calculations/, verification/, uncertainty/ (prof-calculator)
# - drafts/, references/, templates/ (dr-writer)
# - charts/, diagrams/, layouts/ (design-layout)
# - audits/, compliance/, risk-assessment/ (inspector-quality)
# - planning/, coordination/, monitoring/ (director-manager)
```

### Running the Expert Collaboration System
```bash
# Run individual expert agents
python agents/dr_analysis.py
python agents/prof_calculator.py
python agents/dr_writer.py

# Run the full collaboration simulation
python agents/expert_collaboration.py

# Run the agent orchestrator
python agents/base_agent.py
```

## Project Parameters

The project focuses on **1-stage gear reduction system analysis** with these specifications:
- **Module**: 2 mm
- **Gear Ratio**: 5:1 (driving:driven gear)
- **Input Torque**: 20 Nm
- **Motor Speed**: 2000 rpm
- **Gear Standard**: KS B ISO 5 grade
- **Materials**: SCM415 (carburized steel) or S45C (carbon steel)
- **Heat Treatment**: Carburizing/quenching/tempering
- **Lubrication**: Gear oil or grease

## Key Engineering Standards

The system follows these technical standards:
- **ISO 6336**: Gear strength calculation standards
- **AGMA Standards**: American gear manufacturing standards
- **KS B ISO 5**: Korean gear standards
- **IEEE/ASME**: Documentation style standards

## Expert Collaboration Workflow

### Phase 1: Technical Analysis (Days 1-3)
- **Dr. Analysis**: Performs ISO 6336-based strength analysis, system stiffness analysis
- **Prof. Calculator**: Executes precise numerical calculations, multi-methodology verification
- **Integration**: Technical verification and calculation coordination

### Phase 2: Documentation (Days 4-5)
- **Dr. Writer**: Creates IEEE/ASME style academic documentation
- **Design Layout**: Develops professional visualization and layout design
- **Integration**: Documentation and visualization integration

### Phase 3: Quality Verification (Days 6-7)
- **Inspector Quality**: Comprehensive quality auditing, standard compliance verification
- **Director Manager**: Final review, stakeholder management
- **Integration**: Final quality certification and project approval

## Meeting Protocols

The system simulates realistic expert meetings:
- **Kickoff Meeting**: Project overview, role assignment (60 min)
- **Technical Review**: Calculation review, methodology discussion (45 min)
- **Design Review**: Document structure, visualization planning (30 min)
- **Quality Review**: Quality standards, verification results (45 min)
- **Final Review**: Final approval, next steps (30 min)

## Quality Standards

Each component undergoes multi-stage quality verification:
- **Technical Accuracy**: ≥95% calculation precision
- **Standard Compliance**: Full ISO/AGMA/KS adherence
- **Document Quality**: Academic publication level
- **Visual Design**: Professional engineering standards
- **Team Consensus**: ≥85% agreement threshold

## File Organization

### Project Structure
```
/
├── agents/                    # Expert agent implementations
├── PRPs/                     # Context-Engineering templates
├── git-workflow/             # Git worktree automation scripts
├── worktrees/               # Individual expert workspaces
├── research/                # Technical reference materials
├── reports/                 # Generated technical reports
├── logs/                    # System operation logs
└── init.md                  # Project parameters and guidelines
```

### Research Materials
- `research/standards/`: AGMA, ISO, KS standards documentation
- `research/materials/`: Steel materials database
- `research/manufacturers/`: Bearing catalogs
- `research/case_studies/`: Gearbox design case studies
- `research/papers/`: Academic writing style guides

## Development Best Practices

### When Working with Agents
1. **Always check context**: Each agent requires proper context initialization
2. **Follow persona patterns**: Respect each expert's specialization and working style
3. **Use quality gates**: Validate outputs through the multi-stage verification system
4. **Maintain standards**: Ensure all technical work follows ISO/AGMA/KS standards

### When Working with Git Worktrees
1. **Use automation scripts**: Prefer `setup-worktrees.sh` over manual commands
2. **Check status regularly**: Use `status-report.sh` for progress monitoring
3. **Integrate systematically**: Follow the phase-based integration approach
4. **Resolve conflicts carefully**: Maintain technical accuracy over convenience

### When Generating Reports
1. **Academic rigor**: Maintain IEEE/ASME documentation standards
2. **Technical accuracy**: All calculations must be ISO 6336 compliant
3. **Professional presentation**: Use consistent visualization and layout standards
4. **Comprehensive validation**: Include uncertainty analysis and safety factors

## Specialized Tools and Capabilities

### Expert Agent Features
- **Persona-based responses**: Each agent responds according to their professional background
- **Meeting simulation**: Realistic expert panel discussions and consensus building
- **Quality scoring**: Automated quality assessment for all outputs
- **Collaboration patterns**: Peer review, sequential workflow, parallel task execution

### Technical Capabilities
- **Multi-methodology verification**: Cross-validation using ISO, FEM, and AGMA approaches
- **Uncertainty quantification**: Monte Carlo simulation with confidence intervals
- **Professional visualization**: Engineering-grade charts, diagrams, and layouts
- **Standard compliance**: Automated verification against international standards

## Context-Engineering Integration

This project demonstrates advanced **Context-Engineering methodology**:
- **PRP-based development**: Problem-Resource-Process structured approach
- **Persona-driven collaboration**: Expert knowledge simulation and interaction
- **Quality-gated progression**: Systematic validation at each development stage
- **Evidence-based methodology**: Quantitative metrics and verification standards

The system serves as a reference implementation for complex multi-agent collaboration in technical domains, particularly mechanical engineering and academic report generation.