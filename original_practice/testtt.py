import aiohttp
import asyncio
import json

async def diwas_tok():
    url = "https://checkout.pci.shopifyinc.com/sessions"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Origin": "https://checkout.pci.shopifyinc.com",
        "Referer": "https://checkout.pci.shopifyinc.com/"
    }
    
    
    
    payload = {
        "credit_card": {
            "number": "4980 0165 6828 8452",
            "name": "John Banega Don",
            "month": 10,
            "year": 2031,
            "verification_value": "833"
        },
        "payment_session_scope": "www.dyleenfashion.com"
    }
    
    async with aiohttp.ClientSession() as session:
        print(f" {url}")
        try:
            async with session.post(url, json=payload, headers=headers) as resp:
                print(f"{resp.status}")
                text = await resp.text()
                print(f" {text}")
        except Exception as e:
            print(f"{e}")

    
    url_old = "https://deposit.shopifycs.com/sessions"
    print(f"\n {url_old}")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url_old, json=payload, headers=headers) as r:
                print(f"{r.status}")
                text = await r.text()
                print(f" {text}")
        except Exception as e:
            print(f"{e}")

if __name__ == "__main__":
    asyncio.run(diwas_tok())
