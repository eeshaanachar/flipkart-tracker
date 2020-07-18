try:
    import requests
    import webbrowser
    from bs4 import BeautifulSoup

    discounted_items = list()
    with open("products.csv") as fh:
        for line in fh.readlines():
            url, wanted_price = line.split(',')
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            product = soup.find(class_="_35KyD6").text
            price = soup.find(class_="_1vC4OE _3qQ9m1").text.replace(',','')[1:]
            print(product + "\n₹" + price + "\n")
            if int(price) <= int(wanted_price):
                discounted_items.append(url)

    for url in discounted_items:
        webbrowser.open(url)
        
except Exception as message:
    input(message)
