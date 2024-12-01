import asyncio
import pyppeteer

async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()

    test_html_string = open("Crop_Theft_2024_12_01.html", "r").read()
    await page.setContent(test_html_string)
    await page.screenshot({'path': "full-page.png", 'fullPage': True})

    await browser.close()

asyncio.run(main())
