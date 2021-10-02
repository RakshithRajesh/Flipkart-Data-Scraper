from requests_html import HTMLSession
import pandas as pd

search_term = "Drone"
s = HTMLSession()
r = s.get(
    f"https://www.flipkart.com/search?q={search_term}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
)

## PRODUCT NAME ##
product_name_list = []
product_name = r.html.find('div[class="_4rR01T"]')
for x in product_name:
    product_name_list.append(x.text)

## PRODUCT PRICE ##
product_price_list = []
product_price = r.html.find('div[class="_30jeq3 _1_WHN1"]')
for x in product_price:
    product_price_list.append(float(x.text.replace("₹", "").replace(",", "")))

## DISCOUNT ##
discount_list = []
discounts = r.html.find('div[class="_3Ay6Sb"]')
for x in discounts:
    discount_list.append(int(x.text.replace("% off", "")))

## STAR RATINGS ##
ratings_list = []
ratings = r.html.find('div[class="_3LWZlK"]')
for x in ratings:
    ratings_list.append(float(x.text))

## REVIEWS ##
ratings_count = []
reviews_count = []
reviews = r.html.find('span[class="_2_R_DZ"]')
for x in reviews:
    ratings_count.append(x.text.replace("\xa0", "").split("&")[0])
    reviews_count.append(x.text.replace("\xa0", "").split("&")[1])

## SPECS ##
specs_list = []
specs = r.html.find('ul[class="_1xgFaf"]')
for x in specs:
    specs_list.append(x.text.replace("\n", "; "))

try:
    df = pd.DataFrame(
        {
            "Name": product_name_list,
            "Price": product_price_list,
            "Specs List": specs_list,
        }
    )
    df.to_csv("Demo.csv")
    print("Done")
except:
    print(len(product_name_list))
    print(len(product_price_list))
    print(len(discount_list))
    print(len(ratings_list))
    print(len(ratings_count))
    print(len(reviews_count))
    print(len(specs_list))
