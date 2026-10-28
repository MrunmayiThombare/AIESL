rules = {
    "fever" : "Flu",
    "cough" : "Flu",
    "runny_nose" : "Cold",
    "sneezing" : "Cold"
}

symptom = input("Enter the symptom : ").lower().replace(" ", "_")
print("Possible disease : ",rules.get(symptom, "no possible diagnosis"))
