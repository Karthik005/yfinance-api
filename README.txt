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

The API can be used after importing.
Stock/Equity information is be obtained as follows:

get_prices(['GOOG','MSFT','INFY.NS'])
get_volumes(['GOOG','MSFT','INFY.NS'])

Currency information is obtained as follows:

get_currency_price(['INR','JPY'])
get_currency_utc(['INR','JPY'])

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

