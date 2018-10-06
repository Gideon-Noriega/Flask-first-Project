from peewee import *

conn = PostgresqlDatabase('Company', user='postgres', host='localhost', password='skyblue2009*')
conn.connect()

class Projectpy(Model):
    title = CharField()
    startfrom = DateField()
    id = AutoField()
    type = DateField()
    endat = DateField()
    description = TextField()
    amount = DoubleField()
    status = IntegerField()

    class Meta:
        table_name = "projectspy"
        database = conn

#create the table
Projectpy.create_table(fail_silently=True)

#inserting
'''Projectone = Projectpy(title = 'Awesome testing',
                       startfrom = '2018-09-21',
                       endat = '2018-09-24', description = 'Testing is amazing',
                       amount = 5000, status = 1)
#save the insert data
Projectone.save()
'''

data = Projectpy.select()



