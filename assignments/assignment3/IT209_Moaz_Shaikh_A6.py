# FCPD Crime Weekly Database Program
# The purpose of this assignment is to create a custom class called FCPDCrime and import a CSV file and
# sort through the data using the various methods after loading the file in
# Moaz Shaikh 11/18/2025

class FCPDCrime(list):

    def __init__(self, name='Fairfax County Police Crime Report'):
        self.name = name
        super().__init__()


    def load(self, file='CrimeReports_A6.csv'):
        f = open(file)
        x = f.readlines()
        f.close()
        for line in x:
            if len(line) > 3: #checks for blank or extraneous lines
                splitline = line.split(',')
                for n in range(len(splitline)):
                    splitline[n] = splitline[n].strip()
                self.append(splitline)
        return len(self)



    def zipCodeList(self, zip='22030'):
        """Return a list of all incident report lines for a selected Fairfax County ZipCode.
           Input: 5 digit Zip Code in string format, default is "22030"
           Output: No display output is produced.
           Return: List of all report lines for the selected Zip Code. """
        zip = zip.strip().lower()
        return [call for call in self if zip in str(call[8]).lower()]



    def countByZip(self):
        """Displays a report of the number of crimes reported by Zip Code in sorted format from
              highest to lowest.
           Output: displays one line per county zip code with the count and % of total crimes
           Return: No return value   """
        zip_counts = {}
        # Making the frequency dictionary
        for call in self:
            call_zip = str(call[8]).lower()
            if call_zip in zip_counts:
                zip_counts[call_zip] += 1
            else:
                zip_counts[call_zip] = 1
        # To sort by frequency we have to return the index of 1 of the items (done by get_count) in the tuples generated
        # by the sorted function next
        def get_count(item):
            return item[1]
        sorted_zips = sorted(zip_counts.items(), key = get_count, reverse = True)
        # Calculate total number of crimes for calculating percentages
        total = sum(zip_counts.values())
        # Displaying the results
        print(f"{'Zip Code':<15}{'Count':<10}{'Percent':<10}")
        print("-" * 32)
        for zip_code, count in sorted_zips:
            percent = round(((count/total) * 100), 2)
            print(f"{zip_code:<15}{count:<10}{percent:<3}%")


    def countByCrime(self, select='all'):
        select = select.strip().lower()
        crime_counts = {}

        # Making the frequency dictionary
        for call in self:
            call_zip = str(call[8]).lower()
            call_type = str(call[2]).lower()

            if select == 'all' or select in call_zip:
                if call_type in crime_counts:
                    crime_counts[call_type] += 1
                else:
                    crime_counts[call_type] = 1

        # To sort by frequency we have to return the index of 1 of the items (done by get_count) in the tuples generated
        # by the sorted function next
        def get_count(item):
            return item[1]

        sorted_crimes = sorted(crime_counts.items(), key = get_count, reverse = True)

        # Displaying the results
        print(f"{'Crime Type':<100} {'Count':<30}")
        print('-' * 121)
        for crime, count in sorted_crimes:
            print(f"{crime:<100} Frequency Count: {count:<10}")



    def printCrimes(self, searchKey='all', zip='all', locale='all'):
        # Lab 9:  Provide code for this method
        #     The only options required for the Lab are:
        #     (1) print all records,
        #     (2) print all for a selected type (e.g., searchKey = "assault")
        #     (3) print all records for a selected zip code
        #     (4) print all records for a selected type in a selected zip code
        #            (e.g., print "assault"s in zip code "22030"
        #     Hint: when matching use the "in" operator rather than "==" since it gives
        #       more flexibility in the matching process
        """Display a formatted report of selected lines in the downloaded report - the
                 method selects based on the parameter values. Parameters and file attributes
                 are converted to lower case when matching since data is upper case and
                 parameters could be either.
        Input:  searchKey - default = 'all', or a text string that appears in the longer
                            call text (e.g. "assault"), index [2] of the call line
                zip       - default = 'all', or a 5 digit Zip Code in string format, line index [8]
                locale    - default = 'all', or a county locale (e.g. "fairfax") that appears
                            in index [6] of the line
        Output: Crime reports, one line per incident
                    Prints all lines if all parameters are 'all'
                    Prints selected lines based on matching conditions for the parameters
                        Example: searchKey = 'assault' prints all calls for assaults
                                 zip = '22030' prints all calls for zip code 22030
                                 locale = 'Fairfax' prints all calls for locale 'Fairfax'
                                 searchKey = 'assault' and zip = '22030' prints assaults for 22030
                                 searchKey = 'bite' and locale = 'Fairfax' prints all animal bites
                                     reported in Fairfax
        Returns: Nothing is returned.
        """
        counter = 0
        for call in self:
            if (str(searchKey).lower() in str(call[2]).lower() or str(searchKey).lower() == 'all') and (str(zip).lower() == 'all' or str(zip).lower() in str(call[8])) and (str(locale).lower() == 'all' or str(locale).lower() in str(call[6]).lower()):
                counter += 1
                print(f'{f'Call {counter}: ':<12}' + f'Call Type Code: {call[0]}' + '     ' + f'{f'Crime Code: {call[1]}':<25}' + '     ' + f'{f'Description: {call[2]}':<95}' +
                      '     ' + f'Week/Date Range: {call[3]}' + '     ' + f'Report Flag: {call[4]}' + '     ' + f'{f'Street Address: {call[5]}':<85}' +
                      '     ' + f'{f'Location: {call[6]}':<40}' + '     ' + f'{f'State: {call[7]}':<30}' + '     ' + f'Zip Code: {call[8]}')
        print('\n', counter, 'calls recorded for this area \n')


# ------------- TEST CODE --------------
# FC = FCPDCrime(name='IT 209 A7')
# FC.load(file='CrimeReports_A6.csv')
# FC.printCrimes()
# FC.printCrimes()
# ZL = FC.zipCodeList(zip='22102')
# for c in ZL:
#    print(c)
# FC.countByZip()
# FC.countByCrime(select='22102')




