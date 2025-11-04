species = {
    "bacteria" : 20,
    "archaea" : 15,
    "fungi" : 10
}
while True:
    new_species =  input("entrer la nouvelle espece") #we want to write the potentially new species
    if new_species=="stop": # with this if we can stop the while loop when ever we want just by typing "stop"
        print("vous n'avez plus de nouvelle espéce") #display a message "you don't have new species anymore"
        break
    else:
        if new_species in list(species): #if it's a new species, add to the list and give +1
                species[new_species] += 1
                print(species)
        else:
            species[new_species] = 1 #if it's not a new species, add +1 to the species already there
            print(species)