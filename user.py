from peewee import *

conn = PostgresqlDatabase('Company', user='postgres', host='localhost', password='skyblue2009*')
conn.connect()

class Userpy(Model):
    id = AutoField()
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        table_name = "users"
        database = conn

#create the table
Userpy.create_table(fail_silently=True)

#inserting
'''Projectone = Projectpy(title = 'Awesome testing',
                       startfrom = '2018-09-21',
                       endat = '2018-09-24', description = 'Testing is amazing',
                       amount = 5000, status = 1)
#save the insert data
Projectone.save()
'''

data = Userpy.select()



