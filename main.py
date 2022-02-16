import pandas as pd

def find_min_max_from_csv(name):
    #Read Csv initially
    file = pd.read_csv(r'TestCaseData.xlsx - KH Levent.csv')

    #Adding headers
    headerList = ['Dates', 'Numbers']

    #Convert file again after adding header
    file.to_csv(r'TestCaseData.xlsx - KH Levent.csv', header=headerList, index=False)

    # Read as datframe
    df = pd.read_csv(r'TestCaseData.xlsx - KH Levent.csv')

    #Perform Max and Min operation using pandas
    max = df['Numbers'].max()
    min = df['Numbers'].min()

    # Min and Max GroupBy Date Occurence
    date_of_max = df[df['Numbers'] == max]['Dates'].values[0]
    date_of_min = df[df['Numbers'] == min]['Dates'].values[0]

    #Finally Print Results
    print('Date :' + date_of_max, 'Max number: ' + str(max))
    print('Date :' + date_of_min, 'Min number: ' + str(min))


if __name__ == '__main__':
    find_min_max_from_csv('PyCharm')
