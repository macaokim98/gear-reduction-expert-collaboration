"""
Base Agent Class for Gear Reduction Report System
감속기 보고서 시스템을 위한 기본 에이전트 클래스
"""

import asyncio
import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentContext:
    """에이전트 컨텍스트 정보"""
    project_root: Path
    current_phase: str
    parameters: Dict[str, Any]
    previous_results: Dict[str, Any]
    quality_gates: List[str]
    timestamp: datetime = datetime.now()

@dataclass
class AgentResult:
    """에이전트 실행 결과"""
    agent_name: str
    success: bool
    output_data: Dict[str, Any]
    quality_score: float
    errors: List[str]
    warnings: List[str]
    execution_time: float
    next_steps: List[str]

class BaseAgent(ABC):
    """모든 에이전트의 기본 클래스"""
    
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        self.context: Optional[AgentContext] = None
        self.tools: Dict[str, Any] = {}
        self.quality_standards = {}
        
    def set_context(self, context: AgentContext):
        """컨텍스트 설정"""
        self.context = context
        logger.info(f"[{self.name}] 컨텍스트 설정 완료: {context.current_phase}")
    
    def add_tool(self, tool_name: str, tool_function):
        """도구 추가 (Agent-as-Tool 패턴)"""
        self.tools[tool_name] = tool_function
        logger.info(f"[{self.name}] 도구 추가: {tool_name}")
    
    @abstractmethod
    async def execute(self, task: str, **kwargs) -> AgentResult:
        """에이전트 실행 (하위 클래스에서 구현)"""
        pass
    
    async def validate_input(self, task: str, **kwargs) -> bool:
        """입력 검증"""
        if not self.context:
            logger.error(f"[{self.name}] 컨텍스트가 설정되지 않음")
            return False
        
        if not task.strip():
            logger.error(f"[{self.name}] 작업 내용이 비어있음")
            return False
            
        return True
    
    async def run_quality_checks(self, output_data: Dict[str, Any]) -> tuple[float, List[str], List[str]]:
        """품질 검사 실행"""
        score = 1.0
        errors = []
        warnings = []
        
        # 기본 품질 검사
        if not output_data:
            errors.append("출력 데이터가 없음")
            score = 0.0
        
        # 전문 분야별 품질 검사 (하위 클래스에서 오버라이드)
        specialized_score, specialized_errors, specialized_warnings = await self.specialized_quality_check(output_data)
        
        score = min(score, specialized_score)
        errors.extend(specialized_errors)
        warnings.extend(specialized_warnings)
        
        return score, errors, warnings
    
    async def specialized_quality_check(self, output_data: Dict[str, Any]) -> tuple[float, List[str], List[str]]:
        """전문 분야별 품질 검사 (하위 클래스에서 구현)"""
        return 1.0, [], []
    
    def save_result(self, result: AgentResult, output_path: Optional[Path] = None):
        """결과 저장"""
        if not output_path:
            output_path = self.context.project_root / "outputs" / f"{self.name}_results"
            output_path.mkdir(parents=True, exist_ok=True)
        
        result_file = output_path / f"{result.agent_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        result_dict = {
            "agent_name": result.agent_name,
            "success": result.success,
            "output_data": result.output_data,
            "quality_score": result.quality_score,
            "errors": result.errors,
            "warnings": result.warnings,
            "execution_time": result.execution_time,
            "next_steps": result.next_steps,
            "timestamp": datetime.now().isoformat()
        }
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=2)
        
        logger.info(f"[{self.name}] 결과 저장 완료: {result_file}")

class AgentOrchestrator:
    """에이전트 오케스트레이터 - 다중 에이전트 협업 관리"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.agents: Dict[str, BaseAgent] = {}
        self.execution_graph: Dict[str, List[str]] = {}
        
    def register_agent(self, agent: BaseAgent):
        """에이전트 등록"""
        self.agents[agent.name] = agent
        logger.info(f"에이전트 등록: {agent.name} ({agent.specialization})")
    
    def set_execution_order(self, execution_graph: Dict[str, List[str]]):
        """실행 순서 설정"""
        self.execution_graph = execution_graph
        logger.info(f"실행 그래프 설정: {execution_graph}")
    
    async def execute_workflow(self, context: AgentContext, task: str) -> Dict[str, AgentResult]:
        """워크플로우 실행"""
        results = {}
        
        # 모든 에이전트에 컨텍스트 설정
        for agent in self.agents.values():
            agent.set_context(context)
        
        # 실행 순서에 따라 에이전트 실행
        executed = set()
        
        async def execute_agent(agent_name: str):
            if agent_name in executed:
                return
            
            # 의존성 에이전트 먼저 실행
            dependencies = self.execution_graph.get(agent_name, [])
            for dep in dependencies:
                if dep not in executed:
                    await execute_agent(dep)
            
            # 현재 에이전트 실행
            agent = self.agents[agent_name]
            logger.info(f"에이전트 실행 시작: {agent_name}")
            
            start_time = datetime.now()
            result = await agent.execute(task)
            execution_time = (datetime.now() - start_time).total_seconds()
            
            result.execution_time = execution_time
            results[agent_name] = result
            executed.add(agent_name)
            
            # 결과 저장
            agent.save_result(result)
            
            logger.info(f"에이전트 실행 완료: {agent_name} (성공: {result.success})")
        
        # 모든 에이전트 실행
        for agent_name in self.agents.keys():
            await execute_agent(agent_name)
        
        return results

# 유틸리티 함수들
def load_project_parameters(init_file: Path) -> Dict[str, Any]:
    """init.md에서 프로젝트 파라미터 로드"""
    if not init_file.exists():
        return {}
    
    parameters = {}
    with open(init_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # 간단한 파라미터 파싱 (향후 더 정교하게 개선 가능)
        lines = content.split('\n')
        for line in lines:
            if '**모듈**:' in line:
                parameters['module'] = line.split(':')[-1].strip()
            elif '**기어비**:' in line:
                parameters['gear_ratio'] = line.split(':')[-1].strip()
            elif '**입력토크**:' in line:
                parameters['input_torque'] = line.split(':')[-1].strip()
            elif '**모터회전수**:' in line:
                parameters['motor_rpm'] = line.split(':')[-1].strip()
    
    return parameters

def create_agent_context(project_root: Path, phase: str) -> AgentContext:
    """에이전트 컨텍스트 생성"""
    parameters = load_project_parameters(project_root / "init.md")
    
    return AgentContext(
        project_root=project_root,
        current_phase=phase,
        parameters=parameters,
        previous_results={},
        quality_gates=[
            "syntax_check",
            "parameter_validation", 
            "calculation_accuracy",
            "standard_compliance",
            "quality_review"
        ]
    )