# ZilliqaVanity
Generate Vanity Addresses for the Zilliqa Network
https://www.github.com/frog357/zilliqa-vanity/

This is work based on Vanity-Cosmos found here:
https://github.com/etimoz/vanity-cosmos


Please review the license before use, there is no warranty implied. The code is simple to audit and understand. You do not need to be connected to the internet to generate a vanity address. This code is not optimized, it is just working. I desired to have a Vanity Zilliqa address and I set out to accomplish it. Turns out, this had not yet existed for Zilliqa. Try as I might, I could not make any of the existing solutions work for Zilliqa. I had to make my own.


I plan to make some cool stuff for the Zilliqa Community, I'm just getting started.
Visit my website to learn more.
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
sudo pip install -U pyzil
or
sudo pip3 install -U pyzil


## Usage
Look for an address that starts with "00000" (e.g. zil100000v3fpv4qg2a9ea6sj70gykxpt63wgjen2p)
```
python -m zilliqavanity --startswith 00000
```

Look for an address that ends with "8888" (e.g. zil134dck5uddzjure8pyprmmqat96k3jlypn28888)
```
python -m zilliqavanity --endswith 8888
```

Look for an address containing the substring "mystring" (e.g. zil1z39wmystringah22s5a3pyswtnjkx2w0hvn3rv)
```
python -m zilliqavanity --contains mystring
```


You might have to substitue python for python3 if you have multiple versions installed.


An example of a vanity address I created for myself using this tool:

zil1fredmczkfemd2wvc9z75azclf9hwysewzyxjaf

zil1fred :)P

contact me at zilliqafred@gmail.com
