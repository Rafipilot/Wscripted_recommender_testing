
import json
import ao_core as ao
from arch__tester import arch
import numpy as np

agent = ao.Agent(arch)

num_binary_digits = 5

with open('cache_genre.json') as file:
    data = json.load(file)
bucket_id = data["buckets"]["Comedy"]["id"]

bucket_binary = np.array(list(np.binary_repr(bucket_id, num_binary_digits)), dtype=int)
Input_to_agent = bucket_binary.tolist()
print(len(data["buckets"]))
bucket_names = list(data["buckets"].keys())
print(bucket_names)



agent.next_state(Input_to_agent, print_result=True)

