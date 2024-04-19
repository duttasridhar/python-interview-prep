#! /usr/bin/env python3

import requests


def main():
    version = requests.get(
        'https://www.howsmyssl.com/a/check').json()['tls_version']
    print(version)


if __name__ == "__main__":
    main()
