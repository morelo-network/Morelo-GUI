<p align="center">
  <a href="https://github.com/MORELO-PROJECT/Morelo-GUI">
    <img src="https://github.com/MORELO-PROJECT/Morelo-GUI/blob/master/assets/bg.png" alt="Logo" align="center" width="100%">
  </a>
</p>




### Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contact](#contact)




### About The Project

Standard Morelo wallet application is console-based application, and this is reason why it's sometimes hard to operate on her. So I created this easy to use, user friendly and nice looking GUI wallet for Morelo.

Why:
* User friendly
* Easy to setup and use
* Nice looking

Of course that wallet doesn't giving you full control of Morelo wallet, but giving you enough features for basic usage. If you have any suggestions you can pull a request and i will review that.

### Built With
* [Python 3.7](https://www.python.org/downloads/)
* [PyQt 5](https://pypi.org/project/PyQt5/)
* [QrCode](https://pypi.org/project/qrcode/)


### Getting Started

1) Download latest Morelo-GUI release.
2) Download latest Morelo binaries.
3) Unpack both with any archive unpacker in same folder.
4) Run Morelo-GUI.
5) Follow steps in application to create or open existing wallet.

### Prerequisites

If you want run Morelo_GUI script by self or you using other OS than windows you need that things:

* [Python 3.7](https://www.python.org/downloads/)

Download, run installator and follow installation steps.

* [Latest Morelo binaries](https://github.com/MORELO-PROJECT/morelo/releases)

Download and unpack binaries (morelod, morelo-wallet-rpc) in same folder as script.

* PyQt 5
* QrCode
* Requests
* Psutil

Open your terminal and type commands above to install required packages:
```sh
python -m pip install PyQt5
python -m pip install qrcode[pil]
python -m pip install requests
python -m pip install psutil
```
If some another package is missed, script will tell you during execution.


### Usage

If you using windows just run 'Morelo-GUI.exe' from latest release
Then follow steps in application.

If you using another OS than windows you need run python script manually:
```sh
python Morelo-GUI.py
```


## Contact

Krzysztof Walędziak - E-mail: mrkris7100@gmail.com - [Discord](https://discordapp.com/): Mrkris7100#1836

Project Link: [https://github.com/MORELO-PROJECT/Morelo-GUI](https://github.com/MORELO-PROJECT/Morelo-GUI)
