from rl.agents.tabular import ActionValuesTable

# This is every-visit on policy Monte Carlo control.
class OnPolicyMonteCarloAgent:
    def __init__(self, environment, exploration_strategy, discount):
        self.environment = environment
        # TODO: make sure environment has a discrete action and observation space

        self.exploration_strategy = exploration_strategy
        self.discount = discount

        self.action_values = ActionValuesTable(self.environment.action_space)

    def train(self, episodes):
        for episode in range(episodes):
            print(f'Training: episode {episode}')
            states, actions, rewards = [], [], []
            observation = self.environment.reset()
            done = False
            while not done:
                states.append(observation)
                action = self.act(observation)
                actions.append(action)
                observation, reward, done, _ = self.environment.step(action)
                rewards.append(reward)

            episode_return = 0
            for state, action, reward in zip(reversed(states), reversed(actions), reversed(rewards)):
                episode_return = reward + self.discount * episode_return
                self.action_values.record(state, action, episode_return)

    def act(self, observation):
        greedy_action = self.action_values.greedy_action(observation)
        return self.exploration_strategy.choose_action(greedy_action)
