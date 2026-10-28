import random
r = {
    "hello" : ["Hi , how may i help u ? "],
    "hi" : ["Hi , what do u need me for ? "],
    "how are u" : ["Hi , I am totally fine, thanku"],
    "who are you" : ["I am python chatbot !!"],
    "bye" : ["Goodbye !!"]
}

while True : 
    s = input("You : ").lower().strip()
    if s == "bye":
        print("Bot : ",random.choice(r["bye"]))
        break

    for k in r :
        if k in s:
            print("Bot : ",random.choice(r[k]))
            break

    else :
        print("Sorry , could'nt understand this requent pls try again!!")
