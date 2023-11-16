from PIL import Image
import os
matrixes = { # preset matrixes
    "normal":  { # normal people
        "R":[100,      0,     0],
        "G":  [0,    100,      0],
        "B":  [0,      0, 100]},
    "Protanopia":   { # Any red light
        "R":[56.667, 43.333,  0],
        "G":[55.833, 44.167,  0],
        "B": [0,     24.167, 75.833]},
    "Protanomaly":  { # certain reds look different
        "R":[81.667, 18.333,  0],
        "G":[33.333, 66.667,  0],
        "B": [0,     12.5,   87.5]},
    "Deuteranopia": { # Any green light
        "R":[62.5, 37.5,  0],
        "G":[70,   30,    0],
        "B": [0,   30,   70]},
    "Deuterranomaly":{ # Green colors look red
        "R":[80,     20,      0],
        "G":[25.833, 74.167,  0],
        "B": [0,     14.167, 85.833]},
    "Tritanopia":   { # blue yellow colored blindness
        "R":[95,  5,      0],
        "G": [0, 43.333, 56.667],
        "B": [0, 47.5,   52.5]},
    "Tritanomaly":  { # dampens colors
        "R":[96.667, 3.333,   0],
        "G": [0,     73.333, 26.667],
        "B": [0,     18.333, 81.667]},
    "Achromatopsia":{ # near total absense of color vision
        "R":[29.9, 58.7, 11.4],
        "G":[29.9, 58.7, 11.4],
        "B":[29.9, 58.7, 11.4]},
    "Achromatomaly":{ # dull faded colors
        "R":[61.8, 32,    6.2],
        "G":[16.3, 77.5,  6.2],
        "B":[16.3, 32.0, 51.6]}
}
# Data source: https://github.com/MaPePeR/jsColorblindSimulator/blob/master/colorblind.js
def convertColor(matrix, rgb):
  r=rgb[0]
  g=rgb[1]
  b=rgb[2]
  return [
            round(r * matrix["R"][0] / 100.0 + g * matrix["R"][1] / 100.0 + b * matrix["R"][2] / 100.0),
            round(r * matrix["G"][0] / 100.0 + g * matrix["G"][1] / 100.0 + b * matrix["G"][2] / 100.0),
            round(r * matrix["B"][0] / 100.0 + g * matrix["B"][1] / 100.0 + b * matrix["B"][2] / 100.0)
        ];
def clear():
  os.system("clear")
def num_sim(n1, n2):
  if (n1+n2==0):
    return 1
  return 1 - abs(n1 - n2) / (n1 + n2)
def findSimilarity(rgb1, rgb2):
  simR = num_sim(rgb1[0], rgb2[0])
  simG = num_sim(rgb1[1], rgb2[1])
  simB = num_sim(rgb1[2], rgb2[2])
  return round((simR + simG + simB) / 3 * 100, 2)
print("Loading presets...")
im = Image.open("test1.jpg")
# test1 is sunflowers by van gogh
px = im.load() # Load pixels
oldpx = px
# achro = convertColor(matrixes["Achromatopsia"],[241, 204, 35])
width, height = im.size

loading = 0
for item in list(matrixes):
  loading=0
  px =im.load()
  print("Loading image for " + item)
  for i in range(int(width)):
    for j in range(int(height)):
      pixel = px[i,j] 
      convertedColor = convertColor(matrixes[item],pixel)
      px[i, j] = tuple(convertedColor)

    if (i % (int(width/20)) == 0):
      clear()
      print(str(loading) + "% " + item)
      loading+=5
  im.save("test1/result-" + item + ".jpg")
clear()
print("Finished")

