# Ispy scanner

![Version](https://img.shields.io/badge/version-1.0.0-green.svg) ![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

This tool helps automate your bug bounty workflow by running common baseline tools for you automatically, and results can be reported over a discord webhook as well to allow you and members of a read team to instantly share intel as you get it, to a channel of your choosing. The per model choice was made to help with character limits of discord, but also to immediately share relevent information as soon as possible. For example you may need to know as fast as possible what the DNS looks like, so NMA will run and report over the webhook. Nuclei will run after NMAP, but while the Nuclei scan runs (which can take some time), your team already has the DNS information required.

## Installation

```bash
git clone https://github.com/destiny-creates/Ispy.git && cd Ispy && python3 -m venv ispy-env && source ispy-env/bin/activate && pip3 install -r requirements.txt
```

## Usage

python3 main.py

## Features

- NMAP
- Nuclei
- Webhook reporting (discord)
- Tor routing VIA proxychains

## Contributing

You must fork the repository, and work on your own, and then you may submit a pull request. If rejected, you must wait at least 3 days before resubmitting, to give you a chance to look over the code.

## Author

Nulled_Ash
