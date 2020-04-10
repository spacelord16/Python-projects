import os
import random

folder_nmes = ["dfsd","gfdgdg","weioqwieq","sdiosr"]
dir = ""
for i in range(1000):
    keks = random.choice(folder_nmes)
    os.mkdir(os.path.join(dir, keks))
    dir = os.path.join(dir, keks)
