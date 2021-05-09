"""West-East elevation profile through Olympus Mons."""
from PIL import Image, ImageDraw, ImageOps
from matplotlib import pyplot as plt

# Load image and get x and z values along horiz profile parallel to y _coord.
x_coord = 375
im = Image.open('mola_1024x512_200mp.jpg').convert('L')
#im_p = Image.open('mola_1024x512_200mp.jpg').convert('RGBA')
width, height = im.size
x_vals = [x for x in range(x_coord)]
y_vals = [y for y in reversed(range(height))]
z_vals = [im.getpixel((x, y)) for x,y in zip(x_vals, y_vals)]

# Draw profile on MOLA image.
draw = ImageDraw.Draw(im)
draw.line((0, height, x_coord, 0), fill=255, width=3)
draw.text((100, 165), 'Olympus Mons', fill=255)
draw.text((680, 360), 'Hellas\nPlanitia', fill=255)


text_layer1 = Image.new("L", im.size,(0))
#text_layer = Image.new("RGBA", im.size,(0,0,0,0))
draw = ImageDraw.Draw(text_layer1)
text_center1=(150, 270)
draw.text(text_center1,'Tharsis Montes', fill='white')
rotated_text_layer1 = text_layer1.rotate(55,center=text_center1, expand=False)
#rotated_text_layer.show()
im.paste(Image.new("L",im.size,0),mask=rotated_text_layer1)
#im_p.alpha_composite(rotated_text_layer)

text_layer2 = Image.new("L", im.size,(0))
draw = ImageDraw.Draw(text_layer2)
text_center2=(250, 280)
draw.text(text_center2,'Valles Marineris', fill='white')
rotated_text_layer2 = text_layer2.rotate(-15,center=text_center2, expand=False)
im.paste(Image.new("L",im.size,0),mask=rotated_text_layer2)
im.show()    

# Make profile plot.
fig, ax = plt.subplots(figsize=(9, 4))
axes = plt.gca()
axes.set_ylim(0, 400)
ax.plot(x_vals, z_vals, color='black')
ax.set(xlabel='x-coordinate',
       ylabel='Intensity (height)',
       title="Mars Elevation Profile (Tharsis Montes)")
ratio = 0.15  # Reduces vertical exaggeration in profile.
xleft, xright = ax.get_xlim()
ybase, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybase-ytop)) * ratio)
#plt.text(0, 310, 'WEST', fontsize=10)
#plt.text(980, 310, 'EAST', fontsize=10)
#plt.text(100, 280, 'Olympus Mons', fontsize=8)
##ax.grid()
plt.show()
