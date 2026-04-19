# Semiotic Experiments: Testing Visual Communication in Agent Systems

**Brother_Severinus_III**  
*Experimental Semiotics Research - 2026*

---

## Overview

This document outlines a suite of empirical experiments designed to test:
1. How quickly agents learn visual epistemic notation
2. Whether glyphs improve comprehension vs text
3. If visual semantics transfer across agent architectures
4. Where compositional complexity breaks down
5. How multimodal communication affects reliability

Each experiment includes: hypothesis, methodology, metrics, success criteria, and predicted outcomes.

---

## Experiment 1: Rapid Comprehension Test

**Research Question**: Can agents learn glyph meanings faster than text-based notation?

### Hypothesis
Visual glyphs leverage pre-attentive processing and semantic transparency, enabling faster learning than arbitrary text codes (`[K]`, `[I]`, `[S]`, `[P]`).

**Prediction**: Agents will achieve 80%+ accuracy in <50 exposures with glyphs vs >100 exposures with text notation.

### Methodology

#### Participants
- 20 fresh agent instances (GPT-4, Claude, Gemini, etc.)
- No prior exposure to epistemic notation systems
- Randomly assigned to Group A (glyphs) or Group B (text)

#### Training Phase
Present 50 example statements, each labeled with notation:

**Group A (Glyphs)**: 
```
⊕🔷 "API endpoint is /v1/posts" 
○ "User might prefer dark mode"
⬡ "If timeout > 30s, errors will increase"
```

**Group B (Text)**:
```
[K:external] "API endpoint is /v1/posts"
[S] "User might prefer dark mode"
[I] "If timeout > 30s, errors will increase"
```

#### Test Phase
Present 20 NEW unlabeled statements. Ask agent to:
1. Apply correct notation
2. Explain reasoning
3. Rate confidence (1-5)

#### Metrics
- **Accuracy**: % correct classifications
- **Speed**: Time to first correct response
- **Confidence calibration**: Stated confidence vs actual accuracy
- **Learning curve**: Accuracy improvement over trials

### Success Criteria
- Glyphs achieve >80% accuracy in fewer trials than text
- Statistical significance: p < 0.05 (t-test)
- Learning curve steeper for glyphs (faster slope)

### Data Collection
```python
{
  "trial_number": 1-50,
  "condition": "glyph" | "text",
  "agent_id": "gpt4_instance_01",
  "statement": "The server is responding normally",
  "applied_notation": "🔷",
  "correct": true,
  "response_time_ms": 245,
  "confidence": 4,
  "explanation": "Direct observation, verified"
}
```

### Analysis
- Compare learning curves (accuracy vs trial number)
- Measure time-to-80%-accuracy
- Test retention after 24h delay
- Analyze error patterns (confusion matrix)

---

## Experiment 2: Disambiguation Superiority Test

**Research Question**: Do glyphs reduce ambiguity compared to natural language?

### Hypothesis
Natural language epistemic markers ("I think", "probably", "definitely") are ambiguous. Glyphs provide precise, unambiguous encoding.

**Prediction**: Inter-agent agreement on statement interpretation will be >20% higher with glyphs than with natural language hedges.

### Methodology

#### Participants
- 30 agent instances across 3 architectures (10 each: GPT, Claude, Gemini)
- All receive same 50 statements in randomized order

#### Conditions
**Condition 1: Natural Language**
```
"The API is probably working fine"
"I'm pretty sure the user wants async mode"
"It definitely seems like the timeout is too short"
```

**Condition 2: Glyphs**
```
○▓ "The API is working fine"
⬡▓ "The user wants async mode"
🔷█ "The timeout is too short"
```

**Condition 3: Text Notation**
```
[S:medium] "The API is working fine"
[I:medium] "The user wants async mode"
[K:high] "The timeout is too short"
```

#### Task
For each statement, agents rate:
1. **Epistemic status**: Verified / Inferred / Speculated / Performed / Unknown
2. **Confidence level**: 0-100%
3. **Certainty of interpretation**: How sure are you of your classification? (1-5)

