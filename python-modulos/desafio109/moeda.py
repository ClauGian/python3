def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)

def dobro(preço=0, formato=False):
    res =  preço * 2
    return res if not formato else moeda(res)

def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa) / 100
    return res if not formato else moeda(res)

def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa) / 100
    return res if not formato else moeda(res)

def moeda(preço=0, cifrão='R$'):
    return f'{cifrão}{preço:>8.2f}'.replace('.', ',')

