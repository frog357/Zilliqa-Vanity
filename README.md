# ZilliqaVanity
Generate Vanity Addresses for Zilliqa Using Python
https://www.github.com/frog357/zilliqa-vanity/

This is work based on Vanity-Cosmos found here:
https://github.com/etimoz/vanity-cosmos


Please review the license before use, there is no warranty implied. The code is simple to audit and understand. You do not need to be connected to the internet to generate a vanity address. This code is not optimized, it is just working. I desired to have a Vanity Zilliqa address and I set out to accomplish it. Turns out, this had not yet existed for Zilliqa. Try as I might, I could not make any of the existing solutions work for Zilliqa. I had to make my own.


Visit my website for more Zilliqa related tools and information.
https://zilf.red


## Features
* Generate Zilliqa bech32 vanity addresses
* Specify a substring that the addresses must
    * start with
    * end with
    * contains
* Set minimum amount of letters (a-z) or digits (0-9) required in an address
* Set the number of addresses to generate
* Uses all CPU cores


## Before You Begin
Install Pre-Reqs:
sudo pip3 install -U setuptools eth-hash
sudo pip3 install -U setuptools pyzil
or
sudo pip install -U setuptools eth-hash
sudo pip install -U setuptools pyzil


If you don't have python3 or pip3, you can try:
sudo apt install python3-pip


## Usage
Look for an address that starts with "00000" (e.g. zil100000v3fpv4qg2a9ea6sj70gykxpt63wgjen2p)
```
python3 -m zilliqavanity --startswith 00000
```

Look for an address that ends with "8888" (e.g. zil134dck5uddzjure8pyprmmqat96k3jlypn28888)
```
python3 -m zilliqavanity --endswith 8888
```

Look for an address containing the substring "mystring" (e.g. zil1z39wmystringah22s5a3pyswtnjkx2w0hvn3rv)
```
python3 -m zilliqavanity --contains mystring
```
You might have to substitute python3 for python.



An example of a vanity address I created for myself using this tool:

zil1fredmczkfemd2wvc9z75azclf9hwysewzyxjaf

zil1fred :)P

contact me at zilliqafred@gmail.com
