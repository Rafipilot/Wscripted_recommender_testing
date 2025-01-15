import ao_core as ao
import math
import numpy as np
from arch__tester import arch

agent = ao.Agent(arch)

for i in range(4):
     agent.reset_state()
     agent.reset_state(training=True)

num_binary_digits = 5

def get_binary(id):
    bucket_binary = np.array(list(np.binary_repr(id, num_binary_digits)), dtype=int)
    return bucket_binary.tolist()


#Main loop
while True:
    training = input("You want to train (y/n) : ")
    # Get user input
    genre_id = int(input("Genre ID: "))
    theme_id = int(input("Theme ID: "))
    comp_title_id = int(input("Comp Title ID: "))

    #convert inputs to binary
    genre_binary = get_binary(genre_id)
    theme_binary = get_binary(theme_id)
    comp_title_binary = get_binary(comp_title_id)

    #combine inputs for the agent
    input_to_agent = genre_binary + theme_binary + comp_title_binary

    if "y" in training: #testing
        label = int(input("Label to agent ( 0 -don't recommed / 1 -recommed): "))
        label = [label]
        print(label)
        for i in range(5):
            agent.next_state(input_to_agent, LABEL=label, print_result=True)
    else:
        for i in range(5):
            agent.next_state(input_to_agent, print_result=True)


    
   
        