#!/usr/bin/env python3
"""
Python Student Competence Analysis: Evaluation Framework
A demonstration of the proposed approach for evaluating open source models.
"""

import ast
import json
from typing import List, Dict, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class CodeAnalysisResult:
    """Results from analyzing student code"""
    syntax_errors: List[str]
    logical_issues: List[str]
    misconceptions: List[str]
    complexity_score: float
    confidence: float

@dataclass
class GeneratedPrompt:
    """A generated competence assessment prompt"""
    text: str
    category: str  # "conceptual", "debugging", "extension"
    difficulty_level: int  # 1-5
    learning_objective: str

class CodeAnalyzer(ABC):
    """Abstract base class for code analysis"""
    
    @abstractmethod
    def analyze(self, code: str) -> CodeAnalysisResult:
        pass

class BasicPythonAnalyzer(CodeAnalyzer):
    """Basic analyzer using AST and common patterns"""
    
    def analyze(self, code: str) -> CodeAnalysisResult:
        syntax_errors = []
        logical_issues = []
        misconceptions = []
        
        try:
            # Parse the code
            tree = ast.parse(code)
            
            # Basic analysis
            complexity = self._calculate_complexity(tree)
            syntax_errors = self._check_syntax_issues(code)
            misconceptions = self._detect_common_misconceptions(tree, code)
            
        except SyntaxError as e:
            syntax_errors.append(f"Syntax error: {str(e)}")
            
        return CodeAnalysisResult(
            syntax_errors=syntax_errors,
            logical_issues=logical_issues,
            misconceptions=misconceptions,
            complexity_score=complexity,
            confidence=0.8
        )
    
    def _calculate_complexity(self, tree: ast.AST) -> float:
        """Calculate basic complexity score"""
        complexity = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While, ast.If)):
                complexity += 1
            elif isinstance(node, ast.FunctionDef):
                complexity += 2
        return min(complexity / 10.0, 1.0)
    
    def _check_syntax_issues(self, code: str) -> List[str]:
        """Check for common syntax issues"""
        issues = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            if '=' in line and '==' not in line and '!=' not in line:
                # Check if assignment might be confused with equality
                if 'if ' in line:
                    issues.append(f"Line {i}: Possible assignment in condition")
                    
        return issues
    
    def _detect_common_misconceptions(self, tree: ast.AST, code: str) -> List[str]:
        """Detect common Python misconceptions"""
        misconceptions = []
        
        # Check for common issues
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check for missing return statement
                has_return = any(isinstance(n, ast.Return) for n in ast.walk(node))
                if not has_return and node.name != '__init__':
                    misconceptions.append("Function may be missing return statement")
                    
        return misconceptions

class PromptGenerator(ABC):
    """Abstract base class for prompt generation"""
    
    @abstractmethod
    def generate_prompts(self, code: str, analysis: CodeAnalysisResult) -> List[GeneratedPrompt]:
        pass

class RuleBasedPromptGenerator(PromptGenerator):
    """Rule-based prompt generator for demonstration"""
    
    def generate_prompts(self, code: str, analysis: CodeAnalysisResult) -> List[GeneratedPrompt]:
        prompts = []
        
        # Generate prompts based on analysis
        if analysis.syntax_errors:
            prompts.append(GeneratedPrompt(
                text="Look at your code structure. Can you identify any syntax issues? What might Python be expecting differently?",
                category="debugging",
                difficulty_level=2,
                learning_objective="Syntax error identification and resolution"
            ))
        
        if "assignment in condition" in str(analysis.syntax_errors):
            prompts.append(GeneratedPrompt(
                text="In your conditional statement, consider the difference between assignment (=) and comparison (==). Which operation do you intend to perform?",
                category="conceptual",
                difficulty_level=3,
                learning_objective="Understanding assignment vs equality operators"
            ))
            
        if "missing return statement" in str(analysis.misconceptions):
            prompts.append(GeneratedPrompt(
                text="Think about what your function should give back to the caller. What value or result should it return?",
                category="conceptual", 
                difficulty_level=3,
                learning_objective="Function return values and program flow"
            ))
            
        if analysis.complexity_score > 0.5:
            prompts.append(GeneratedPrompt(
                text="Your solution shows good complexity. Can you explain the logic flow? How would you trace through it step by step?",
                category="extension",
                difficulty_level=4,
                learning_objective="Algorithm analysis and explanation"
            ))
            
        return prompts

class CompetenceEvaluator:
    """Main evaluation framework"""
    
    def __init__(self, analyzer: CodeAnalyzer, prompt_generator: PromptGenerator):
        self.analyzer = analyzer
        self.prompt_generator = prompt_generator
        
    def evaluate_student_code(self, code: str) -> Dict[str, Any]:
        """Complete evaluation of student code"""
        
        # Analyze the code
        analysis = self.analyzer.analyze(code)
        
        # Generate prompts
        prompts = self.prompt_generator.generate_prompts(code, analysis)
        
        # Create evaluation report
        return {
            "code": code,
            "analysis": {
                "syntax_errors": analysis.syntax_errors,
                "logical_issues": analysis.logical_issues,
                "misconceptions": analysis.misconceptions,
                "complexity_score": analysis.complexity_score,
                "confidence": analysis.confidence
            },
            "generated_prompts": [
                {
                    "text": p.text,
                    "category": p.category,
                    "difficulty": p.difficulty_level,
                    "objective": p.learning_objective
                }
                for p in prompts
            ],
            "summary": {
                "total_prompts": len(prompts),
                "categories": list(set(p.category for p in prompts)),
                "avg_difficulty": sum(p.difficulty_level for p in prompts) / len(prompts) if prompts else 0
            }
        }

def demonstrate_evaluation():
    """Demonstrate the evaluation framework"""
    
    # Sample student code with common issues
    sample_codes = [
        # Code with assignment in condition
        """
def check_number(x):
    if x = 5:
        return "equal"
    else:
        return "not equal"
        """,
        
        # Code missing return statement
        """
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        """,
        
        # More complex but correct code
        """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        """
    ]
    
    # Initialize evaluator
    analyzer = BasicPythonAnalyzer()
    prompt_gen = RuleBasedPromptGenerator()
    evaluator = CompetenceEvaluator(analyzer, prompt_gen)
    
    print("Python Student Competence Analysis - Demonstration")
    print("=" * 60)
    
    for i, code in enumerate(sample_codes, 1):
        print(f"\nExample {i}:")
        print("-" * 40)
        print("Student Code:")
        print(code.strip())
        
        try:
            result = evaluator.evaluate_student_code(code.strip())
            
            print(f"\nAnalysis Results:")
            print(f"  Syntax Errors: {len(result['analysis']['syntax_errors'])}")
            print(f"  Misconceptions: {len(result['analysis']['misconceptions'])}")
            print(f"  Complexity Score: {result['analysis']['complexity_score']:.2f}")
            
            print(f"\nGenerated Prompts ({result['summary']['total_prompts']}):")
            for j, prompt in enumerate(result['generated_prompts'], 1):
                print(f"  {j}. [{prompt['category'].title()}] {prompt['text']}")
                print(f"     Difficulty: {prompt['difficulty']}/5")
                print()
                
        except Exception as e:
            print(f"Error analyzing code: {e}")
    
    print("\nThis demonstration shows how the framework can:")
    print("• Analyze Python code for common issues")
    print("• Detect potential misconceptions") 
    print("• Generate targeted prompts for learning")
    print("• Classify prompts by category and difficulty")
    print("\nNext steps: Integration with CodeT5+ for advanced prompt generation")

if __name__ == "__main__":
    demonstrate_evaluation()
