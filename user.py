import mysql.connector
from flask import session
from datetime import datetime


class UserOperation:
    def connection(self):
        con=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="b4_fullstack")
        return con
   

    
    def user_signup(self,name,email,mobile,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into user (name,email,mobile,password) values(%s,%s,%s,%s)"
        record=[name,email,mobile,password]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return  
    
    def user_login(self,email,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select name,email,mobile from user where email=%s and password=%s"
        record=[email,password]
        mycursor.execute(sq,record)
        row = mycursor.fetchall()
        mycursor.close()
        db.close()
        return row
    
    
    
    def user_profile(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select name,email,mobile from user where email=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        record = mycursor.fetchall()
        mycursor.close()
        db.close()
        return record
    
    
    def user_profile_update(self,name,mobile):
        db=self.connection()
        mycursor=db.cursor()
        sq="update user set name =%s,mobile=%s where email=%s"
        record=[name,mobile,session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return  
    

    
    def user_delete(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="delete from user where email=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return  
    


      
    def user_change_password(self,oldPassword,newPassword):
        db=self.connection()
        mycursor=db.cursor()
        sq="select * from user where email=%s and password=%s"
        record=[session['email'],oldPassword]
        mycursor.execute(sq,record)
        row= mycursor.fetchall()
        rc = mycursor.rowcount
        if(rc==0):
           return 0
        
        sq="update user set password=%s where email=%s"
        record=[newPassword,session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return 1
   



    def user_camp_explore(self,city):
        db=self.connection()
        mycursor=db.cursor()
        sq="select path,campName,location,startDate,endDate,charges,c.campID from camp c,camp_photo cp where c.campID=cp.campID and city=%s and startDate>%s"
        currentDate=datetime.now()
        record=[city,currentDate]
        mycursor.execute(sq,record)
        record = mycursor.fetchall()
        mycursor.close()
        db.close()
        return record
    
    def user_camp_all(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select path,campName,location,startDate,endDate,charges,c.campID from camp c,camp_photo cp where c.campID=cp.campID and startDate>%s"
        currentDate=datetime.now()
        record=[currentDate]
        mycursor.execute(sq,record)
        record = mycursor.fetchall()
        mycursor.close()
        db.close()
        return record
    
    def user_camp_detail(self,campID):
        db=self.connection()
        mycursor=db.cursor()
        sq="select campName,contact,city,location,startDate,endDate,charges,descp,campID from camp where campID=%s"
        record=[campID]
        mycursor.execute(sq,record)
        record = mycursor.fetchall()
        mycursor.close()
        db.close()
        return record
    

    def booking(self,campID,pid,person,amount):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into booking(campID,userEmail,paymentID,person,amount,bookingDate)values(%s,%s,%s,%s,%s,%s)"

        bookingDate=datetime.now()
        record=[campID,session['email'],pid,person,amount,bookingDate]
        
        mycursor.execute(sq,record)
        db.commit()
        db.close()
        return
    
    def user_booking_history(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select c.campID,campName,contact,city,startDate,person,amount,bookingDate from camp c, booking b where c.campID=b.campID and userEmail=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        record = mycursor.fetchall()
        mycursor.close()
        db.close()
        return record
    
    def user_review(self,campID):
        db=self.connection()
        mycursor=db.cursor()
        sq="select star,name,comment from review r,user u where r.userEmail=u.email and campID=%s"
        record=[campID]
        mycursor.execute(sq,record)
        record = mycursor.fetchall()
        mycursor.close()
        db.close()
        return record
    
    def user_review_insert(self,campID,star,comment):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into review(userEmail,campID,star,comment)values(%s,%s,%s,%s)"
        record=[session['email'],campID,star,comment]
        mycursor.execute(sq,record)
        db.commit()
        db.close()
        return

    