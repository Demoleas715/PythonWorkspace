state_birds={"NJ": "American bird thing",
             "NY": "DIFFERENT BIRD"}
state=list(state_birds.keys())
state_bird=input("Enter a state")
if state_bird==state_birds.keys():
    print(state_birds.get(state))