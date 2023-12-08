import aiohttp
import asyncio
from bs4 import BeautifulSoup

# url = 'https://itciket.uz/'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://books.toscrape.com/')
        web_content = await response.text()
        soup = BeautifulSoup(web_content, 'html.parser')
        all_quotes = soup.find_all(class_='product_pod')

        for quote in all_quotes:
            main_text = quote.find('h3').text
            print(main_text)

        all_price = soup.find_all(class_='product_price')
        for price in all_price:
            prices = price.find('p').text
            print(prices)


asyncio.run(main())