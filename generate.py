import asyncio
import playwright.async_api
import json
import os
import PIL.Image
import cv2
import configparser
import sys
import shutil

def maybe_read_config(maybe, section, name = None):
    try:
        config = configparser.RawConfigParser()
        config.read(os.path.dirname(__file__) + "/" + "config.ini", encoding="utf-8")

        if name == None:
            return config[section]

        return config[section][name]

    except Exception as e:
        print(e)
        return maybe

images_output_directory = maybe_read_config("images", "config", "images_output_directory")
images_output_format = maybe_read_config("png", "config", "images_output_format")
image_width = int(maybe_read_config(1920, "config", "image_width"))
image_style = maybe_read_config("dark", "config", "image_style")
video_output_name = maybe_read_config("output_timelapse.mp4", "config", "video_output_name")
video_codec = maybe_read_config("mp4v", "config", "video_codec")
video_framerate = int(maybe_read_config(5, "config", "video_framerate"))

def dedupe_consecutive(json_array):
    return [v for i, v in enumerate(json_array) if i == 0 or v != json_array[i-1]]

async def generate_images(json_array):
    playwright_session = await playwright.async_api.async_playwright().start()
    browser = await playwright_session.chromium.launch()
    page = await browser.new_page()
    await page.set_viewport_size({"width": image_width, "height": 1}) #height will grow to whatever size it needs for the screenshot

    json_array_length = len(json_array)
    for i, html_string in enumerate(json_array):
        filename = str(i).zfill(len(str(json_array_length)))
        await page.set_content(html_string)
        if image_style == "dark":
            await page.add_style_tag(path = "dark.css")
        elif image_style == "light":
            await page.add_style_tag(path = "light.css")
        await page.screenshot(path = images_output_directory + "/" + filename + "." + images_output_format, full_page = True)
        print("Generated " + filename + "/" + str(json_array_length - 1))
        sys.stdout.write("\033[F")
    sys.stdout.write("\n")

    await browser.close()
    await playwright_session.stop()

def resize_images():
    highest_width = 0
    highest_height = 0

    image_paths = sorted(os.listdir(images_output_directory))

    for image_file in image_paths:
        image = PIL.Image.open(os.path.join(images_output_directory, image_file))

        current_width, current_height = image.size
        if current_width > highest_width:
            highest_width = current_width
        if current_height > highest_height:
            highest_height = current_height

    image_paths_length = len(image_paths)
    for image_file in image_paths:
        bg_color = (0,0,0,0) #transparent
        if image_style == "dark":
            bg_color = (44,44,44,255) #2c2c2c
        elif image_style == "light":
            bg_color = (255,255,255,255) #ffffff
        image = PIL.Image.open(os.path.join(images_output_directory, image_file))
        new_image = PIL.Image.new("RGBA", size = (highest_width, highest_height), color = bg_color)
        new_image.paste(image)
        new_image.save(images_output_directory + "/" + image_file, images_output_format)
        print("Resized " + image_file.split(".")[0] + "/" + str(image_paths_length - 1))
        sys.stdout.write("\033[F")
    sys.stdout.write("\n")

def generate_video():
    images = sorted(os.listdir(images_output_directory))
    print("Found " + str(len(images)) +  " images for video")

    frame = cv2.imread(os.path.join(images_output_directory, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_output_name, cv2.VideoWriter_fourcc(*video_codec), video_framerate, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(images_output_directory, image)))

    video.release()
    cv2.destroyAllWindows()
    print("Video generated successfully!")

skip_image_processing = input("Skip image generation (images must already be generated) (y/N): ").lower()
if skip_image_processing in ["y", "yes"]:
    print("Generating video")
    generate_video()
    sys.exit()

json_path = input("Input Timelapse JSON path: ")
json_array = json.loads(open(json_path, "r").read())

dedupe_json_array = input("Remove consecutive duplicates (days where nothing changed) (y/N): ").lower()
if dedupe_json_array in ["y", "yes"]:
    json_array = dedupe_consecutive(json_array)

if os.path.exists(images_output_directory):
    shutil.rmtree(images_output_directory)
os.makedirs(images_output_directory)

print("Generating images")
asyncio.run(generate_images(json_array))

print("Resizing images")
resize_images()

print("Generating video")
generate_video()
