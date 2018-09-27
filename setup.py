from setuptools import setup, find_packages

setup(
    name='cyhy-core',
    version='0.0.2',
    author='Mark Feldhousen Jr.',
    author_email='mark.feldhousen@hq.dhs.gov',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=['bin/cyhy-ip','bin/cyhy-tool','bin/cyhy-export',
             'bin/cyhy-import','bin/cyhy-sched','bin/cyhy-snapshot',
             'bin/cyhy-mongo', 'bin/cyhy-simple', 'bin/cyhy-nvdsync',
             'bin/cyhy-control', 'bin/cyhy-ticket', 'bin/cyhy-archive',
             'bin/cyhy-suborg'],
    #url='http://pypi.python.org/pypi/cyhy/',
    license='LICENSE.txt',
    description='Core scanning libraries for Cyber Hygiene',
    long_description=open('README.md').read(),
    install_requires=[
        "pymongo >= 2.9.2, < 3",
        "python-dateutil >= 2.2",
        "netaddr >= 0.7.10",
        "progressbar >=2.3-dev",
        "geoip2 >= 2.3.0",
        "mongokit >= 0.9.0",
        "pycrypto >= 2.6",
        "docopt >= 0.6.2",
        "pandas >= 0.16.2",  # TODO: test with 0.19.1
        "six >= 1.9",
        "mock >= 2.0.0",
        "PyYAML >= 3.12",
        "ipython >= 5.4.0"
    ]
)
