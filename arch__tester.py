
import ao_arch as ar

description = "Wscripter tester"

description = "Wscripted- Personal Curation Agent - demo #1"
arch_i = [7, 21, 21]               # 7 binary neurons each for Genre, Theme, and Comparative Title
arch_z = [10]                       # 10 binary neurons for output-- if the sum of the response >7, positive recommendation
arch_c = []
connector_function = "full_conn"

# To maintain compatibility with our API, do not change the variable name "Arch" or the constructor class "ao.Arch" in the line below (the API is pre-loaded with a version of the Arch class in this repo's main branch, hence "ao.Arch")
arch = ar.Arch(arch_i, arch_z, arch_c, connector_function, description)