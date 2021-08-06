import re

destination = input()
places = []
pattern = r'(=|/)(?P<destination>[A-Z][A-Za-z]{2,})\1'
result = re.finditer(pattern, destination)
for match in result:
    places.append(match.group("destination"))
print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {len(''.join(places))}")
