'''
Created on 05-Mar-2015

'''
__author__= "Karthik Bharadwaj"
__copyright__ = "Copyright 2015, Karthik.S"
__maintainer__ = "Karthik Bharadwaj"
__email__= "karthikbharadwaj005@gmail.com"
__license__= "GNU v2.0"
__version__="1.0.0"
__status__="Production"

'''
Imports
'''

import json
import urllib2 as jsonfetch



'''
Commodity/Equity information fetcher functions
'''

'''
The tickers/symbols must be the same as those used on Yahoo! Finance 
Eg: Lenovo Group listed on the Hong Kong Stock Exchange would have a symbol of '0992.HK'
'''

def get_json(symbols):
    '''
    Return the corresponding json string fetched from the yahoo server for each
    symbol in symbols list
    ''' 
    url = 'http://finance.yahoo.com/webservice/v1/symbols/'
    url+="".join([",%20"+l if l != symbols[0] else l for l in symbols])+"/quote?format=json"
    json_str = jsonfetch.urlopen(url).read()
    content = json.loads(json_str)
    return content


def parse_json(content):
    '''
    Parse a content (yahoo finance json) string and return a dictionary containing 
    information about the stocks in content
    ''' 
    parsed_content = {}
    for item in content['list']['resources']:
        parsed_content[item['resource']['fields']['symbol']]=item['resource']['fields']
    return parsed_content


def get_dict(symbols):
    '''
    Return a dictionary containing (symbol,stock information) key-value pairs
    for each symbol in symbols
    '''
    return parse_json(get_json(symbols))


def get_resource(symbols, param):
    '''
    Return a dictionary with symbol-parameter specified resource as key-value
    pairs for each symbol in symbols list
    '''
    dicter = get_dict(symbols)
    diction = {}
    for symbol in dicter:
        diction[str(symbol)] = dicter[symbol][param]
    return diction


def get_prices(symbols):
    '''
    Return a dictionary with symbol-price as key-value pairs for each symbol in
    symbols list
    '''
    ret = get_resource(symbols,'price')
    for each in ret:
        ret[each] = float(ret[each])
    return ret


def get_names(symbols):
    '''
    Return a dictionary containing symbol-name as key-value pairs for each symbol in
    symbols list
    '''
    ret = get_resource(symbols,'name')
    for each in ret:
        ret[each] = str(ret[each])
    return ret


def get_volumes(symbols):
    '''
    Return a dictionary containing symbol-volume as key-value pairs for each symbol in
    symbols list
    '''
    ret = get_resource(symbols,'volume')
    for each in ret:
        ret[each] = int(ret[each])
    return ret

def get_utc(symbols):
    '''
    Return a dictionary containing symbol-utc time as key-value pairs for each symbol in
    symbols list
    '''
    ret = get_resource(symbols,'utctime')
    for each in ret:
        ret[each] = str(ret[each])
    return ret

'''
Currency information fetcher functions 
'''

'''
Accepted currency symbols:
'UYU', 'UZS', 'COP', 'VND', 'AZN', 'ISK', 'FKP', 'UAH', 'SLL', 'MZN', 'GEL',
'KZT', 'IDR', 'LAK', 'IRR', 'ETB', 'PAB', 'BZD', 'DEM', 'BAM', 'TWD', 'MGA',
'ARS', 'SRD', 'PHP', 'GIP', 'FRF', 'TRY', 'MYR', 'ECS', 'BSD', 'SBD', 'KES',
'AED', 'BWP', 'ZWL', 'VUV', 'MXV', 'SVC', 'MDL', 'TOP', 'GNF', 'BHD', 'TND',
'NAD', 'MUR', 'DZD', 'MOP', 'GMD', 'XPF', 'GBP', 'HTG', 'BIF', 'ITL', 'NOK',
'JPY', 'BBD', 'AMD', 'AWG', 'CRC', 'LKR', 'XDR', 'SHP', 'ALL', 'TJS', 'KPW',
'VEF', 'BGN', 'FJD', 'BRL', 'HRK', 'RWF', 'ILS', 'PKR', 'TMT', 'XAG', 'ZMW',
'RUB', 'KWD', 'MKD', 'DOP', 'LVL', 'TTD', 'TZS', 'SGD', 'LBP', 'HKD', 'CNY',
'DKK', 'USD', 'NIO', 'KYD', 'PEN', 'EUR', 'MMK', 'CYP', 'RON', 'IQD', 'NPR',
'KGS', 'ANG', 'CHF', 'CUP', 'KHR', 'XOF', 'JOD', 'XCP', 'MWK', 'SDG', 'CZK',
'ZAR', 'NZD', 'WST', 'YER', 'CNH', 'PLN', 'XPT', 'RSD', 'AOA', 'NGN', 'LYD',
'INR', 'SCR', 'SIT', 'BDT', 'ERN', 'SZL', 'HUF', 'GYD', 'MNT', 'QAR', 'XAU',
'XPD', 'SOS', 'KRW', 'UGX', 'SEK', 'CVE', 'PYG', 'CAD', 'XCD', 'KMF', 'CDF',
'CLF', 'LRD', 'MXN', 'IEP', 'PGK', 'MVR', 'STD', 'LSL', 'GHS', 'BND', 'HNL',
'SAR', 'SYP', 'OMR', 'DJF', 'AUD', 'BTN', 'XAF', 'LTL', 'AFN', 'THB', 'BMD',
'BYR', 'EGP', 'MRO', 'GTQ', 'CLP', 'BOB', 'MAD', 'JMD'

All returned values are in USD
'''

def get_currency_json(currencies):
    '''
    Return the corresponding json string fetched from the yahoo server for each
    currency in currencies list
    ''' 
    symbols = [t+'=X' for t in currencies]
    content = get_json(symbols)
    return content


def parse_currency_json(content):
    '''
    Parse a content (yahoo finance json) string and return a dictionary containing 
    information about the currencies in content
    ''' 
    parsed_content = parse_json(content)
    parsed_currency_content={}
    for currency in parsed_content:
        parsed_currency_content[currency.split('=')[0]] = parsed_content[currency]
    return parsed_currency_content


def get_currency_dict(currencies):
    '''
    Return a dictionary containing currency-currency information as key-value pairs
    for each currency in currencies
    '''
    return parse_currency_json(get_currency_json(currencies))


def get_currency_resource(currencies, param):
    '''
    Return a dictionary with currency-parameter specified resource as key-value
    pairs for each currency in currencies
    '''
    dicter = get_currency_dict(currencies)
    diction = {}
    for symbol in dicter:
        diction[str(symbol)] = dicter[symbol][param]
    return diction

def get_currency_prices(currencies):
    '''
    Return a dictionary with currency-price as key-value pairs for each currency in
    currencies list
    '''
    ret = get_currency_resource(currencies,'price')
    for each in ret:
        ret[each] = float(ret[each])
    return ret


def get_currency_names(currencies):
    '''
    Return a dictionary containing currency-name as key-value pairs for each currency in
    currencies list
    '''
    ret = get_currency_resource(currencies,'name')
    for each in ret:
        ret[each] = str(ret[each])
    return ret


def get_currency_volumes(currencies):
    '''
    Return a dictionary containing currency-volume as key-value pairs for each currency in
    currencies list
    '''
    ret = get_resource(currencies,'volume')
    for each in ret:
        ret[each] = int(ret[each])
    return ret

def get_currency_utc(currencies):
    '''
    Return a dictionary containing currency-utc time as key-value pairs for each currency in
    currencies list
    '''
    ret = get_resource(currencies,'utctime')
    for each in ret:
        ret[each] = str(ret[each])
    return ret

    
