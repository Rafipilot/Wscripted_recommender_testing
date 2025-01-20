import ao_core as ao
import math
import numpy as np
# from arch__tester import arch
from embedding_snippets import embedding_response

import ao_arch as ar

description = "Wscripter tester"

description = "Wscripted- Personal Curation Agent - demo #1"
arch_i = [7, 21, 21]               # 7 binary neurons each for Genre, Theme, and Comparative Title
arch_z = [10]                       # 10 binary neurons for output-- if the sum of the response >7, positive recommendation
arch_c = []
connector_function = "full_conn"

# connector_parameters = [32, 16, 32, 10]



# To maintain compatibility with our API, do not change the variable name "Arch" or the constructor class "ao.Arch" in the line below (the API is pre-loaded with a version of the Arch class in this repo's main branch, hence "ao.Arch")
arch = ar.Arch(arch_i, arch_z, arch_c, connector_function, description)


a = ao.Agent(arch, save_meta=True)

# inn = np.random.randint(0, 2, 7+21+21)
# inn = np.zeros(7+21+21)
# inn = np.ones(7+21+21)
# a.next_state(inn, LABEL=np.zeros(10))
# a.reset_state()
a.next_state( np.zeros(7+21+21), LABEL=np.zeros(10))
a.reset_state()
a.next_state( np.ones(7+21+21), LABEL=np.zeros(10))
a.reset_state()
a.next_state( np.zeros(7+21+21), LABEL=np.zeros(10))
a.reset_state()
a.next_state( np.ones(7+21+21), LABEL=np.zeros(10))
a.reset_state()

for i in range(5):
    inn = np.random.randint(0, 2, 7+21+21)
    inn2 = np.random.randint(0, 2, 7+21+21)
    inn3 = np.random.randint(0, 2, 7+21+21)
    rand = np.random.randint(0, 2, 10)
    a.next_state(inn, LABEL=np.zeros(10))
    a.reset_state()
    a.next_state(inn2, LABEL=np.ones(10))
    a.reset_state()
    a.next_state(inn3, LABEL=rand)
    a.reset_state()

num_binary_digits = 7

def get_binary(id):
    bucket_binary = np.array(list(np.binary_repr(id, num_binary_digits)), dtype=int)
    return bucket_binary.tolist()


#%%
### Main loop -- Run this whole call for a particular input

training = "n" # or "y" or "yneg" for dislike

# Inception
# user_input = ["Science Fiction Thriller", "Dream manipulation", "Redemption", "Subconscious guilt", "The Matrix", "Minority Report", "Eternal Sunshine of the Spotless Mind"]

## Goldfinger
# user_input = ["Spy Thriller", "Espionage", "International Intrigue", "High-tech Gadgetry", "Casino Royale", "The Bourne Identity", "Mission: Impossible"]

## Fight Club
# user_input = ["Psychological Thriller", "Identity Crisis", "Societal Rebellion", "Masculinity", "American Psycho", "The Machinist", "Memento"]

## The Matrix
# user_input = ["Science Fiction Thriller", "Reality vs Illusion", "Human vs Machine", "Destiny and Free Will", "Inception", "Ready Player One", "Blade Runner"]

## It's a Wonderful Life
user_input= ["Drama", "Self-sacrifice", "Community", "Personal fulfillment", "A Christmas Carol", "The Bishop's Wife", "Mr. Smith Goes to Washington"]

input_to_a= embedding_response(user_input)


## Old logic for calling agent with ids only, without embedding bucketing module
# # Get user input
# genre_id = int(input("Genre ID: "))

# theme_id1 = int(input("Theme ID 1: "))
# theme_id2 = int(input("Theme ID 2: "))
# theme_id3 = int(input("Theme ID 3: "))

# comp_title_id1 = int(input("Comp Title ID 1: "))
# comp_title_id2 = int(input("Comp Title ID 2: "))
# comp_title_id3 = int(input("Comp Title ID 3: "))

# #convert inputs to binary
# genre_binary = get_binary(genre_id)

# theme_binary1 = get_binary(theme_id1)
# theme_binary2 = get_binary(theme_id2)
# theme_binary3 = get_binary(theme_id3)

# comp_title_binary1 = get_binary(comp_title_id1)
# comp_title_binary2 = get_binary(comp_title_id2)
# comp_title_binary3 = get_binary(comp_title_id3)

# #combine inputs for the a
# input_to_a = genre_binary + theme_binary1 + theme_binary2 + theme_binary3 + comp_title_binary1 + comp_title_binary2 + comp_title_binary3


if "y" in training: #testing
    label = np.ones(10)
    if "neg" in training:
        label = np.zeros(10)            
    a.reset_state()
    a.next_state(input_to_a, LABEL=label, print_result=True)
    print("Agent trained")
else:
    a.reset_state()
    for i in range(5):
        result = a.next_state(input_to_a, print_result=True)
        percentage = np.sum(result)*10
    print("Final recommendation:  "+str(percentage)+"%")