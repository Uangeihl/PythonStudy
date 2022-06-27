# import gym
# env = gym.make("Taxi-v3")
# observation = env.reset()
# agent = load_agent()
# for _ in range(100):
from gym import envs
env_specs = envs.registry.all()
envs_ids = [env_spec.id for env_spec in env_specs]
print(envs_ids)
