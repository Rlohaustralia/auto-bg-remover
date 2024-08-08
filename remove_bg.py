from rembg import remove
from PIL import Image
import io

input_source = 'input.jpg'
output_source = 'output.png'


with open(input_source, 'rb') as input:
    input_data = input.read()

# Call the remover function
output_data = remove(input_data)

with open(output_source, 'wb') as output:
    output.write(output_data)

