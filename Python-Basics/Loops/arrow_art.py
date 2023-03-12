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

for row in picture:
    while loop == True:
        for element in row:
            if element == 0:
                new_line += " "
            elif element == 1:
                new_line += "*"

        new_line += " " * 8
        counter += 1

        # Controls the number of times the image should be drawn before breaking
        if counter >= 4:
            loop = False

    print(new_line)
    new_line = ""
    loop = True
    counter = 0