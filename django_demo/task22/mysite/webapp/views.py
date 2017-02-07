from django.shortcuts import render
from django.http import HttpResponse


from django.db import models,MySQLdb


def index(request):
 conn = MySQLdb.connect(host= "localhost:3306",
                  user="root",
                  passwd="root",
                  db="office")
 x = conn.cursor()

try:
   return HttpResponse(x.execute("""INSERT INTO employee VALUES (%s,%s,%s,%s)""",(188,'Chetna','Odisha',2000)))
   conn.commit()
except:
   conn.rollback()

conn.close()



  
  

