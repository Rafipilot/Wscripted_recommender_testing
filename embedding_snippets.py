#################
# PREPARING BINARY INPUT DATA FOR API.AOLABS.AI

import embedding_bucketing.embedding_model_test as em # pip install git+https://github.com/Rafipilot/embedding_bucketing
import numpy as np

from config import openai_api_key  # you'll need an OpenAPI key
em.config(openai_api_key)

## Run this code first to generate your caches first to then use the function below 

## GENRE
starting_genre_buckets= ["Comedy", "Drama", "Action"] # if you have an existing list of categories, list them here
cache_genre, genre_buckets = em.init("cache_genre.json", starting_genre_buckets)  # will be saved or loaded from your current working directory

## THEME
start_theme = ["Love", "Sacrifice", "Sad", "Death", "Dark"]
cache_theme, theme_buckets = em.init("cache_theme.json", start_theme)

## COMPARATIVE TITLE
starting_comparative_title_buckets = ["romeo and juliet", "the great gatsby", "harry potter", "oliver twist", "an inspector calls" ]
cache_comp, comparative_title_buckets = em.init("cache_comparative_title.json", starting_comparative_title_buckets)


def embedding_response(new_inn):

    new_genre_input = new_inn[0]
    new_theme_input = [new_inn[1], new_inn[2], new_inn[3]]
    new_comparative_input =  [new_inn[4], new_inn[5], new_inn[6]]

    # Constants - no need to change these
    max_distance = 0.4 # max distance a word can be from the closest bucket before we create a new bucket
    type_of_distance_calc="COSINE SIMILARITY" # another option to try is "EUCLIDEAN DISTANCE"   
    amount_of_binary_digits= 7 # amount of binary digits for the bucket to be encoded into; e.g if "Romance" has bucket id 5, its binary representation would be 0000000101

    # Function to get the closest bucket and its binary encoding
    def embedding_bucketing_response(cache, uncategorized_input, max_distance, bucket_list, type_of_distance_calc, amount_of_binary_digits):
        sort_response = em.auto_sort(cache, uncategorized_input, max_distance, bucket_list, type_of_distance_calc, amount_of_binary_digits) 

        closest_distance = sort_response[0]
        closest_bucket   = sort_response[1]  # which bucket the uncategorized_input was placed in
        bucket_id        = sort_response[2]  # the id of the closest_bucket
        bucket_binary    = sort_response[3]  # binary representation of the id for INPUT into api.aolabs.ai

        return closest_bucket, bucket_binary # returning the closest bucket and its binary encoding


    # Call for genre
    # new_genre_input  = "Documentary"
    closest_genre, genre_encoding = embedding_bucketing_response(cache_genre, new_genre_input, max_distance, genre_buckets, type_of_distance_calc, amount_of_binary_digits)
    print("Closest Genre to: ", new_genre_input, "is", closest_genre)


    # Call for theme
    # new_theme_input = ["Romance", "Thriller", "Horror"]
    theme_encodings = []
    closest_theme_buckets = []

    for i in range(len(new_theme_input)):  # Iterate using indices
        closest_theme, theme_encoding = embedding_bucketing_response(cache_theme, new_theme_input[i], max_distance, theme_buckets, type_of_distance_calc, amount_of_binary_digits)
        closest_theme_buckets = np.append(closest_theme_buckets, closest_theme)
        theme_encodings = np.append(theme_encodings, theme_encoding)
        print("Encoded: ", new_theme_input[i], "into ", "Bucket: ", closest_theme, "With Binary Encoding: ", theme_encoding)

    theme_encodings = theme_encodings.astype(int)
    print("Inputs Closest to: ", closest_genre, "Closest thene: ", closest_theme_buckets)


    # Call for comparative title
    # new_comparative_input = ["beauty and the beast", "the red october", "the big short"]
    comparative_title_encodings = []
    closest_comparative_title_buckets= []
    for i in range(len(new_comparative_input)):
        closest_comp_bucket, comparative_title_encoding = embedding_bucketing_response(cache_comp, new_comparative_input[i], max_distance, comparative_title_buckets, type_of_distance_calc, amount_of_binary_digits)
        closest_comparative_title_buckets = np.append(closest_comparative_title_buckets, closest_comp_bucket)
        comparative_title_encodings = np.append(comparative_title_encodings, comparative_title_encoding)
        print("Encoded: ", new_comparative_input[i], "into ", "Bucket: ", closest_comp_bucket, "With binary encoding: ", comparative_title_encoding)

    comparative_title_encodings = comparative_title_encodings.astype(int)
    print("Inputs Closest to: ", closest_genre, closest_theme, "Closest comparative titles: ", closest_comparative_title_buckets)


    ## INPUT TO API
    ao_input_binary_array = np.zeros(49, dtype=int) # Adding genre, theme, and comp title encodings into one binary array
    ao_input_binary_array[0:7] = genre_encoding
    ao_input_binary_array[7:28]= theme_encodings
    ao_input_binary_array[28:49]= comparative_title_encodings

    INPUT_AO_api = ''.join(map(str,ao_input_binary_array))  # right now, our API accepts only binary strings as input
    print("input to ao: ", INPUT_AO_api)

    return ao_input_binary_array