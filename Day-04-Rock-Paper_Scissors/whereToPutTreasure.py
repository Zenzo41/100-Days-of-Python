row1 = ['⬜️','⬜️','⬜️']
row2 = ['⬜️','⬜️','⬜️']
row3 = ['⬜️','⬜️','⬜️']

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where fo you wanna put the treasure? ")
# input : 32
horizontal = int(position[0]) # 3rd row
vertical = int(position[1])  # 2nd column

selected_row = map[vertical - 1] 
selected_row[horizontal - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
