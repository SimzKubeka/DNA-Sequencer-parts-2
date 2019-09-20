# Introduction to Programming: Task 25
#[Friday 7th June]
#[DNA Sequencing done on python]

print("Hi There!\n")

#Dictionary of codons
codons = {
    "ATT" : "I", "ATC" : "I", "ATA" : "I",
    "CTT" : "L", "CTC" : "L", "CTA" : "L", "TTA" : "L", "TTG" : "L",
    "GTT" : "V", "GTC" : "V", "GTA" : "V", "CTG" : "V",
    "TTT" : "F", "TTC" : "F", 
    "ATG" : "M",
    }

#translate funtion that allos for refenecing
def translate(sequence):
    translated = " "
    for i in range(0, len(sequence), 3):
        code = sequence[i:i+3]
        if (code in codons):
           translated += codons[code]
        else:
            translated +=  "X"
    return translated
            
#mutate funtion that reads a file, replaces certain charercters of that file
#and the write that inpute to another flle
def mutate():
    dna = open("DNA.txt", "r").read()
    dna = dna.replace("\n","")
    normal_dna  = open("normalDNA.txt","w")
    mutated_dna  = open("mutatedDNA.txt","w")

    normal_dna.write(dna.replace("a","A"))
    mutated_dna.write(dna.replace("a","T"))

    normal_dna.close()
    mutated_dna.close()

mutate()

#txtTranslate funtion allows us to translate the file into their respective codons
def txtTranslate():
    normalDNA = open("normalDNA.txt", "r").read()
    mutatedDNA = open("mutatedDNA.txt", "r").read()

    print("\nNormal DNA")
    print(translate(normalDNA))
    print("\nMutated DNA")
    print(translate(mutatedDNA))

txtTranslate()

print("\n     -------------")
print("el alto colectivo")
print("     -------------\n")
