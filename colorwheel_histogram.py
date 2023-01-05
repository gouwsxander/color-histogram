from PIL import Image
import colorsys
import numpy as np
import matplotlib.pyplot as plt

# Get source image
source_image_path = input("")
source = Image.open(source_image_path).convert('RGB')

THETA = []
R = []
C = []

for i in range(0, source.width, 5):
    for j in range(0, source.height, 5):
        r, g, b = source.getpixel((i, j))
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        THETA.append(2 * np.pi * h)
        R.append(s)
        C.append([r/255, g/255, b/255, 0.25])

#plt.rcParams['figure.dpi'] = 700
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(5,5))

ax.scatter(THETA, R, 1, C)

ax.set_rmax(1)
ax.set_rticks([0.25,0.5,0.75,1])
#ax.set_thetagrids(np.arange(0, 360, 60))
ax.set_thetagrids(np.arange(0, 360, 60), ['R', 'Y', 'G', 'C', 'B', 'M'])
ax.set_yticklabels(['']*4)
ax.set_aspect(1)

plt.show()
