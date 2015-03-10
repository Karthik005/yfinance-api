				yfinanceapi (Equity and currency information API)

Description
-----------

The yfinanceapi is an API for Python that builds on top of the Yahoo! finance JSON API to provide equity and currency information, such as price, volume, last trade time etc.

Installation
------------

The API can be installed from PyPi using the following command:
pip install yfinanceapi
Instructions on installing pip can be found here: https://pip.pypa.io/en/latest/installing.html

Alternatively, it can be installed using github:
pip install git+https://github.com/Karthik005/yfinanceapi#egg=yfinanceapi

The installation may require root permissions.

Usage
-----

The API can be used after importing in the following manner:

import yfinanceapi.api as api

Stock/equity information is obtained as follows:

api.get_prices(['GOOG','MSFT','INFY.NS'])
api.get_volumes(['GOOG','MSFT','INFY.NS'])

Prices are in currency values of the country in which symbol is listed

Currency information is obtained as follows:

api.get_currency_prices(['INR','JPY'])
api.get_currency_utc(['INR','JPY'])

Currency values are measured with respect to USD.

Additional functions, information on usage and allowed symbol values can be found in the docstrings of the api.py file.


Copyright
---------

Copyright 2015, Karthik.S


License
-------

This project is licensed under GNU v2.0. For more information read the LICENSE.txt file.


Bugs and requests
----------------

Bugs and feature requests can be reported at karthikbharadwaj005@gmail.com

