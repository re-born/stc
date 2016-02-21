#-*- coding: utf-8 -*-
import mysql.connector
import sqlconfig
import sys


def read_table(query):
    cnx = mysql.connector.connect(database=sqlconfig.db, user=sqlconfig.user,
                                  password=sqlconfig.passwd, host=sqlconfig.host)
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


def all_tweets(table_name = None):
    if table_name is None:
        table_name = sqlconfig.tweet_table_name
    dic = {}
    query = "select " + "success, item_id, text" + " from " + table_name
    rows = read_table(query)
    for (success, item_id, text) in rows:
        if isvalid(success):
            dic[str(item_id)] = text
        else:
            errorlog(success, item_id)
    return dic


def all_tweet_pairs():
    id_table = sqlconfig.id_table_name
    tweet_table = sqlconfig.tweet_table_name
    dic = {}
    query = "select " + "t1.item_id, t1.text, t2.item_id, t2.text " + "from " + tweet_table + " as t1 "
    query += "inner join " + id_table + " as ids "
    query += "on t1.item_id = ids.post_id "
    query += "inner join " + tweet_table + " as t2 "
    query += "on ids.reply_id = t2.item_id "
    query += "where t1.success = 1 and t2.success = 1"
    rows = read_table(query)
    pairs = [{"P_ID": row[0], "P_TEXT": row[1], "R_ID": row[2], "R_TEXT": row[3]} for row in rows]
    return pairs


def isvalid(success):
    return 1 == int(success)

log = []


def errorlog(success, item_id):
    log.append((success, item_id))

if __name__ == '__main__':
    tweets = all_tweets(sqlconfig.run_table_name)
    print "check input tweets"
    print len(tweets)
