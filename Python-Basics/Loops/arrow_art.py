picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

new_line = ""
loop = True
counter = 0

for index, row in enumerate(picture):
    while loop == True:
        for index, element in enumerate(row):
            if element == 0:
                new_line += " "
            elif element == 1:
                new_line += "*"
        new_line += " " * 8
        counter += 1

        if counter >= 4:
            loop = False
    print(new_line)
    new_line = ""
    loop = True
    counter = 0