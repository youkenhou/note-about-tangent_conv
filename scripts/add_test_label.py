import os

labels = os.listdir("submit_example")

path = "data/test_data"

for label in labels:
    cmd = "cp " + os.path.join("submit_example", label) + " " + os.path.join(path,label, "scan.labels")
    os.system(cmd)