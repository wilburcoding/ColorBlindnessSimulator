from PIL import Image
import os
matrixes = { # preset matrixes
    "Normal":  { # normal people
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
# achro = convertColor(matrixes["Achromatopsia"],[241, 204, 35])
width, height = im.size
data = {
    "Normal":0,
  "Protanopia" : 0,
  "Protanomaly":0,
  "Deuteranopia":0,
  "Deuterranomaly":0,
  "Tritanopia":0,
  "Tritanomaly":0,
  "Achromatopsia":0,
  "Achromatomaly":0
}
loading = 0
for i in range(int(width)):
  for j in range(int(height)):
    pixel = px[i,j] 
    for item in list(matrixes):
      if item != "i":
        convertedColor = convertColor(matrixes[item],pixel)
        if (findSimilarity(convertedColor, pixel) > 90):
          data[item]+=1
  if (i % (int(width/100)) == 0):
    clear()
    print(str(loading) + "%")
    loading+=1
clear()
print("Finish parsing data..." + str(width*height) + "px...")
print("% of >90% Similarity based on condition")
for item in list(data):
  percent = round((data[item]/(int(width)*int(height)))*100, 2)
  if (percent < 10):
    percent = "\033[38;2;255;86;86m" + str(percent) + "%\033[0m"
  elif (percent < 40):
    percent = "\033[38;2;255;163;86m" + str(percent) + "%\033[0m"
  elif (percent < 75):
    percent = "\033[38;2;255;229;86m" + str(percent) + "%\033[0m"
  else:
    percent = "\033[38;2;168;255;86m" + str(percent) +  "%\033[0m"
  print(item + ": " + str(percent))