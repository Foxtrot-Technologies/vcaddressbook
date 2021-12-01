# VC Ricoh AddressBook Sync

A simple tool to update the address books on Ricoh multi-function printers to match up with the InTrays folder in Virtual Cabinet
This is to enable Scan-to Virtual Cabinet, but could be used for any similar "scan to a set of folders named after people" functionality.

Configuration can be found at the top of the script.  Simply provide:
* IP addresses of the printers
* Login credentials for the printer web admin interface
* The name of the share as seen by the printers
* The local path to the share

While only tested on a Ricoh IM C3500, it likely supports any Ricoh printer supported by the WTFox printers library referenced below.


# Dependencies

1. Download and install python 64bit: 
https://www.python.org/downloads/release/python-3100/
a.	Choose Customise installation. 
b.	Choose "Add Python to Path"
c.	Choose "Install for all users"

2.	Install Python Ricoh Library (in Administrator command prompt):
https://github.com/WTFox/printers
a.	pip install requests
b.	python setup.py install

# Disclaimer

No warranty is provided with this code, use at your own risk.
