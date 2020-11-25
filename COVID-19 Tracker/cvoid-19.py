# import requests to get html of a website
import requests
# import bs4 to parse html
from bs4 import BeautifulSoup

#request html of a website 
def get_html(url):
    r = requests.get(url)
    return r.text

def get_global(html):
    glob = []
    soup = BeautifulSoup(html, features="html.parser")
    #find tag where our information is located
    block = soup.find('div', class_="content-inner")
    nums = block.find_all('div', class_="maincounter-number")
    percent_table = block.find_all('strong')
    num_table = block.find_all('span', class_="number-table")
    nums_table = block.find_all('div', class_="number-table-main")
    # add all needed info to list in dictionary form
    glob.append({
            'cases':nums[0].find('span').text,
            'deaths':nums[1].find('span').text,
            'recovered':nums[2].find('span').text
            })
    glob.append({
            'infected':nums_table[0].text,
            'mid':num_table[0].text,
            'midp':percent_table[0].text,
            'serious':num_table[1].text,
            'seriousp':percent_table[1].text,
            })
    glob.append({
            'closed':nums_table[1].text,
            'recovered':num_table[2].text,
            'recoveredp':percent_table[2].text,
            'deaths':num_table[3].text[1:],
            'deathsp':percent_table[3].text,
            })
    
    return glob
    

def get_countries(html):
    countries = []
    soup = BeautifulSoup(html, features="html.parser")
    # find html table where countries list is located
    table = soup.find('table', class_="table")
    #go through all rows in a table except first(header) and last(total_row)
    for row in table.find_all('tr')[1:-1]:
        #get all coloumn of the first row
        cols = row.find_all('td')
        #place needed info to list in dictionary form
        countries.append({
            'country':cols[0].text,
            'total_cases':cols[1].text,
            'new_cases':cols[2].text,
            'total_deaths':cols[3].text,
            'new_deaths':cols[4].text,
            'total_recovered':cols[5].text,
            'active_cases':cols[6].text,
            'serious':cols[7].text,
            'tot_cases':cols[8].text,
            'deaths':cols[9].text
            })
    return countries

def main():
    try:
        #delete pass if you want to run any function in here

        print(get_global(get_html("https://www.worldometers.info/coronavirus/")))
        #print(get_countries(get_html("https://www.worldometers.info/coronavirus/")))
    except requests.exceptions.ConnectionError:
        #print "no internet!" if ConnectionError exception occur 
        print("No Internet Connecton\nTry Again!")

if __name__ == '__main__':
    main()
