#!/usr/bin/python3
import pymysql
import staticnumber
def getid():
    db = pymysql.connect("localhost","root",staticnumber.mysqlpassword,"qchat" )
    cursor = db.cursor()
    sql = "select * from idnumber ;"
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        #print(results)
        idnum=results[0]
        int_id=int(idnum)
        int_id=int_id+1
        #print(int_id)
        db.commit()
    except:
        #print(len(results))
        print ("Error: unable to fetch data")
    
    
    cursor2 = db.cursor()
    sql2="update idnumber set unusednumber='"+str(int_id)+"';"
    #print(sql2)
    try:
        cursor2.execute(sql2)
        #print(int_id)
        db.commit()
    except:
        #print(len(results))
        print ("Error: unable to fetch data")
    db.close()
    return int_id

def main():
    getid()


if __name__ == '__main__':
    main()
