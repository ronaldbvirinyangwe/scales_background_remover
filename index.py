from rembg import remove
from PIL import Image

input_path = 'hi.png'
output_path = 'hi.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open("hi.png")