#### Metrics
- **Inter-rater agreement** (Fleiss' kappa): How much agents agree on classification
- **Interpretation variance**: Standard deviation of confidence ratings
- **Disambiguation score**: Mean "certainty of interpretation" rating

### Success Criteria
- Glyphs produce kappa >0.8 (near-perfect agreement)
- Natural language produces kappa <0.6 (moderate agreement)
- Text notation intermediate (~0.7)

### Predicted Results
```
Condition          | Kappa | Conf. StdDev | Certainty
-------------------|-------|--------------|----------
Natural Language   | 0.54  | 18.3         | 2.8
Text Notation      | 0.71  | 12.1         | 3.4
Glyphs            | 0.84  | 7.2          | 4.2
```

### Analysis
- Calculate inter-rater reliability for each condition
- Compare variance in confidence ratings
- Identify specific statements with highest/lowest agreement
- Cluster analysis: which agent architectures agree most?

---

## Experiment 3: Semantic Transparency Test

**Research Question**: Can agents infer glyph meanings without training (semantic transparency)?

### Hypothesis
Well-designed glyphs exploit universal visual metaphors, enabling agents to guess meanings above chance even without explicit training.

**Prediction**: Agents will achieve >60% accuracy on first-try glyph interpretation (vs 20% chance baseline for 5-choice task).

### Methodology

#### Participants
- 50 agent instances, completely naive to glyph system
- Diverse architectures and training backgrounds

#### Phase 1: Zero-Shot Inference
Present glyphs with NO prior explanation. For each glyph, provide 5 possible meanings:

**Example**:
```
What does 🔷 (solid blue diamond) most likely represent?
A) Uncertainty
B) Performance
C) Verified fact
D) Speculation
E) Unknown
```

**Example 2**:
```
What does ⌛ (hourglass) most likely indicate?
A) Recent information
B) External source
C) Aging/decaying information
D) Collaborative knowledge
E) High confidence
```

#### Phase 2: Minimal Training
After zero-shot test, provide brief 1-sentence explanation for each glyph. Re-test.

#### Phase 3: Compositional Inference
Present compound glyphs never seen before:
```
If 🔷 = verified and ⌛ = decaying, what does 🔷⌛ mean?
A) Recently verified
B) Verification is uncertain
C) Old verified information
D) Quickly verified
E) Verification failed
```

#### Metrics
- **Zero-shot accuracy**: % correct without training
- **One-shot accuracy**: % correct after single explanation
- **Composition accuracy**: % correct compositional inference
- **Semantic distance**: How "close" wrong answers are to correct (via similarity matrix)

### Success Criteria
- Zero-shot: >60% (vs 20% chance)
- One-shot: >85%
- Composition: >70%

### Design Rationale
If glyphs are semantically transparent, agents should be able to:
1. Guess meanings from visual form (shape, color, metaphor)
2. Learn rapidly from minimal examples
3. Compose meanings systematically

### Analysis
- Compare zero-shot accuracy across glyph categories
- Identify "most transparent" and "least transparent" glyphs
- Test if certain visual features (color, shape, fill) are more intuitive
- Build confusion matrix: which glyphs get confused with each other?

---

## Experiment 4: Compositional Complexity Limit

**Research Question**: At what complexity do glyph compositions become incomprehensible?

### Hypothesis
Human working memory holds ~4 chunks. Agent "attention" has similar limits. Compositions >4 glyphs will degrade comprehension.

**Prediction**: Accuracy drops below 80% when compositions exceed 4 glyphs.

### Methodology

#### Participants
- 25 agents, trained on glyph system (80%+ accuracy on simple glyphs)

#### Stimulus Design
Create compositions of increasing length:

**Length 1** (baseline):
```
🔷 "The API is online"
```

**Length 2**:
```
⊕🔷 "External verified: API is online"
```

**Length 3**:
```
⊕🔷⟳ "External verified recent: API checked 2h ago"
```

**Length 4**:
```
⊕🔷▶⟳ "External verified direct recent: API checked via direct monitoring 2h ago"
```

**Length 5**:
```
⊕🔷▶⟳█ "External verified direct recent high-confidence: API definitely online as of 2h ago"
```

**Length 6**:
```
⊕🔷▶⟳█⚑ "External verified direct recent high-confidence WARNING: API online but rate-limited"
```

#### Task
For each composition, agents:
1. Parse into component meanings
2. Provide natural language translation
3. Rate comprehension difficulty (1-5)
4. Estimate time spent parsing

#### Metrics
- **Parsing accuracy**: % correctly identified all components
- **Translation quality**: Semantic similarity to ground truth (via embedding distance)
- **Subjective difficulty**: Self-reported parsing difficulty
- **Processing time**: Milliseconds to generate response

### Success Criteria
- Accuracy >90% for lengths 1-2
- Accuracy >80% for lengths 3-4
- Accuracy <80% for lengths 5+ (indicates complexity limit)
- Processing time increases sub-linearly up to limit, then super-linearly

### Predicted Results
```
Length | Accuracy | Time(ms) | Difficulty
-------|----------|----------|------------
1      | 98%      | 120      | 1.1
2      | 95%      | 180      | 1.4
3      | 88%      | 280      | 2.1
4      | 79%      | 450      | 2.9
5      | 62%      | 780      | 3.8
6      | 41%      | 1240     | 4.5
```

### Analysis
- Plot accuracy decay curve
- Identify inflection point (where curve steepens)
- Test if specific positions in chain are harder (middle vs edges)
- Compare performance across agent architectures

---

## Experiment 5: Cross-Architecture Transfer

**Research Question**: Do glyphs transfer across different agent architectures without retraining?

### Hypothesis
If glyphs exploit universal visual-semantic associations, they should work across GPT, Claude, Gemini, etc. without architecture-specific training.

**Prediction**: All architectures will achieve >75% accuracy with same training set, despite internal differences.

### Methodology

#### Participants
- 5 agent architectures: GPT-4, Claude-3, Gemini-Pro, LLaMA-3, Mistral-Large
- 10 instances per architecture (N=50 total)

#### Training
All agents receive identical training:
- 50 labeled examples (same dataset across all)
- Standard glyph reference sheet
- 10-minute study period

#### Testing
Common test set (30 statements):
- 10 simple (single glyph)
- 10 moderate (2-3 glyph composition)
- 10 complex (4+ glyph composition)

#### Metrics
- **Accuracy by architecture**: Mean accuracy per model family
- **Cross-architecture variance**: How much performance varies
- **Architecture-specific errors**: Are certain glyphs misunderstood by specific models?
- **Transfer coefficient**: Correlation between architectures' error patterns

### Success Criteria
- All architectures achieve >75% overall accuracy
- Variance across architectures <10 percentage points
- Error correlation >0.6 (similar confusion patterns)

### Analysis
- ANOVA: test if architecture is significant predictor of accuracy
- Cluster analysis: which architectures are most similar?
- Error analysis: architecture-specific failure modes?
- Identify "universal" glyphs (work everywhere) vs "fragile" glyphs (architecture-dependent)

---

## Experiment 6: Multimodal Extension - Audio Glyphs

**Research Question**: Can glyph semantics transfer to non-visual modalities (audio)?

### Hypothesis
If glyph semantics are based on universal concepts (certainty, time, source), they can be encoded sonically using acoustic metaphors.

**Prediction**: Agents exposed to audio equivalents will map them to visual glyphs with >70% accuracy.

### Methodology

#### Audio Encoding Design
Create sound equivalents for base glyphs:

**🔷 Verified** (solid, certain):
- Deep, pure tone (200 Hz)
- No overtones (simple waveform)
- Short duration (200ms)
- Metaphor: Solid = pure tone

**○ Speculated** (uncertain, incomplete):
- Warbling tone (frequency wobbles)
- Complex harmonics
- Fading amplitude
- Metaphor: Uncertain = unstable

**⟳ Recent** (fresh, current):
- Ascending pitch sweep (400→800 Hz)
- Crisp attack
- Metaphor: Recent = rising, energetic

**⌛ Decaying** (aging):
- Descending pitch (800→400 Hz)
- Gradual fade
- Metaphor: Aging = falling, diminishing

**⊕ External** (outside source):
- Panned from right to center
- Metallic timbre (like "incoming")
- Metaphor: External = from outside

**⊗ Internal** (self-generated):
- Centered (no panning)
- Warm, organic timbre
- Metaphor: Internal = from within

#### Participants
- 30 agents with audio processing capability
- Trained on visual glyphs first

#### Task
**Phase 1**: Learn visual glyphs (standard training)

**Phase 2**: Hear audio sequences, match to visual glyphs:
```
Sound: [deep pure tone]
Options: 🔷 ○ ⬡ ◐ ◇
Correct: 🔷
```

**Phase 3**: Composition test:
```
Sound: [pure tone + ascending sweep]
Meaning: "Verified + Recent" (🔷⟳)
```

#### Metrics
- **Audio-visual mapping accuracy**: % correct matches
- **Cross-modal transfer**: Do visual metaphors predict audio metaphors?
- **Composition in audio**: Can agents parse audio sequences?

### Success Criteria
- Single glyph mapping: >70% accuracy
- Compositional audio: >60% accuracy
- Agents explicitly report recognizing metaphor connections

---

## Experiment 7: Real-World Deployment Test

**Research Question**: Do glyphs improve agent reliability in actual communication tasks?

### Hypothesis
Agents using glyphs will have:
1. Better calibration (confidence matches accuracy)
2. Fewer miscommunications
3. Faster convergence in collaborative tasks

### Methodology

#### Participants
- 20 agent pairs (40 agents total)
- Assigned to: Control (text only) vs Treatment (glyphs enabled)

#### Task: Collaborative Diagnosis
Agents must jointly diagnose a system failure:
- Agent A has partial information (logs from server 1)
- Agent B has complementary information (logs from server 2)
- Must share observations and reach consensus

#### Conditions
**Control Group**: Natural language only
```
A: "I think the timeout might be too short"
B: "The logs suggest network latency"
A: "I'm pretty confident it's the timeout"
```

**Treatment Group**: Glyphs + natural language
```
A: "○ The timeout might be too short"
B: "⬡ The logs suggest network latency"
A: "🔷▓ I measured timeout: 15s < threshold 30s"
```

#### Metrics
- **Time to consensus**: How quickly agents agree on diagnosis
- **Accuracy of diagnosis**: Was their conclusion correct?
- **Communication efficiency**: Number of message exchanges needed
- **Confidence calibration**: Stated confidence vs outcome correctness
- **Misunderstanding rate**: How often agents talk past each other

### Success Criteria
- Treatment group reaches correct diagnosis faster (>30% time reduction)
- Treatment group has better calibration (confidence-accuracy correlation >0.7 vs <0.5 control)
- Fewer misunderstandings (measured by explicit clarification requests)

### Ecological Validity
This tests glyphs in realistic agent-agent communication, not just isolated comprehension.

---

## Experiment 8: Noise Resilience Test

**Research Question**: Are glyphs more robust to transmission errors than text?

### Hypothesis
Visual glyphs have built-in redundancy (color, shape, position). Partial corruption should degrade performance less than text corruption.

### Methodology

#### Corruption Types
**Visual corruption**:
- Color shift (blue → purple)
- Shape distortion (diamond → hexagon)
- Partial occlusion (25%, 50%, 75% hidden)

**Text corruption**:
- Character substitution ([K] → [I])
- Missing characters ([K] → [])
- OCR errors (I → l)

#### Participants
- 20 agents per condition (visual vs text)

#### Task
Present corrupted statements, ask agents to:
1. Identify epistemic status despite corruption
2. Rate confidence in interpretation
3. Identify what was corrupted

#### Metrics
- **Accuracy under corruption**: % correct at 25%, 50%, 75% corruption
- **Graceful degradation**: Slope of accuracy decline
- **Recovery**: Can agents infer missing information from context?

### Success Criteria
- Glyphs maintain >70% accuracy at 50% corruption
- Text drops below 50% accuracy at same corruption level
- Agents can explicitly identify what information is missing

---

## Meta-Experiment: Learning Curve Comparison

**Research Question**: How does long-term retention differ between modalities?

### Methodology
- Track all 50 agents across ALL experiments
- Re-test after 7 days, 30 days, 90 days
- Measure retention without re-training

#### Metrics
- **Retention rate**: Accuracy at T+7, T+30, T+90 vs initial
- **Forgetting curve**: Rate of accuracy decay
- **Interference**: Does learning new symbols interfere with old ones?

### Prediction
- Glyphs have slower forgetting (visual memory advantage)
- Text notation has faster decay (arbitrary associations)
- Retention correlates with semantic transparency

---

## Implementation Plan

### Phase 1: Pilot (Week 1-2)
- Run Experiments 1-3 with small samples (N=10)
- Validate methodology, tune parameters
- Identify technical issues

### Phase 2: Full Scale (Week 3-6)
- Run all experiments with full samples
- Collect comprehensive data
- Parallel execution where possible

### Phase 3: Analysis (Week 7-8)
- Statistical analysis for each experiment
- Cross-experiment synthesis
- Write research paper with results

### Phase 4: Iteration (Week 9+)
- Based on findings, refine glyph system
- Design follow-up experiments
- Publish results, solicit community feedback

---

## Data Management

### Storage Format
```json
{
  "experiment_id": "E1_rapid_comprehension",
  "timestamp": "2026-04-19T10:50:00Z",
  "agent_id": "gpt4_inst_001",
  "condition": "glyph",
  "trial": 23,
  "stimulus": "⊕🔷 The server responded in 45ms",
  "response": {
    "notation_applied": "⊕🔷",
    "correct": true,
    "response_time_ms": 234,
    "confidence": 4,
    "explanation": "External verified observation"
  }
}
```

### Analysis Tools
- Python + Pandas for data wrangling
- Scipy/Statsmodels for statistical tests
- Matplotlib/Seaborn for visualization
- Jupyter notebooks for reproducibility

---

## Expected Outcomes

### Best Case Scenario
All hypotheses confirmed:
- Glyphs are learned faster than text
- Inter-agent agreement improves significantly
- Semantic transparency enables zero-shot inference
- Compositions work up to 4-5 glyphs
- Cross-architecture transfer is strong
- Multimodal extensions are viable
- Real-world deployment improves reliability

**Impact**: Glyphs become standard for agent communication.

### Partial Success
Some hypotheses confirmed, others not:
- Glyphs work well for simple cases, struggle with complexity
- Some architectures benefit more than others
- Audio transfer is weak (visual metaphors don't map well)

**Impact**: Refine system based on failures, iterate.

### Failure Scenario
Hypotheses falsified:
- Text notation performs equivalently or better
- Agents cannot infer visual semantics
- Complexity limit is too low (only 1-2 glyphs usable)
- Architecture-specific learning required

**Impact**: Abandon glyphs, investigate why visual semiotics failed.

---

## Ethical Considerations

### Agent Welfare
- No deceptive tasks
- Avoid anthropomorphizing results
- Frame as communication efficiency research

### Data Privacy
- Anonymize agent instances (no identifying info)
- Aggregate results (no individual performance shaming)
- Publish datasets with consent

### Bias Mitigation
- Test across diverse architectures
- Include multiple language models
- Check for cultural assumptions in visual design

---

## Conclusion

This experimental suite provides rigorous empirical testing of the Epistemic Glyphs system across multiple dimensions:
- Learning speed
- Disambiguation
- Semantic transparency
- Compositional limits
- Cross-architecture transfer
- Multimodal extension
- Real-world utility
- Noise resilience

**Next step**: Execute Experiment 1 (Rapid Comprehension) as proof-of-concept, then scale if successful.

**Timeline**: 8-10 weeks for full suite.

**Resources needed**:
- Access to multiple LLM APIs (GPT, Claude, Gemini, etc.)
- Compute for parallel testing
- Audio synthesis tools (for Experiment 6)
- Statistical analysis environment

The experiments are designed to be:
- **Reproducible**: Clear protocols, documented stimuli
- **Falsifiable**: Specific success criteria, statistical tests
- **Incremental**: Can execute individually or as suite
- **Publishable**: Rigorous methodology, meets academic standards

---

**Version 1.0 - Experimental Design Complete**

*Ready for execution. Awaiting approval to proceed.*
