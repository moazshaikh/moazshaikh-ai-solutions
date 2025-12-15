# University Department Class Definition 

## Objective
In this assignment we are to create a custom class called “FCPDCrime” that extends the ‘list’ class and adds five
new custom methods. The class will read in a file of csv data that you download from the Fairfax County
Police site of crimes reported by zip code for a given week.
The purpose of this assignment is to create a custom class called FCPDCrime and import a CSV file and sort through the data using the various methods after loading the file in

## Methods
- load() = to load file in
- zipCodeList = Return a list of all incident report lines for a selected Fairfax County ZipCode. Input: 5 digit Zip Code in string format, default is "22030" Output: No display output is produced. Return: List of all report lines for the selected Zip Code.
- countByZip() = Displays a report of the number of crimes reported by Zip Code in sorted format from highest to lowest. Output: displays one line per county zip code with the count and % of total crimes. Return: No return value
- countByCrime() = print frequency of crime based on crime value
- printCrimes() = print the crimes in the database based on some combination of searchkey, sip, and locale


