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
        'License :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: Production',
        'Environment :: Console',
        'Intended Audience :: Finance',
        'Topic :: Finance'
    ],
    install_requires = [
        'json',
        'urllib2',
    ]
)
