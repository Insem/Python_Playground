import sqlite3
import urllib3.request
import urllib3.connection
import xml.etree.ElementTree as ET

def SQLite():
    """
    Returns SQLite cursor
    """

    # ROOT DIRECTORY#
    root = 'C:/Users/ScaryDomain/PycharmProjects/fbTrack/venv/'
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




##### REGION LIST ######

regionIDs = getRegions()

######## MAIN ########

#Hydrogen Fuel Block ID: 4246
fbid = 4246
###

url = 'https://api.evemarketer.com/ec/marketstat?typeid=34'

http = urllib3.PoolManager()
test = http.request('GET', url)

test = test.data

tree = ET.fromstring(test)

for t in tree.iter('sell'):
    print(t.text)
    print(t.find('max').text)
    print(t.text)
