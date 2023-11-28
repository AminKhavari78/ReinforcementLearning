import random
import numpy as np

class Harness:

    def run_episode(self, agent):
        total_reward = 0
        for _ in range(1000):
            action = agent.next_action(current_state_agent_bot, episode)
            action = action['agent']
            step = step(action)
            step_x_agent = current_state_agent_bot['agent'][0] + step[0]
            step_y_agent = current_state_agent_bot['agent'][1] + step[1]
            current_state_agent_bot['agent'] = [step_x_agent, step_y_agent]
            reward_agent = agent.consume(container, 'agent')

            action = agent.next_action(current_state_agent_bot, episode)
            action = action['bot']
            step = step(action)
            step_x_bot = current_state_agent_bot['bot'][0] + step[0]
            step_y_bot = current_state_agent_bot['bot'][1] + step[1]
            current_state_agent_bot['agent'] = [step_x_bot, step_y_bot]
            reward_bot = agent.consume(container, 'bot')

            total_reward += reward_agent + reward_bot
            if done:
                break
        return total_reward


class LinearAgent:

    def __init__(self):
        self.parameters = np.random.rand(4) * 2 - 1
        self.partial_observe_agent = []
        self.partial_observe_bot = []
    # observation is limited...

    def next_action(self, current_state, episode):

        for i in range(4):
            for j in range(4):
                x = (i+1)*25 + current_state['agent'][0]
                y = (j+1)*25 + current_state['agent'][1]
                self.partial_observe_agent.append(x,y)

                x = (j+1)*25 + current_state['agent'][1]
                y = (j+1)*25 + current_state['agent'][1]
                self.partial_observe_bot.append(x, y)

        result_agent = np.matmul(self.parameters, self.partial_observe_agent)
        result_bot = np.matmul(self.parameters, self.partial_observe_bot)
        result_agent = 0 if result_agent < 0 else 1
        result_bot = 0 if result_bot < 0 else 1

        division = episode % 4
        result_agent += episode
        result_bot += episode

        dict_result = {
            'agent': result_agent,
            'bot': result_bot,
        }

        return dict_result

    def consume(self, container, who):
        key_local = []
        if who == 'agent':
            partial_observe = self.partial_observe_agent
        else:
            partial_observe = self.partial_observe_bot
        for key, value in container.items():
            for x, y in partial_observe:
                if value[1] == x and value[2] == y:
                    key_local.append(key, value[0])

        for key_locals, value_locals in key_local:
            if value_locals[1] == blue_berry_unripe or red_berry_unripe:
                continue
            else:
                consuming = random.choice(key_local)

                if who in consuming:
                    reward = 2
                else:
                    reward = 1
                container.pop(consuming)
                key_local.clear()
                partial_observe.clear()

                return reward


def random_search():
    best_params = None
    best_reward = 0
    agent = LinearAgent()
    harness = Harness()


    for step in range(2000):
        agent.parameters = np.random.rand(4) * 2 - 1
        reward = harness.run_episode(current_state, episode)
        if reward > best_reward:
            best_reward = reward
            best_params = agent.parameters
            if reward == 200:
                print('200 achieved on step {}'.format(step))

    print(best_params)

    pygame.quit()
    quit()
