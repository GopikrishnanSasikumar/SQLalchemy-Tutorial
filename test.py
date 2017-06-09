#This is a program to insert some data to a database and read them
#Using python and a package called sqlalchemy
#Refer this link
#https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjJ_vDYirHUAhXMrY8KHSZUCvgQFggnMAA&url=https%3A%2F%2Fwww.sqlalchemy.org%2F&usg=AFQjCNF1g-F68vdKCgebFy1OHiy-eSyX5w&sig2=s8aXdX9ZF86egmh28RGN4g



#importing sqlalchemy create_engine
from sqlalchemy import create_engine
from sqlalchemy import *
#importing metadata,Column for defining Column and Table for defining table
from sqlalchemy import MetaData ,Column ,Table
#importing Integer for datatype.(other types are String,Float,Date...etc)
from sqlalchemy import Integer
#creating the database file using create_engine,echo is used to display in terminal(I think so)
engine=create_engine('sqlite:///demo.db',echo=True)
#defining database metadata
metadata=MetaData(bind=engine)

#This is the syntax for creating table
#Table name is given in quotes followed by metadata  Column define the column with value name value and type integer
#try adding more column inside the Table by adding new Column seperated by comma
#like this...
#tudents_table = Table('students', metadata ,Column('Barcodeno', String, primary_key=True),Column('Name', String(40)),Column('Fine', Integer),)
table=Table('table',metadata,Column('value',Integer))
#This line will initialize the table
metadata.create_all()
#Connection to the database is established
connection=engine.connect()
#loading the table to the variable tab
tab=Table('table',metadata,autoload=True)
k=[] #this is a list for storing the input
print('enter 3 numbers')
print() #just for going one line down
for i in range(3):
    #loop,change the value 3 to take more inputs
    a=input() #honey..thats how python takes values from you
    k.append(a) #appending the list that means..damn it just storing each value to the list
print()
print("inserting to database")
print()
for i in k:
    #Taking each value from the list,inserting it to table 
    connection.execute(tab.insert().values(value=i))
#We inserted the values successfully
#now we need toread it..yo use select
#If you have a table called greedy and a column heart,access it using 's=select([greedy.c.heart])' I don't see anything there by the way
s=select([tab.c.value])
#executing the statement 's' and storing the output to 'result'
result=connection.execute(s)
print('stored value')
#Each value for 'value' in result to i 
for i in result:
    #vola...printing it
    print(i.value)
