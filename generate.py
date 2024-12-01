import asyncio
import pyppeteer
import json

async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()

    json_path = input("Input JSON path: ")

    json_array = json.loads(open(json_path, "r").read())

    for i, html_string in enumerate(json_array):
        await page.setContent(html_string)
        await page.screenshot({'path': "images/" + str(i) + ".png", 'fullPage': True})

    await browser.close()

asyncio.run(main())
