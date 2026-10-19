import requests
from bs4 import BeautifulSoup
import json
from discord_webhook import DiscordWebhook, DiscordEmbed

webhookUrl = "https://discord.com/api/webhooks/...."

headers = {
    'authority': 'api.nike.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.7',
    # 'cookie': 'geoloc=cc=US,rc=NY,tp=vhigh,tz=EST,la=40.7500,lo=-73.9967; AnalysisUserId=23.36.1.37.206391669992489968; AMCVS_F0935E09512D2C270A490D4D%40AdobeOrg=1; anonymousId=2073CA3503577ABA778F84C06269FB77; at_check=true; NIKE_COMMERCE_COUNTRY=US; NIKE_COMMERCE_LANG_LOCALE=en_US; nike_locale=us/en_us; s_ecid=MCMID%7C69766903964148132471817867691910690607; AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C69766903964148132471817867691910690607%7CMCAID%7CNONE%7CMCOPTOUT-1675892149s%7CNONE%7CvVersion%7C3.4.0; AKA_A2=A; audience_segmentation_performed=true; bm_sz=DF520276BE964FAC429606730F21FA99~YAAQmJIuFzPdvy+GAQAAFLmnQRK3JipvJRvJgzRnGg79iO8Pkuy5daMb/lJxl0ZbyXyoDxB3cP7da+hTIdp8LPhWYgfdA+/IRdmiAiahyfEJ1zEK1wFD83auzU9uq7DfP7A0cNdtCumb9JM63DkFx7HizFg9NFl3TBykjkONCSxudcGErew1rlvha7u4n3yX5rOP0x77WapyLg+6l0I5NzjvqgtF+hsgbV+uGDut0GQovrsxljz7Q9jc9GvG1WW1uuRzeSt66J1AbQPwQvF3ndNDz3JitfS9dWLWHKQ7F9WDdITNh8JFnSNQmLxVPpMMh7ryGdIH0mAMt/CHMaoikKKHhBXvTDbmWFgNqxfOxMIYFLPuwwbwglTGy5/pa6WDzgYjb2RFaBtE82AAvLi09V93~3291202~3224644; optimizelyEndUserId=oeu1676138756354r0.08173428524336201; ak_bmsc=6DEC8AB4C4462864CCE3578D0BA7BEF3~000000000000000000000000000000~YAAQmJIuF/Hdvy+GAQAA+76nQRKhomNBNLKLaUN7nAnudb3AI1k/vFC0bAI/CPzUxnkaX2T7+IqIrjNyk3nqj0/tayDeQkYNT34jJhCKl746vsZuYXe4etk51mCtvByrW7EUqyt1Rk5HiloC3ZHTJp5bxJjlThcu0fHiiIY8zpywFIotwQQYe9ZRO9hB8sFi1bGXraa/u1aCuN7b3t+KAv7eAKLMck0XGwSdXesMhkUOBE+fj+kvWNvmGsrR6HrNSiShM3oVdEjKnM7ALKAMEWaptLLZmvtUMAfZdJtqOYSRRSUtQ6+in9qcgZQ/dnqS1mjDdm6h9/Dd9VqziVIia3FVeKYuuX9+HNvZw2g5CxFFTWXybkl4GdsSYDau2GfXcmLTHMS0pIRVp2vsyiYvQzT02ww55pDK68liZuGP16YjAOHv4qkD1PF2nuGl+JOY4dp3Ke0G/7euLJyXCnwRRdTQJN7Ou5t11BjxZuPTs5jD1FiNIXiy; cid=undefined%7Cundefined; ak_bmsc_nke-2.2-ssn=0e7rQHmNgBmTAu2a2nroFTNeGADJAQ8rcKgC0NZyZDfKf9aCtII0hoUtqqBpvZXuZNvzzAHCMrzC4ydaEfHrCsEULsRQ7Sdos8HdRdHuvxPvV70Lzaaqv2xwfMqQcwx2itvLx4wRhcWrCkb99raU5z5I; ak_bmsc_nke-2.2=0e7rQHmNgBmTAu2a2nroFTNeGADJAQ8rcKgC0NZyZDfKf9aCtII0hoUtqqBpvZXuZNvzzAHCMrzC4ydaEfHrCsEULsRQ7Sdos8HdRdHuvxPvV70Lzaaqv2xwfMqQcwx2itvLx4wRhcWrCkb99raU5z5I; bm_sv=373C7E073F364AC8810F53384E4C6CCA~YAAQmiABF7B6ejmGAQAAXtanQRLOTc/EekpxYtf5PW0/PyobOFj6Ss9VPO1Lw+XX5Ab7/VafwCjwBNgmXQlW88zjp58eTFAGN3Leq4EpK/Ad1CWzOcqRX7F+wDAVJnZkzyIQ6PYmYpMcRNjn0YIDwvP7ZvYUhVUNyRpKeEZidfpd0trmWREyqQ8inKVyRjs9TB3Q3AczIExvD45WFD1tn3ZCpK/eJ+m7PuRsJPZSLVsxQuQmQJlyejXLwr4f1w==~1; _abck=B9EB50A491937ACB5F4029DA705679A2~-1~YAAQmJIuF3fpvy+GAQAAwg+oQQn6fJ8rv6JnffPxmvGVtr0vJLGg9bR65uxwLNqXx+DnQhCQnHPtxvM0P6PKllXDHs7x22/aW3Qbaj1lZ/Ai7CR9x8uivBA01hIvcXFpThtaQzXHBaAFkCCL0Dv+9VgwcdW9NEGISD+tOSXtjmbV8dzm2+tuU6+7hzhTj2FCy9wXb2y8zvILFq8x60+5fLjKt5JRRO0ovnzH7FB2+TQtPueQXBiKVjowRVgELLYAUd03o1uIVCp5ih/h5isJvnNfgfy5BwyVHQqQMk295nON6qYuMpkXZmp1be4KG53LQnnHPQjFbNW6rLHEgIDYX5aTs1ESFXwC6fnQEpSXvsj34MLRKeNMzwbThKHSiLfOV6LKD1HBV8dK7kJ2G6jUBvEpG6XVA42JzC/V5Cu0kBj0jHKIY5F0T0dMaNwUC64nghjXWHVKWy8RNya97h8FR+bYhZTw2OhI9vtRr40+7hgY0d+tETcLaB0ei73LNgjkjHs+aRNAy0bigmyrDxo6o+btdtWbUA==~-1~-1~-1; ppd=myorders|nikecom>myorders>order%20details',
    'dnt': '1',
    'nike-api-caller-id': 'com.nike:sse.orders',
    'origin': 'https://www.nike.com',
    'referer': 'https://www.nike.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Brave";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-nike-visitid': '4',
    'x-nike-visitorid': '1a653e67-29f6-47af-bab1-9dd9ac3224c5',
}

