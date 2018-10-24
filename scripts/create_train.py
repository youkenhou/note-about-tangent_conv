import os

#data = "../ali_data/train_data"
data = "data/ali"

files = os.listdir(data)
i = 1

train = open("train.txt","a")
validation = open("validation.txt", "a")

for f in files:
    if i <= 1600:
        train.write(f+"\n")
        i += 1
    else:
        validation.write(f+"\n")
        i += 1

train.close()
validation.close()