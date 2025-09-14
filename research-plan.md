# Research Plan: Open Source Model Evaluation for Python Student Competence Analysis

## Approach to Model Identification and Evaluation

My approach will begin with a systematic survey of open source models across three key categories: general-purpose LLMs (Llama 2/3, Mistral, CodeLlama), specialized code analysis tools (tree-sitter parsers, AST analyzers), and educational AI frameworks (Open edX plugins, AutoGrader systems). I will prioritize models that demonstrate strong performance in code understanding tasks, such as CodeT5+ for code-text generation and CodeBERT for semantic code analysis, while also examining lighter-weight solutions like static analysis tools combined with rule-based systems. The evaluation will focus on models that can be locally deployed or accessed through free APIs, ensuring accessibility for educational institutions with limited resources.

The validation process will involve creating a diverse dataset of Python code samples representing different competency levels, from basic syntax errors to advanced algorithmic thinking gaps. I will test each model's ability to generate targeted prompts that probe conceptual understanding rather than surface-level debugging, evaluate their capacity to identify specific misconceptions (like confusing assignment with equality, or misunderstanding scope), and assess whether their feedback encourages metacognitive reflection. The testing framework will include both automated metrics (prompt relevance scoring, misconception detection accuracy) and qualitative evaluation through expert review, ensuring that generated prompts align with established pedagogical principles for formative assessment in programming education.

## Research Questions and Reasoning

### What makes a model suitable for high-level competence analysis?

A model suitable for competence analysis must possess several critical capabilities: **semantic code understanding** beyond syntax checking, **pedagogical awareness** to distinguish between different types of errors and misconceptions, and **prompt generation skills** that encourage student reflection rather than providing direct solutions. The model should understand the hierarchical nature of programming concepts (from basic syntax to algorithmic thinking) and be able to map student errors to underlying conceptual gaps. Additionally, it must demonstrate **contextual sensitivity**, recognizing that the same error might indicate different competency issues depending on the student's level and the specific learning objective.

### How would you test whether a model generates meaningful prompts?

To validate prompt quality, I will employ a multi-faceted evaluation approach. **Relevance testing** will measure how well generated prompts target the specific misconceptions present in student code, using expert-annotated code samples as ground truth. **Pedagogical effectiveness** will be assessed through alignment with Bloom's taxonomy levels, ensuring prompts encourage analysis and synthesis rather than mere recall. **Student engagement metrics** will be simulated through prompt complexity analysis and question clarity scoring. Finally, **iterative refinement testing** will examine whether follow-up prompts adapt appropriately based on simulated student responses, demonstrating the model's ability to scaffold learning progressively.

### What trade-offs might exist between accuracy, interpretability, and cost?

The primary trade-off exists between model sophistication and practical deployment constraints. Large language models like CodeLlama-34B offer superior contextual understanding and nuanced prompt generation but require significant computational resources and may lack interpretability in their decision-making process. Conversely, rule-based systems combined with smaller specialized models (like CodeBERT) provide greater interpretability and lower operational costs but may miss subtle conceptual errors that require deeper semantic understanding. A hybrid approach balances these trade-offs by using interpretable static analysis for common misconceptions while leveraging LLMs for complex reasoning assessment, though this introduces system complexity and integration challenges.

### Why did you choose CodeT5+ and what are its strengths/limitations?

I selected **CodeT5+** as the primary evaluation model due to its demonstrated performance in code-to-text and text-to-code tasks, making it well-suited for generating explanatory prompts from code analysis. Its open-source availability, reasonable computational requirements (compared to larger models), and strong performance on code understanding benchmarks make it a practical choice for educational deployment. The model's encoder-decoder architecture is particularly advantageous for our use case, as it can process student code and generate contextually appropriate pedagogical prompts.

**Strengths**: Strong multilingual code support, proven performance on code summarization and generation tasks, manageable size for institutional deployment, and active community support with available fine-tuning resources.

**Limitations**: May require domain-specific fine-tuning for optimal pedagogical prompt generation, limited built-in understanding of educational frameworks, and potential challenges in detecting subtle logical errors that don't manifest as syntax issues. Additionally, like most transformer-based models, it may struggle with very long code sequences and could generate plausible but pedagogically inappropriate prompts without proper training data.

## Implementation Strategy

### Phase 1: Baseline Analysis (Weeks 1-2)
- Set up CodeT5+ model environment
- Create dataset of common Python student errors
- Implement basic static analysis tools for comparison

### Phase 2: Model Evaluation (Weeks 3-4)  
- Test CodeT5+ on curated code samples
- Compare against rule-based baseline systems
- Measure prompt quality using defined metrics

### Phase 3: Validation and Refinement (Weeks 5-6)
- Expert review of generated prompts
- Fine-tune model parameters based on results
- Document best practices and limitations

## Success Metrics

### Technical Performance
- **Misconception Detection**: 85%+ accuracy in identifying common Python errors
- **Prompt Relevance**: 90%+ of generated prompts address detected issues appropriately
- **Response Time**: Sub-second analysis for typical student code samples

### Educational Quality
- **Bloom's Taxonomy Alignment**: Prompts classified by cognitive complexity
- **Scaffolding Quality**: Evidence of progressive difficulty in prompt sequences
- **Pedagogical Appropriateness**: Expert rating of educational value

## Expected Deliverables

1. Functional evaluation framework with CodeT5+ integration
2. Comparative analysis report of model performance
3. Recommendations for educational implementation
4. Open-source tools for continued research and development

## References

- Wang, Y., et al. (2023). "CodeT5+: Open Code Large Language Models for Code Understanding and Generation"
- Ihantola, P., et al. (2010). "Review of recent systems for automatic assessment of programming assignments"  
- Brown, N. C., et al. (2014). "Blackbox dataset of novice programmers' programming behaviours"
- Bloom, B. S. (1956). "Taxonomy of educational objectives"
