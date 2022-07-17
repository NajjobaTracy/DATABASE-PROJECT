from cs50 import SQL
import csv
open("DOG_STORE.db","w").close()
db = SQL("sqlite:///DOG_STORE.db")
db.execute ("CREATE TABLE DOGS(DOG_ID INTEGER PRIMARY KEY AUTOINCREMENT,DOG_NAME TEXT,BREED_ID INTEGER, AGE INTEGER ,SEX TEXT,PRICE INTEGER ,FOREIGN KEY(BREED_ID) REFERENCES BREED(BREED_ID) );")
db.execute ("CREATE TABLE CUSTOMER(CUSTOMER_ID INTEGER, CUSTOMER_NAME TEXT,BREED_BROUGHT TEXT,ADDRESS TEXT,DOGS_ID INTEGER, FOREIGN KEY (DOGS_ID) REFERENCES DOGS(DOG_ID));")
db.execute ("CREATE TABLE BREED(BREED_NAME TEXT,BREED_ID INTEGER PRIMARY KEY );")

with open("DOG PET STORE.csv", "r") as file:    
    reader=csv.DictReader(file)   
    for row in reader: 
                  
        Dog_name=row["DOG_NAME"]        
        Breed_id=row["BREED_ID"]        
        Age=row["AGE(MONTHS)"]        
        Sex=row["SEX"]        
        Price=row["PRICE"]        
        Customer_id=row["CUSTOMER_ID"]       
        Customer_name=row["CUSTOMER_NAME"]        
        Breed_bought=row["BREED BROUGHT"]        
        Address=row["ADDRESS"]        
        Breed_name=row["BREED_NAME"]                      
        Breed_Id=row["BREED_ID"]
        IDS = db.execute("INSERT INTO BREED(BREED_ID,BREED_NAME) VALUES (?,?);",Breed_Id,Breed_name)      
        IDS2 = db.execute("INSERT INTO DOGS(DOG_NAME,BREED_ID,AGE,SEX,PRICE) VALUES (?,(SELECT BREED_ID FROM BREED WHERE BREED_ID =?),?,?,?);", Dog_name,IDS,Age,Sex,Price)       
        db.execute("INSERT INTO CUSTOMER(CUSTOMER_ID,CUSTOMER_NAME,BREED_BROUGHT,ADDRESS,DOGS_ID) VALUES (?,?,?,?,(SELECT DOG_ID FROM DOGS WHERE DOG_ID = ?));",Customer_id,Customer_name,Breed_bought,Address,IDS2)        
        