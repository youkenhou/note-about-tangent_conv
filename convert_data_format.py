from util.path_config import *
from util.dataset_params import *
from util.cloud import *
from util.common import *

import os
import csv
import json

data_path = "../ali_data"
pts_path = "../ali_data/training/pts"
category_path = "../ali_data/training/category"
intensity_path = "../ali_data/training/intensity"
result_path = "../ali_data/train_data"
pts_files = os.listdir(pts_path)

frame = 0

for pts in pts_files:
    points = []
    #intensity = []
    labels = []
    with open(os.path.join(pts_path, pts)) as f:
        cnt = 0
        pts_content = csv.reader(f)
        for entry in pts_content:
            points.append(np.asarray(entry[0:3]))
            if cnt % 10000 == 0:
                print(cnt)
            cnt += 1

    os.mkdir(os.path.join(result_path, pts))
    pcd = PointCloud()
    pcd.points = Vector3dVector(points)
    write_point_cloud(os.path.join(result_path, pts, "scan.pcd"), pcd)

    cmd = "cp " + os.path.join(category_path, pts) + " " + os.path.join(result_path, pts, "scan.labels")
    os.system(cmd)
    if frame%100 == 0:
        print("done with 100 frames")
    frame += 1