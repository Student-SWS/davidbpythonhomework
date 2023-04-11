def get_price(symbol):
    import requests

    apikey = 'alphavantage'

    url = ( 'https://www.alphavantage.co/query?'
            'function=TIME_SERIES_INTRADAY'
           f'&symbol={symbol}&interval=1min&apikey={apikey}'
            '&datatype=csv')

    response = requests.get(url)
    text = response.text

    try:
        quote = text.splitlines()[1].split(',')[4]
    except IndexError:
        if 'demo purposes' in text:
            exit('\n*** NOTE ***  This demo URL can only be '
                 'used with MSFT.  To obtain live data on '
                 'other symbols, you must edit your program '
                 'to change "apikey = " variable in this '
                 'function to a user key you can obtain from '
                 'the "alphavantage" service by signing up for '
                 'a free account.  See error message below: '
                 ' \n\n' + text)

        exit('error parsing response.  Response:  ' + text)

    return quote

aa = input('please input the stock symbol you would '
               'like to buy:  ') #string, MSFT

bb = input('please input the cash you have to invest:  ') #string, 50000

cc = get_price(aa)      # returns a string price

amount_can_buy = float(bb)//float(cc) ##float, 183

print('with $' + bb + ' you can buy ' + str(int(amount_can_buy)) + ' shares of ' + aa + ' at $' + str(round(float(cc), 2)) + '/share')