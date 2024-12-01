import asyncio
import pyppeteer
import json
import os
import PIL.Image

images_output_directory = "images"
images_output_format = "png"

async def generate_images():
    browser = await pyppeteer.launch()
    page = await browser.newPage()

    json_path = input("Input JSON path: ")
    json_array = json.loads(open(json_path, "r").read())

    if not os.path.exists(images_output_directory):
        os.makedirs(images_output_directory)

    json_array_length = len(json_array)
    for i, html_string in enumerate(json_array):
        filename = str(i).zfill(len(str(json_array_length)))
        await page.setContent(html_string)
        await page.screenshot({'path': images_output_directory + "/" + filename + "." + images_output_format, 'fullPage': True})
        print("Generated " + filename + "/" + str(json_array_length) - 1)

    await browser.close()

def resize_images():
    highest_width = 0
    highest_height = 0
    for image_file in os.listdir(images_output_directory):
        image = PIL.Image.open(os.path.join(images_output_directory, image_file))

        current_width, current_height = image.size
        if current_width > highest_width:
            highest_width = current_width
        if current_height > highest_height:
            highest_height = current_height

    for image_file in os.listdir(images_output_directory):
        image = PIL.Image.open(os.path.join(images_output_directory, image_file))
        image_resized = image.crop((0, 0, highest_width, highest_height))
        image_resized.save(images_output_directory + "/" + image_file, "PNG")

asyncio.run(generate_images())

resize_images()
