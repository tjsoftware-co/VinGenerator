from distutils.core import setup


files = ["VinPrefixes.txt"]

setup(
    name="vin",
    version="0.5",
    packages = ["vin"],
    package_data = {"vin" : files}
)