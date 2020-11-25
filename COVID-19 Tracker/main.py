import sys
# imports for web parsing
import requests
from bs4 import BeautifulSoup
#pyqt imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# ui forms imports
from home import *
from update import *
from error import *

# update window class (a child of QMainWindow)
class Update(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.ui = Ui_Update()
        self.ui.setupUi(self)
        self.set_update()
        
    
    
    def set_update(self):
        #set text to labels with our information
        glob_update = get_global(get_html("https://www.worldometers.info/coronavirus/"))
        self.ui.label_8.setText(str(glob_update[1]['infected']))
        self.ui.label_2.setText(str(glob_update[1]['mid']))
        self.ui.label_3.setText("(" + str(glob_update[1]['midp']) + "%)")
        self.ui.label_4.setText(str(glob_update[1]['serious']))
        self.ui.label_5.setText("(" + str(glob_update[1]['seriousp']) + "%)")
        glob_update = get_global(get_html("https://www.worldometers.info/coronavirus/"))
        self.ui.label_21.setText(str(glob_update[2]['closed']))
        self.ui.label_23.setText(str(glob_update[2]['recovered']))
        self.ui.label_24.setText("(" + str(glob_update[2]['recoveredp']) + "%)")
        self.ui.label_26.setText(str(glob_update[2]['deaths']))
        self.ui.label_27.setText("(" + str(glob_update[2]['deathsp']) + "%)")

# retry window class (a child of QMainWindow)
class Retry(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Retry()
        self.ui.setupUi(self)
        #sets connection to retry button (if clicked)
        self.ui.pushButton_4.clicked.connect(self.on_retry_clicked)

    def on_retry_clicked(self):
        try:
            #if button is clicked and pc is connected to internet
            self.home = Home()
            #hide current window
            self.hide()
            #run home window
            self.home.show()
        except requests.exceptions.ConnectionError:
            # if no internet connection nothing happens
            pass
        


#home window class (a child of QMainWindow)
class Home(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #define connections  
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.ui.pushButton.clicked.connect(self.pushButton_3_clicked)
        self.updat = Update()
        self.set_home()

    def pushButton_3_clicked(self):
        #if update button is clicked hide home window and show update window
        self.hide()
        self.updat.show()


    
    def set_home(self):
        #setText to labels with our information
        glob_home = get_global(get_html("https://www.worldometers.info/coronavirus/"))
        self.ui.label_5.setText(str(glob_home[0]['cases']))
        self.ui.label_6.setText(str(glob_home[0]['deaths']))
        self.ui.label_7.setText(str(glob_home[0]['recovered']))
    
#parsing functions (see cvoid-19.py)

def get_html(url):
    r = requests.get(url)
    return r.text

def get_global(html):
    glob = []
    soup = BeautifulSoup(html, features="html.parser")
    block = soup.find('div', class_="content-inner")
    nums = block.find_all('div', class_="maincounter-number")
    percent_table = block.find_all('strong')
    num_table = block.find_all('span', class_="number-table")
    nums_table = block.find_all('div', class_="number-table-main")
        
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
    table = soup.find('table', class_="table")
    for row in table.find_all('tr')[1:-1]:
        cols = row.find_all('td')   
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



if __name__=="__main__":
    try:
        #if there is internet connection on start:
        #create QApplication
        app = QtWidgets.QApplication(sys.argv)
        #Home() object
        myapp = Home()
        #show home window
        myapp.show()
        #run app
        sys.exit(app.exec_())
    except requests.exceptions.ConnectionError:
        #if no connection on start:
        #show retry window
        retry = Retry()
        retry.show()
        
