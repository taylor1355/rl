import gym
import rl

from rl import agents
from rl import exploration
from rl import wrappers

if __name__ == '__main__':
    # environment = gym.make('Roulette-v0')
    environment = gym.make('Taxi-v3')
    # environment = gym.make('CartPole-v0')
    # environment = gym.make('MountainCar-v0')

    environment = wrappers.BaseWrapper(environment)

    explore_strategy = exploration.EpsilonGreedy(environment.action_space, epsilon=0.01)
    discount = 0.99

    agents_to_train = [
        agents.tabular.OnPolicyMonteCarloAgent(environment, explore_strategy, discount),
        agents.tabular.OffPolicyMonteCarloAgent(environment, explore_strategy, discount),
        agents.tabular.SarsaAgent(environment, explore_strategy, discount, 0.05),
        agents.tabular.ExpectedSarsaAgent(environment, explore_strategy, discount, 0.05),
        agents.tabular.QLearningAgent(environment, explore_strategy, discount, 0.05),
        agents.tabular.DoubleQLearningAgent(environment, explore_strategy, discount, 0.05)
    ]

    for agent in agents_to_train:
        runner = rl.Runner(environment, agent)
        runner.train(1000)
        # runner.run(10, 10000)
