pkgname = "hunspell-ru"
pkgver = "2013.11.01"
pkgrel = 0
pkgdesc = "English language dictionaries for hunspell"
license = "MIT"
url = "https://bitbucket.org/Shaman_Alex"
source = [
    f"{url}/russian-dictionary-hunspell/downloads/ru_RU_UTF-8_20131101.zip"
]
sha256 = [
    "616348ad645a716d91c8a6645065e710f15e9dda3ffef60cdf7ec8a4e27975af",
]


def install(self):
    self.install_license("README_ru_RU.txt")

    self.install_file("./ru_*.dic", "usr/share/hunspell", glob=True)
    self.install_file("./ru_*.aff", "usr/share/hunspell", glob=True)
