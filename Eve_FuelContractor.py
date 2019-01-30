import sqlite3
import urllib3.request
import urllib3.connection
import xml.etree.ElementTree as ET

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def SQLite():
    """
    Returns SQLite cursor
    """

    # ROOT DIRECTORY#
    #root = 'C:/Users/ScaryDomain/PycharmProjects/fbTrack/venv/'
    root = 'C:/Users/kczarniecki/Documents/eveMoneyMaker'
    ###

    # SQLITE Connector
    conn = sqlite3.connect(root + '/sqlite-latest.sqlite')
    c = conn.cursor()
    ###

    return c

def checkVal(value):
    """
    :param value:
    :return Converts str,int or array to correct value for SQLLite():
    """

    if (isinstance(value, str)):
        value = [value]

    elif (isinstance(value, int)):
        value = [str(value)]
        test = value[0]

        if(isinstance(test, int)):
            value = [str(test)]

    return value


def getMats(typeID):
    """
    Searches database provided in SQLite() function and looks for all data related to provided item type.
    Is able to convert: int, array (w/wo int), str
    """

    typeID = checkVal(typeID)

    c = SQLite()
    mats = c.execute("SELECT [materialTypeID],[quantity] FROM invTypeMaterials WHERE typeID = ?", typeID)

    return mats.fetchall()

def getRegions():
    """
    Returns collection of region ID's and Names
    :return:
    """

    c = SQLite()
    regions = c.execute(
        "SELECT regionID, regionName FROM mapRegions WHERE regionID IN "
        "(SELECT distinct(RegionId) FROM mapSolarSystems WHERE Security > 0)"
    )

    return regions.fetchall()


def getPrice(itemType, orderType, region = None):
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = 'https://api.evemarketer.com/ec/marketstat?typeid=' + str(itemType)

    if(region != None):
        url += '&regionlimit=' + str(region)

    http = urllib3.PoolManager()
    request = http.request('GET', url)
    request = request.data
    tree = ET.fromstring(request)

    for t in tree.iter(orderType):
        ret = float(t.find('max').text)

    return ret





##### REGION LIST ######

regionIDs = getRegions()

######## MAIN ########

#Hydrogen Fuel Block ID: 4246
fbid = 4246
###



scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Main").sheet1




#ADD FUNCTION THAT WILL ALLOW TO DISPLAY TOP 10 BEST DEALS IN PROVIDED REGION FOR CURRENT PRODUCT
#AND THAT WILL WRITE TO THE SPREADSHEET
