
import ao_arch as ar

description = "Basic Recommender System"

#genre, length
arch_i = [5]   # genre_binary_encoding + length_binary + fnf_binary + mood_binary
arch_z = [1]           
arch_c = []           
connector_function = "full_conn"

# To maintain compatibility with our API, do not change the variable name "Arch" or the constructor class "ao.Arch" in the line below (the API is pre-loaded with a version of the Arch class in this repo's main branch, hence "ao.Arch")
arch = ar.Arch(arch_i, arch_z, arch_c, connector_function, description)