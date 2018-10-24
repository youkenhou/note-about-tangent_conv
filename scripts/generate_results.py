import os
import numpy as np

results_path = "dhn/outputs"
#results_path = "/tangent_conv/scripts"
result_name = "extrapolated.labels"

folders = os.listdir(results_path)

for name in folders:
    label = np.loadtxt(os.path.join(results_path, name, result_name))
    label = label - 1
    label = label.astype(int)
    np.savetxt(name, label, fmt="%d")
    cmd = "mv " + name + " /ali_data/results2/"
    os.system(cmd)
    print("done with " + name)