# Pompem - Exploit and Vulnerability Finder

Pompem is an open source tool, designed to automate the search for Exploits and Vulnerability in the most important databases.
Developed in Python, has a system of advanced search, that help the work of pentesters and ethical hackers.
In the current version, it performs searches in PacketStorm security, CXSecurity, ZeroDay, Vulners, National Vulnerability Database, WPScan Vulnerability Database ...

## Screenshots
![](http://i.imgur.com/lhBRLhl.png)

![](http://i.imgur.com/taqkdtT.png)

![](http://i.imgur.com/uNyqNF0.png)

## Source code

You can download the latest [tarball](https://github.com/rfunix/Pompem/archive/v0.2.0.tar.gz) by clicking here or latest [zipball](https://github.com/rfunix/Pompem/archive/v0.2.0.zip) by clicking here.

You can also download Pompem directly from its [Git repository](https://github.com/rfunix/Pompem):

```
$ git clone https://github.com/rfunix/Pompem.git
```

## Dependencies

Pompem works out of the box with [Python 3.5](https://www.python.org/downloads/) on any platform and requires the following packages:

- [Requests 2.9.1+](http://docs.python-requests.org/en/master/)

## Installation

Get Pompem up and running in a single command:

```
$ pip3.5 install -r requirements.txt
```

You may greatly benefit from using [virtualenv](https://virtualenv.pypa.io/en/stable/), which isolates packages installed for every project. If you have never used it, simply check [this tutorial] (http://docs.python-guide.org/en/latest/dev/virtualenvs) .

## Usage

To get the list of basic options and information about the project:

```bash
$ python3.5 pompem.py -h

Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt                           Write txt File
  --html                          Write html File
```

Examples of use:

    $ python3.5 pompem.py -s Wordpress
    $ python3.5 pompem.py -s Joomla --html
    $ python3.5 pompem.py -s "Internet Explorer,joomla,wordpress" --html
    $ python3.5 pompem.py -s FortiGate --txt
    $ python3.5 pompem.py -s ssh,ftp,mysql

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Pompem is free software, keeping the picture can USE AND ABUSE 
