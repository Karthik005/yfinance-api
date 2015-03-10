from setuptools import setup
 
setup(
    name = 'yfinanceapi',
    version = '1.0.1',
    py_modules=['yfinanceapi'],
    description = 'Equity/commodity/currency information API; sources content from Yahoo! Finance',
    author='Karthik Bharadwaj',
    requires=['urllib2','json'],
    author_email='karthikbharadwaj005@gmail.com',
    url='https://github.com/Karthik005/yfinanceapi',
    license='GNU v2.0',
    classifiers=[
    	'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: Unix',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Topic :: Office/Business :: Financial',
    ]
)
