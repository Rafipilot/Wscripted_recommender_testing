
import ao_core as ao
from arch__tester import arch
import numpy as np

agent = ao.Agent(arch)
for i in range(4):
    agent.reset_state()
    agent.reset_state(training=True)

num_binary_digits = 5

def get_binary(id):
    bucket_binary = np.array(list(np.binary_repr(id, num_binary_digits)), dtype=int)
    blist = bucket_binary.tolist()

    return blist 




while True:
    genre_id = int(input("Genre id: "))
    theme_id = int(input("theme id; "))
    genre_binary = get_binary(genre_id)
    theme_binary = get_binary(theme_id)

    Input_to_agent = genre_binary + theme_binary
    agent.next_state(Input_to_agent, print_result=True)

    recommendation_result = input("Did you like the recommendation (y/n): ")

    if recommendation_result == "y":
        agent.next_state(Input_to_agent, LABEL=[1], print_result=True)
    else:
        agent.next_state(Input_to_agent, LABEL=[0], print_result=True)

