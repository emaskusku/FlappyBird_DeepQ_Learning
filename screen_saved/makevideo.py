#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
import os
from PIL import Image

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

shape = (288, 512, 3)
frameSize = (288, 512)

out = cv2.VideoWriter('../output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)

names = []
for filename in glob.glob('screen_*.jpg'):
    names.append(filename)

names.sort()
for name in names:
    img = cv2.imread(name)
    out.write(img)


out.release()