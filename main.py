from tori_parser import parseUrl


if __name__ == "__main__":

    lista = parseUrl(
        "https://www.tori.fi/pirkanmaa?q=&cg=3020&w=1&st=s&c=3023&ps=&pe=&ca=11&l=0&md=th"
    )
    for im in lista:
        print(im)
