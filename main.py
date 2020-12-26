from lxml import etree
import cairosvg
import os

SOURCE_COLOR = 'svg xmlns'
TARGET_COLOR = 'svg fill="#FFFFFF" xmlns'
for file in os.listdir("svgs"):
  tree = etree.parse(open("svgs/" + file, 'r'))

  for element in tree.iter():
    if element.tag.split('}')[1] == 'path':
      if "fill" not in element.attrib:
        element.set("fill", "#FFFFFF")
    else:
      continue
  
  newBytes = etree.tostring(tree)
  try:
    cairosvg.svg2png(bytestring=newBytes, write_to=f"pngs/{file}.png")
  except Exception as e:
    print(e)
    pass
