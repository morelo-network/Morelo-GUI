<br />
<p align="center">
  <a href="https://gitlab.com/galaxia-project/app/pywallet">
    <img src="assets/logo_green.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Xi-GUIWallet</h3>

  <p align="center">
    Easy to use and user friendly Galaxia GUI wallet!
    <br />
    <br />
    <a href="https://gitlab.com/galaxia-project/app/pywallet/issues">Report Bug</a>
    ·
    <a href="https://gitlab.com/galaxia-project/app/pywallet/issues">Request Feature</a>
  </p>
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

Standard Galaxia wallet application is console-based application, and this is reason why it's sometimes hard to operate on her. So I created this easy to use, user friendly and nice looking GUI wallet for Galaxia.

Why:
* User friendly
* Easy to setup and use
* Nice looking

Of course that wallet doesn't giving you full control of Galaxia wallet, but giving you enough features for basic usage. If you have any suggestions you can pull a request and i will review that.

### Built With
* [Python 3.7](https://www.python.org/downloads/)
* [PyQt 5](https://pypi.org/project/PyQt5/)
* [QrCode](https://pypi.org/project/qrcode/)


### Getting Started

1) Download latest GUI wallet release.
2) Download latest Galaxia binaries.
3) Unpack both with any archive unpacker in same folder.
4) Run Xi-GUIWallet.
5) Follow steps in application to create or open existing wallet.

### Prerequisites

If you want run GUI wallet script by self or you using other OS than windows you need that things:

* [Python 3.7](https://www.python.org/downloads/)

Download, run installator and follow installation steps.

* [Latest Galaxia binaries](https://releases.galaxia-project.com/stable/latest/)
Download and unpack binaries (xi-daemon, xi-pgservice) in same folder as script.

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

If you using windows just run 'Xi-GUIWallet' from latest release or run python script using command:
```sh
python Xi-GUIWallet.py
```
Then follow steps in application.

If you using another OS than windows you need run python script manually.


## Contact

Krzysztof Walędziak - mrkris7100@gmail.com

Project Link: [https://gitlab.com/galaxia-project/app/pywallet](https://gitlab.com/galaxia-project/app/pywallet)
