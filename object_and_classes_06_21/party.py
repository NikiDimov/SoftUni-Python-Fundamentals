class Party:
    def __init__(self):
        self.people = []


party_people = Party()
name = input()
while not name == "End":
    party_people.people.append(name)
    name = input()
print(f"Going: {', '.join(party_people.people)}")
print(f"Total: {len(party_people.people)}")


