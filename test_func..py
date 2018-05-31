def get_vat(price, vat_rate):
    vat = ((price/(1+(vat_rate/100)))-price)*(-1)
    price_no_vat = round((price-vat),2)
    print('Сумма без НДС: '+ str(price_no_vat))

print('Узнай сумму, за вычетом НДС')
price1=input('Сумма: ')
vat_rate1=input('НДС: ')
get_vat(float(price1), float(vat_rate1))

