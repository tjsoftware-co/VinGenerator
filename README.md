## Description: 
A basic script to generate check summed valid VINs to be used when testing flooring vehicles

## Requirements:
1. num.py must be viewable via a mobile browser. (tested against the iphone simulator)
2. Generated VIN must have appropriate Make and Model prefix codes for automatic field population where available

## Usage: 
The designed usage was for viewing via a mobile web browser, and facilitating copy-paste into form fields for ease of 
testing. Point your browser to localhost/num.py

Or, one can run the following at the command line (from this directory) to generate a random vin:

`python -c "import vin; print vin.get_random_vin()"`


TODO:
Allow users to select specific makes and models prior to generating any random vin
