import requests

working = 0

while working == 0:
    try:
        website = input("URL: ")
        html_output_name = 'page.html'
        req = requests.get(website, 'html.parser', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/101.0.4951.67 Safari/537.36'})

        with open(html_output_name, 'w') as f:
            f.write(req.text)
            working = 1
            f.close()

    except requests.exceptions.MissingSchema as e:
        print("Make sure you enter the full url (ex: https://www.google.com/")
        print("Usages like 'www.google.com' will not work.")
