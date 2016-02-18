#-*- coding: utf-8 -*-
import mysql.connector
import sqlconfig
import sys

def read_table(query):
    cnx = mysql.connector.connect(database=sqlconfig.db, user=sqlconfig.user, password=sqlconfig.passwd, host=sqlconfig.host)
    cur = cnx.cursor(buffered=True)

    cur.execute(query)
    rows = cur.fetchall()

    cnx.close()
    cur.close()

    return rows

def all_tweet_ids():
    idlist = []
    query = "select * from " + sqlconfig.id_table_name
    rows = read_table(query)
    for row in rows:
        idlist.append(row)
    return idlist

def all_tweets():
    dic = {}
    query = "select " + "success, item_id, text" + " from " + sqlconfig.tweet_table_name
    rows = read_table(query)
    for (success, item_id, text) in rows:
        if isvalid(success):
            dic[str(item_id)] = text
        else:
            errorlog(success, item_id)
    return dic

def isvalid(success):
    return 1 == int(success)

log = []
def errorlog(success, item_id):
    log.append((success, item_id))

if __name__ == '__main__':
    ids = all_tweet_ids()
    tweets = all_tweets()
    print ids
    for id in tweets:
        print id,tweets[id]