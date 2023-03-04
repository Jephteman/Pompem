

def shodan(html):
    names = []
    urls = []
    for i in html.split(sep='\n'):
        if '<div class="result"><a href="' in i:
            
            url = i.split(sep='<div class="result"><a href="')[1].split(sep='"')[0]
            urls.append(url)
            name = i.split(sep='class="bold">')[1]
            names.append(name)
    return (names, urls)


