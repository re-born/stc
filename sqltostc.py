import mysql.connector
import sqlconfig
import sys

def readtable(query):
    cnx = mysql.connector.connect(database=sqlconfig.db, user=sqlconfig.user, password=sqlconfig.passwd, host=sqlconfig.host)
    cur = cnx.cursor(buffered=True)
    
    rows = cur.fetchall()
    
    cnx.close()
    cur.close()
    
    return rows

def alltweetids():
    idlist = []
    query = "select * from " + sqlconfig.id_table_name
    rows = readtable(query)
    for row in rows:
        idlist.append(row)
    return idlist
        
def alltweets():
    dic = {}
    query = "select " + "success, item_id, text" + " from " + sqlconfig.tweet_table_name
    rows = readtable(query)
    for (success, item_id, text) in rows:
        if isvalid(success):
            dic[str(item_id)] = text
        else:
            errorlog(success, item_id)
    return dic

def isvalid():
    return 1 == int(success)
    
def genidquery(ids):
    query = "(,"
    last = ")"
    for id in ids:
        query = query + str(id)
    return query + last

log = []
def errorlog(success, item_id):
    log.append((success, item_id))