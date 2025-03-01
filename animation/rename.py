import os

files_names = os.listdir("./images")
for f_n in files_names:
    os.rename(f"./images/{f_n}", f"./images/{f_n}".\
        replace(" ","").replace("(","").replace(")", ""))

# create a class For Player
# player has two animation types -> 1) Idle     1) Run
# when player moves change animation to Run   
# And when doesn't move change animation to Idle