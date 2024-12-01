import asyncio
import pyppeteer
import json
import os

async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()

    json_path = input("Input JSON path: ")
    json_array = json.loads(open(json_path, "r").read())

    output_directory = "images"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i, html_string in enumerate(json_array):
        await page.setContent(html_string)
        await page.screenshot({'path': output_directory + "/" + str(i) + ".png", 'fullPage': True})

    await browser.close()

asyncio.run(main())
