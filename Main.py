from bs4 import BeautifulSoup
import requests
import lxml

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "91.0.4472.124 Safari/537.36"

}

# product URLs and Names  dictionary
products = [

    {
        "FLIPKART_URL": "https://www.flipkart.com/gopro-hero8-black-sports-action-camera/p/itmc22957c908f01?pid=SAYFKYD4UE2GYZJR&lid=LSTSAYFKYD4UE2GYZJR5T628Y&marketplace=FLIPKART&q=gopro+camera&store=jek%2Fp31%2Fs3q&spotlightTagId=BestvalueId_jek%2Fp31%2Fs3q&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=18df5d21-dee4-42b4-bed5-1db6af32ed6b.SAYFKYD4UE2GYZJR.SEARCH&ppt=sp&ppn=sp&ssid=ugfq3b7mf40000001625548865782&qH=be2b8cb84c3036ac",
        "name": "Gopro hero 8 Black",
        "target_price": 28000
    },

    {
        "FLIPKART_URL": "https://www.flipkart.com/sony-chu-2208bb01i-1000-gb-spider-man-ratchet-clank-gran-turismo/p/itm8230ffd9a827b?pid=GMCFUAKAMHX6QJ2C&lid=LSTGMCFUAKAMHX6QJ2C1HTDLX&marketplace=FLIPKART&store=4rr%2Fx1m%2Fwym&srno=b_1_19&otracker=sp_browse_announcement_4rr%2Cx1m%2Cwym&fm=organic&iid=62e2e8bc-40f8-4b0d-96e1-4e3d24d35c30.GMCFUAKAMHX6QJ2C.SEARCH&ppt=None&ppn=None&ssid=zwf05ypn400000001625547950359",
        "name": "PS4 pro 1TB",
        "target_price": 30000

    },
    {
        "FLIPKART_URL": "https://www.flipkart.com/microsoft-xbox-one-s-1-tb-star-wars-jedi-fallen-order/p/itma750e2d30cf0f?pid=GMCFZ23MQNWGHYG6&lid=LSTGMCFZ23MQNWGHYG6YPIUQX&marketplace=FLIPKART&q=xbox+one+s&store=4rr%2Fx1m%2Fnn6&spotlightTagId=BestvalueId_4rr%2Fx1m%2Fnn6&srno=s_1_8&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_ps&fm=SEARCH&iid=ea8a755d-8710-486f-a5d7-660ff4e76d7d.GMCFZ23MQNWGHYG6.SEARCH&ppt=sp&ppn=sp&ssid=c1m1xcagqo0000001625491104180&qH=cc078572da53c819",
        "name": "xbox-one-s 1TB",
        "target_price": 28000
    },

    {
        "FLIPKART_URL": "https://www.flipkart.com/samsung-galaxy-m42-prism-dot-black-128-gb/p/itmb137b3296810c?pid=MOBG3KGVVVVZ6YHF&lid=LSTMOBG3KGVVVVZ6YHFPHRKJS&marketplace=FLIPKART&q=samsung+mobiles&store=tyy%2F4io&srno=s_1_7&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=SEARCH&iid=52a9684c-2c3a-418c-8e50-fbbc78ebb63a.MOBG3KGVVVVZ6YHF.SEARCH&ppt=sp&ppn=sp&ssid=ul4cgwnauo0000001625491353404&qH=0258c7d48242959a",
        "name": "samsung-galaxy-m42",
        "target_price": 27000

    },
    {
        "FLIPKART_URL": "https://www.flipkart.com/apple-watch-se-gps-cellular-44-mm-space-grey-aluminium-case-black-sport-band/p/itm870f9d947c04c?pid=SMWFVNKGUDQMGTXA&lid=LSTSMWFVNKGUDQMGTXAUHG45T&marketplace=FLIPKART&q=APPLE+Watch+&store=ajy%2Fbuh&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=7bb025b3-c85f-47bc-b602-9ca54e18f98e.SMWFVNKGUDQMGTXA.SEARCH&ppt=pp&ppn=pp&ssid=9pbh98ohio0000001625547579604&qH=0d98f784fcb111f3",
        "name": "apple_watch",
        "target_price": 28000

    },

]


# Let’s define the function that will check the price of the product
def give_the_price(FLIPKART_URL):
    response_1 = requests.get(FLIPKART_URL, headers=Headers)
    website_1 = response_1
    soup = BeautifulSoup(website_1.content, 'lxml')
    # class_="_30jeq3 _16Jk6d"  # below sentence used to convert the price from string format to a ‘float’.
    title = soup.find(class_="_30jeq3 _16Jk6d").get_text()[1:].strip().replace(',', '')
    p_price = float(title)
    return p_price


# print the price of the every_product
for every_product in products:
    product_price = give_the_price(every_product.get("FLIPKART_URL"))
    print(f"product= {every_product.get('name')}\nprice= Rs.{product_price}")

    # checking the Available at our required price
    if product_price <= every_product.get("target_price"):
        print("Available at Our required price\n")

        # This adds the product_price to the file.
        with open("product_price.txt", 'a') as file:  # If you don't care about closing the file, this one-liner works:
            file.write(
             f"Available at Our required price \nproduct= {every_product.get('name')}\nprice= Rs.{product_price}\n\n")


    else:
        print("Still at current price\n ")
        
        
        
        
        
        
        
        
        
