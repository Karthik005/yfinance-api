from setuptools import setup
 
setup(
    name = 'yfinanceapi',
    packages = ['yfinanceapi'],
    version = '1.0.0',
    description = 'Equity/commodity/currency information API',
    author='Karthik Bharadwaj',
    author_email='karthikbharadwaj005@gmail.com',
    url='https://github.com/Karthik005/yfinanceapi',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Topic :: Office/Business :: Financial',
    ],
    install_requires = [
        'json',
        'urllib2',
    ]
)