params = {
    'locale': 'en_us',
    'country': 'US',
    'language': 'en',
    'email': 'wizpig7@gmail.com',
    'timezone': 'America/New_York',
}

ordernumber = 'C01179605726'

nikeLink = 'https://api.nike.com/orders/summary/v1/'+ ordernumber
print(nikeLink)


def nikeInit():
    r = requests.Session()
    request = r.get(nikeLink, params=params, headers=headers)
    print(request.content)
    
    data = request.content

    parsed_data = json.loads(data)

    delivery_date = parsed_data['group'][0]['heading']
    size = parsed_data['group'][0]['orderItems'][0]['product']['size']
    styleColor = parsed_data['group'][0]['orderItems'][0]['product']['styleColor']
    productImage = parsed_data['group'][0]['orderItems'][0]['product']['productImage']
    productName = parsed_data['group'][0]['orderItems'][0]['product']['title']
    orderDate = parsed_data["fullOrderStatus"]["subStatus"]
    orderId = parsed_data["orderId"]
    trackLink = parsed_data['group'][0]['actions']['trackShipment']['webLink']

    print(size)
    print("Order Status:",delivery_date)
    print("Item Sku",styleColor)
    print(productImage)
    print("Item:",productName)
    print("Order Date:", orderDate)
    print("OrderID:",orderId)
    print("Tracking Link (If Shipped/Available):",trackLink)
    
    webhook = DiscordWebhook(url=webhookUrl, username="")
    embed = DiscordEmbed(
            title="Nike Order Info", description="", color='03b2f8'
         )
    embed.set_author(
            name="TaxEvader Nike Checker"
        )
    #embed.set_image(url='https://secure-images.nike.com/is/image/DotCom/DZ4864_100?$OMEGA_PRODUCT$')
    embed.add_embed_field(name="SKU:", value= styleColor, inline=False)
    embed.add_embed_field(name="Item Name:", value= productName, inline=False)
    embed.add_embed_field(name="Size:", value= size)
    embed.add_embed_field(name="Order Status:", value= delivery_date)
    embed.add_embed_field(name="Order Date:", value= orderDate)
    embed.add_embed_field(name="OrderID:", value= orderId)
    embed.add_embed_field(name="Tracking Link (If Available):", value= trackLink)
    embed.set_thumbnail(url=productImage)

    webhook.add_embed(embed)
    response = webhook.execute()
