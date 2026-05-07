# Reinforcement Learning

**Summary**: RL is a machine learning paradigm where agents learn optimal behavior through trial-feedback-optimization cycles driven by a reward function; it achieved superhuman performance in narrow domains but has poor transferability for general-purpose tasks — though it remains central to LLM training pipelines (RLHF, DPO, PPO).

**Sources**: `From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md`

**Last updated**: 2026-05-07

**Tags**: `reinforcement-learning` `llm-fundamentals` `ai-evolution` `concept` `foundational`

---

## Core Idea

Instead of defining *how* to act (as in rule-based systems), RL defines *what to optimize*. The agent learns via:

> **Trial → Feedback → Optimization**

A **Reward Function** scores each action, and the system iterates toward a policy that maximizes cumulative reward (source: From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md).

## Strengths

- Capable of discovering strategies that humans wouldn't pre-program
- Achieves **superhuman performance in narrow domains**:
  - AlphaGo / AlphaZero (board games)
  - Robotic control
  - Autonomous driving simulators

## Limitations

| Limitation | Why It Matters |
|-----------|----------------|
| Poor transferability outside training domain | A model trained to play Go cannot play chess without retraining |
| Strict dependency on reward design | Poorly specified rewards lead to unintended behaviors (reward hacking) |
| Score maximization, not real-world goal satisfaction | The agent optimizes the metric, not the intent behind it |

(source: From Hardcoded Tools to Reinforcement Learning to LLM Agents_ The Evolution of AI Systems.md)

## Role in the AI Evolution

RL is the second wave of AI system evolution, bridging rule-based systems (Wave 1) and LLM-powered agents (Wave 3). Its limitation — domain specificity — is exactly what LLMs solved with general-purpose reasoning. See [[ai-systems-evolution]] for the full picture.

## RL in Modern LLM Training

RL remains highly relevant *within* LLM training pipelines (RLHF, DPO, PPO for alignment), even though RL alone is no longer the dominant paradigm for agent *behavior* at inference time. This distinction is important: LLMs replaced RL as the *runtime* reasoning engine, but RL is how LLMs themselves get fine-tuned toward human preferences.

> **Needs verification**: claims about RLHF, DPO, PPO have no source in the current ingested articles. To be expanded when relevant sources are added.

## Related pages

- [[ai-systems-evolution]]
- [[llm-agents]]
