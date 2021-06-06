fires_with_their_cells = input().split("#")
amount_of_water = int(input())
cells = []
effort = 0

for el in fires_with_their_cells:
    type_of_fire, value_of_cells = el.split(" = ")
    value_of_cells = int(value_of_cells)
    if type_of_fire == "High":
        if value_of_cells in range(81, 126) and amount_of_water >= value_of_cells:
            cells.append(value_of_cells)
            amount_of_water -= value_of_cells
            effort += value_of_cells * 0.25
    elif type_of_fire == "Medium":
        if value_of_cells in range(51, 81) and amount_of_water >= value_of_cells:
            cells.append(value_of_cells)
            amount_of_water -= value_of_cells
            effort += value_of_cells * 0.25
    elif type_of_fire == "Low":
        if value_of_cells in range(1, 51) and amount_of_water >= value_of_cells:
            cells.append(value_of_cells)
            amount_of_water -= value_of_cells
            effort += value_of_cells * 0.25

print("Cells:")
for el in cells:
    print(f" - {el}")
print(f"Effort: {effort:.2f}\nTotal Fire: {sum(cells)}")

