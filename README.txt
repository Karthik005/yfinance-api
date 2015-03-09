				yfinanceapi (Finance API)

Description
-----------

The yfinanceapi is an API for Python that builds on top of the Yahoo finance JSON API to provide equity and commodity information, such as price, volume traded and last trade time etc.

Installation
------------

The API can be installed from PyPi using the following command:
pip install yfinanceapi
Instructions on installing pip can be found here: https://pip.pypa.io/en/latest/installing.html

Usage
-----

The API can be used after importing in the following manner:

import yfinanceapi.api as api

Stock/Equity information is be obtained as follows:

api.get_prices(['GOOG','MSFT','INFY.NS'])
api.get_volumes(['GOOG','MSFT','INFY.NS'])

Prices are in currency values of the country in which symbol is listed

Currency information is obtained as follows:

api.get_currency_price(['INR','JPY'])
api.get_currency_utc(['INR','JPY'])

All prices are in USD for currencies

More functions, information on usage and allowed symbol values can be found in the docstrings of the yfinanceapi.py file


Copyright
---------

Copyright 2015, Karthik.S


License
-------

This project is licensed under GNU v2.0. For more information read the License.txt file


Bugs and requests
----------------

Bugs and feature requests can be reported at karthikbharadwaj005@gmail.com

