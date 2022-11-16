import mysql.connector
import pymongo
import os
from dotenv import load_dotenv
import time
load_dotenv()


mysql_host = os.getenv("DB_HOST")
mysql_database = os.getenv("DB_NAME")
mysql_user = os.getenv("DB_USER")
mysql_password = os.getenv("DB_PASSWORD")
mongodb_host = os.getenv("MONGO_DB_HOST")
mongodb_dbname = os.getenv("MONGO_DB_NAME")

myclient = pymongo.MongoClient(mongodb_host, username=os.getenv("MONGO_NAME"), password=os.getenv("MONGO_PASS"))
mydb = myclient[mongodb_dbname]
mycol = mydb["percentages"]


while True:
    try:
        mysqldb = mysql.connector.connect(
            host=mysql_host,
            database=mysql_database,
            user=mysql_user,
            password=mysql_password,
            auth_plugin='mysql_native_password'
        )
    except:
        print("An exception occurred") 

    mycursor = mysqldb.cursor(dictionary=True)

    mycursor.execute(
        "SELECT MAX(percent) AS highest_grade, MIN(percent) AS lowest_grade, FLOOR(AVG(percent)) AS avg_grade from percentages;")

    myresult = mycursor.fetchall()

    if len(myresult) > 0:
        if myresult[0]['highest_grade'] != None:
            x = mycol.insert_many(myresult)
    else:
        mycol.delete_many({"highest_grade": None})

