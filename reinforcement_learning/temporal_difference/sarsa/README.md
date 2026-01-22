# SARSA (State-Action-Reward-State-Action)

## Overview

SARSA is an on-policy temporal difference (TD) learning algorithm for learning the optimal action-value function Q(s,a). The name comes from the sequence of elements it uses: (State, Action, Reward, State, Action). SARSA is one of the fundamental algorithms in reinforcement learning and is often taught alongside Q-Learning as a core TD method.

## How It Works

SARSA is an **on-policy** algorithm, meaning it learns the value of the policy it is currently following, rather than learning the optimal policy directly (like Q-Learning does).

### Update Rule

```
Q(sₜ, aₜ) ← Q(sₜ, aₜ) + α[rₜ₊₁ + γQ(sₜ₊₁, aₜ₊₁) - Q(sₜ, aₜ)]
```

Where:
- `Q(s, a)` is the action-value function (Q-function)
- `sₜ` is the current state
- `aₜ` is the current action
- `rₜ₊₁` is the reward received after taking action aₜ
- `sₜ₊₁` is the next state
- `aₜ₊₁` is the next action (selected using the current policy)
- `α` (alpha) is the learning rate
- `γ` (gamma) is the discount factor

### Key Difference from Q-Learning

**SARSA (On-Policy)**:
- Uses the action actually taken in the next state: `Q(sₜ₊₁, aₜ₊₁)`
- Learns the value of the policy being followed
- More conservative, safer exploration

**Q-Learning (Off-Policy)**:
- Uses the maximum Q-value in the next state: `max Q(sₜ₊₁, a')`
- Learns the optimal policy directly
- More aggressive, can learn optimal policy while exploring

### Algorithm Steps

1. Initialize Q(s,a) arbitrarily for all state-action pairs
2. For each episode:
   - Initialize state s
   - Choose action a from s using policy derived from Q (e.g., ε-greedy)
   - For each step of episode:
     - Take action a, observe reward r and next state s'
     - Choose action a' from s' using policy derived from Q (e.g., ε-greedy)
     - Update: `Q(s,a) ← Q(s,a) + α[r + γQ(s',a') - Q(s,a)]`
     - Set s ← s' and a ← a'
   - Until s is terminal

## Parameters

### Learning Rate (α)

- **Range**: 0 < α ≤ 1
- **Typical values**: 0.1 to 0.5
- **Small α**: Slow learning, more stable
- **Large α**: Fast learning, may be unstable
- **Decay**: Often decreased over time for convergence

### Discount Factor (γ)

- **Range**: 0 ≤ γ ≤ 1
- **Typical values**: 0.9 to 0.99
- **γ = 0**: Only considers immediate reward
- **γ = 1**: Considers all future rewards equally
- **Higher γ**: More emphasis on long-term rewards

### Exploration Rate (ε for ε-greedy)

- **Range**: 0 ≤ ε ≤ 1
- **Typical values**: Start with 0.1-0.3, decay over time
- **ε = 0**: Pure exploitation (greedy)
- **ε = 1**: Pure exploration (random)
- **Common strategy**: Start high, decay to 0.01-0.05

### Convergence

- **Convergence**: Q-values converge to Q^π (value of policy π)
- **Convergence rate**: Depends on learning rate and exploration
- **Guarantees**: Converges to optimal Q* if all state-action pairs visited infinitely often and learning rate satisfies certain conditions

## Use Cases

**Good for:**
- Environments where safety is important (learns conservative policy)
- Online learning scenarios (learns while acting)
- When you want to learn the value of a specific policy
- Environments with negative rewards (avoids dangerous states)
- Cliff-walking type problems (prefers safer paths)

**Not ideal for:**
- When you need optimal policy quickly
- Offline learning scenarios
- When exploration is very expensive
- Large state spaces without function approximation

## Example Use Cases

1. **Robot Navigation**: Learning safe paths while avoiding obstacles
2. **Trading Algorithms**: Conservative trading strategies
3. **Game Playing**: Learning safe, consistent strategies
4. **Autonomous Vehicles**: Learning defensive driving policies
5. **Resource Management**: Learning policies that avoid risky states

## Pros and Cons

### Pros
- **Safe exploration**: Learns conservative policies, avoids dangerous states
- **On-policy**: Learns the policy it's actually using
- **Simple**: Easy to understand and implement
- **Convergent**: Guaranteed to converge under certain conditions
- **Online learning**: Can learn while interacting with environment

### Cons
- **Slower convergence**: May converge slower than Q-Learning
- **Suboptimal**: Learns value of current policy, not necessarily optimal
- **Exploration dependent**: Performance depends heavily on exploration strategy
- **Tabular**: Typically used with tabular Q-functions (can be extended with function approximation)

## Comparison with Q-Learning

| Aspect | SARSA | Q-Learning |
|--------|-------|------------|
| **Type** | On-policy | Off-policy |
| **Update** | Uses actual next action | Uses max Q-value |
| **Policy** | Learns current policy | Learns optimal policy |
| **Safety** | More conservative | More aggressive |
| **Convergence** | To Q^π | To Q* |
| **Use case** | Safe exploration | Optimal performance |

## SARSA(λ) - Eligibility Traces

SARSA can be extended with eligibility traces for faster learning:

**SARSA(λ)**:
- Uses eligibility traces to update multiple state-action pairs
- λ (lambda) controls trace decay
- Faster learning, especially in sparse reward environments
- More complex but more efficient

## Function Approximation

SARSA can be combined with function approximation:
- **Linear function approximation**: Q(s,a) ≈ θᵀφ(s,a)
- **Neural networks**: Deep SARSA
- **Tile coding**: For continuous state spaces
- Allows scaling to large/continuous state spaces

## Mathematical Foundation

### Bellman Equation for SARSA

SARSA updates towards:
```
Q^π(s,a) = E[r + γQ^π(s',a') | s,a]
```

Where the expectation is over:
- Next state s' (from environment dynamics)
- Next action a' (from policy π)

### Convergence

Under conditions:
- All state-action pairs visited infinitely often
- Learning rate: Σαₜ = ∞ and Σαₜ² < ∞
- Policy becomes greedy in the limit

SARSA converges to Q^π, the action-value function for policy π.

## Key Takeaways

1. **SARSA is on-policy**: Learns the value of the policy being followed
2. **More conservative than Q-Learning**: Prefers safer actions
3. **Uses actual next action**: Updates based on action actually taken
4. **Good for safety-critical applications**: Learns to avoid dangerous states
5. **Foundation for many algorithms**: Basis for many on-policy methods

## Extensions

- **Expected SARSA**: Uses expected value of next action instead of actual action
- **SARSA(λ)**: With eligibility traces for faster learning
- **Deep SARSA**: With neural network function approximation
- **Multi-step SARSA**: Uses n-step returns instead of 1-step

## References

- Sutton & Barto (2018). "Reinforcement Learning: An Introduction" - Chapter 6
- Temporal difference learning foundations
- On-policy vs off-policy learning
