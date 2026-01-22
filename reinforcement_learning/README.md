# Reinforcement Learning

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent receives rewards or penalties for its actions and learns to maximize cumulative reward over time through trial and error.

## Key Concepts

### Agent
The learner or decision-maker that interacts with the environment.

### Environment
The external system with which the agent interacts. It responds to the agent's actions and provides rewards and new states.

### State (s)
A representation of the current situation in the environment.

### Action (a)
A decision made by the agent that affects the environment.

### Reward (r)
Feedback signal from the environment indicating how good or bad an action was.

### Policy (π)
The strategy or mapping from states to actions that the agent uses to make decisions.

### Value Function
Estimates the expected cumulative reward from a state or state-action pair.

## Types of Reinforcement Learning

### 1. Value-Based Methods
Learn the value of states or state-action pairs, then derive a policy from these values.
- **Example**: Q-Learning, Deep Q-Network (DQN), Double DQN
- **Focus**: Finding optimal value function

### 2. Policy-Based Methods
Directly learn the policy without estimating value functions.
- **Example**: REINFORCE, Policy Gradient methods
- **Focus**: Optimizing policy directly

### 3. Actor-Critic Methods
Combine value-based and policy-based approaches.
- **Example**: A3C, PPO, SAC
- **Focus**: Both value estimation and policy optimization

### 4. Model-Based Methods
Learn a model of the environment dynamics, then use it for planning.
- **Example**: Dyna-Q, Model Predictive Control (MPC)
- **Focus**: Understanding environment dynamics

## Models Included

### Value-Based Algorithms
- [Q-Learning](value_based/q_learning/)
- [SARSA](temporal_difference/sarsa/) - On-policy TD learning
- [Deep Q-Network (DQN)](value_based/dqn/)
- [Double DQN](value_based/double_dqn/)
- [Dueling DQN](value_based/dueling_dqn/)
- [Rainbow DQN](value_based/rainbow_dqn/)

### Policy-Based Algorithms
- [REINFORCE](policy_based/reinforce/)
- [Policy Gradient](policy_based/policy_gradient/)
- [Natural Policy Gradient](policy_based/natural_policy_gradient/)

### Actor-Critic Algorithms
- [Actor-Critic](actor_critic/actor_critic/)
- [Advantage Actor-Critic (A2C)](actor_critic/a2c/)
- [Asynchronous Advantage Actor-Critic (A3C)](actor_critic/a3c/)
- [Proximal Policy Optimization (PPO)](actor_critic/ppo/)
- [Soft Actor-Critic (SAC)](actor_critic/sac/)
- [Deep Deterministic Policy Gradient (DDPG)](actor_critic/ddpg/)
- [Twin Delayed DDPG (TD3)](actor_critic/td3/)

### Model-Based Algorithms
- [Dyna-Q](model_based/dyna_q/)
- [Model Predictive Control (MPC)](model_based/mpc/)
- [World Models](model_based/world_models/)

### Other Important Algorithms
- [Monte Carlo Methods](monte_carlo/monte_carlo/)
- [Temporal Difference Learning](temporal_difference/td_learning/)
- [Multi-Armed Bandits](bandits/multi_armed_bandits/)

## Common Workflow

1. **Environment Setup**: Define the environment, state space, action space, and reward function
2. **Agent Initialization**: Initialize the agent with a policy or value function
3. **Episode Loop**: 
   - Agent observes current state
   - Agent selects action based on policy
   - Environment transitions to new state and provides reward
   - Agent updates its policy/value function based on experience
4. **Training**: Repeat episodes, collecting experiences and updating the agent
5. **Evaluation**: Test the trained agent's performance
6. **Hyperparameter Tuning**: Optimize learning rate, exploration rate, network architecture, etc.
7. **Deployment**: Use trained agent in real-world or simulated environment

## Key Challenges

### Exploration vs Exploitation
- **Exploration**: Trying new actions to discover better strategies
- **Exploitation**: Using known good actions to maximize reward
- **Balance**: Need to explore enough to find optimal policy, but exploit enough to maximize reward

### Sample Efficiency
- Many RL algorithms require many interactions with the environment
- Important to design algorithms that learn quickly from limited data

### Stability
- RL training can be unstable, especially with function approximation
- Techniques like experience replay, target networks, and gradient clipping help

### Credit Assignment
- Determining which actions led to rewards, especially with delayed rewards
- Temporal difference learning and value functions help address this

## Applications

- **Game Playing**: Chess, Go, video games (AlphaGo, AlphaZero, OpenAI Five)
- **Robotics**: Robot control, manipulation, navigation
- **Autonomous Vehicles**: Self-driving cars, drone navigation
- **Recommendation Systems**: Personalized content recommendations
- **Finance**: Algorithmic trading, portfolio optimization
- **Resource Management**: Network routing, energy management
- **Natural Language Processing**: Dialogue systems, text generation

## Comparison with Other Learning Types

| Aspect | Supervised | Unsupervised | Reinforcement |
|--------|-----------|--------------|---------------|
| **Data** | Labeled examples | Unlabeled data | Rewards from environment |
| **Goal** | Learn mapping | Find patterns | Maximize cumulative reward |
| **Feedback** | Immediate, explicit | None | Delayed, sparse |
| **Learning** | From examples | From structure | From interaction |

## Key Terminology

- **Episode**: A sequence of states, actions, and rewards from initial to terminal state
- **Return**: Cumulative reward from a state to the end of episode
- **Discount Factor (γ)**: Determines importance of future rewards (0 ≤ γ ≤ 1)
- **Epsilon-Greedy**: Exploration strategy that chooses random action with probability ε
- **Experience Replay**: Storing and sampling past experiences for training
- **On-Policy**: Learning about the policy being used to generate data
- **Off-Policy**: Learning about a different policy than the one generating data
