import os
import csv
import numpy as np

file_path = "/ali_data/processed_data"

class_file_path = os.listdir(file_path)

classes = np.zeros((1, 8))

for cate in class_file_path:
    
    with open(os.path.join(file_path, cate, "scan.labels")) as f:
        for entry in f:
            classes[0, int(entry)] += 1

class_freq = classes/np.sum(classes)

np.savetxt("ali_class_freq", classes)

print(class_freq)
