try:
    import requests
    import webbrowser
    from bs4 import BeautifulSoup

    fh = open("./flipkart_links_and_price.csv")
    dictionary = dict()
    for line in fh.readlines():
        if line != '\n':
            url, wanted_price = line.split(',')
            dictionary[url] = int(wanted_price)
    fh.close()

    discounted_items = list()
    for url, wanted_price in dictionary.items():
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        product = soup.find(class_="_35KyD6").text
        price = soup.find(class_="_1vC4OE _3qQ9m1").text.replace(',','')[1:]
        print(product + "\n₹" + price + "\n")
        if int(price) <= wanted_price:
            discounted_items.append(url)

    for url in discounted_items:
        webbrowser.open(url)

    input("Done")
        
except:
    input("Some error occurred!")
