import psycopg2
import sys
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    try:
            #Define our connection string
        conn_string = "host='deis.certuit.com' dbname='postgres' user='postgres' password='' port='49155'"
     
        # print the connection string we will use to connect
        #print "Connecting to database\n    ->%s" % (conn_string)
     
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
     
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        return "Connected!\n"

    except psycopg2.DatabaseError:
        return 'Error %s'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    resp = app.get('/')