from parser import parseUrl

if __name__ == "__main__":
    lista = parseUrl('https://www.tori.fi/pirkanmaa?q=&cg=3020&w=1&st=s&st=k&st=u&st=h&st=g&c=3023&ps=&pe=&ca=11&l=0&md=th')
    print(len(lista))