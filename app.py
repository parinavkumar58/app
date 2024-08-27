from flask import Flask,render_template,request,redirect,url_for,flash,session
from user import UserOperation
from organiser import OrgOperation
from encryption import Encryption
from validation import Validation
from datetime import datetime
import razorpay
app=Flask(__name__)    # object of Flask class
app.secret_key="ghgjsd76hkjgy7kdsyuihiiyhujs"   #any value you can put here

client=razorpay.Client(auth=("rzp_test_ncA8cq0QRQXDlq","oAa0hlEpbvYHrg3Of8G139kE"))
userObj = UserOperation()  # object for user
organiserObj=OrgOperation()    # object for organiser
encryptObj = Encryption()  # object for Encryption Class
validObj = Validation()    # object for Validation class


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if request.method=='GET':
        return render_template('user_signup.html')
    else:
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        password=request.form['password']
        # -------------validation--------------------
        frmList=[name,email,mobile,password]
        if(validObj.empty(frmList)):
            flash("field can't be empty!!")
            return redirect(url_for('user_signup'))
        
        if(validObj.checkAlpha(name)):
            flash("Name must be in alphabates!!")
            return redirect(url_for('user_signup'))
        
        if(validObj.checkDigit(mobile) or validObj.checkMobileLength(mobile)):
            flash("Mobile must be a number with length of 10 digits!!")
            return redirect(url_for('user_signup'))


        password=encryptObj.convert(password)  # encryption


        userObj.user_signup(name,email,mobile,password)
        flash("Successfully Registered!! Login Now!!")   #temp session
        return redirect(url_for('user_login'))

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    if request.method=='GET':
        return render_template('user_login.html')
    else:
        email=request.form['email']
        password=request.form['password']
        # -------------validation--------------------
        frmList=[email,password]
        if(validObj.empty(frmList)):
            flash("field can't be empty!!")
            return redirect(url_for('user_login'))
        
        password=encryptObj.convert(password)  # encryption

        row = userObj.user_login(email,password)
        if (row):
            session['name']=row[0][0]
            session['email']=row[0][1]
            return redirect (url_for('user_dashboard'))

        else:
            flash("invalid user & password!!")
            return redirect (url_for('user_login'))
        

@app.route('/user_logout')
def user_logout():
    session.clear()     #it will destroyed all activated session
    flash("succesfully logged out")
    return redirect(url_for('index'))       
        
@app.route('/user_dashboard')
def user_dashboard():
    if 'email'  in session:
         return render_template('user_dashboard.html')
    else:
        flash("please login to access this page")
        return redirect (url_for('user_login'))
        #---------- end validation------------------


@app.route('/user_profile',methods=['GET','POST'])
def user_profile():
        if 'email' in session:
            if request.method=='GET':
                record=userObj.user_profile()
                return render_template('user_profile.html',record=record)
            else:
                name=request.form['name']
                mobile=request.form['mobile']
        
            # -------------validation--------------------
            frmList=[name,mobile]
            if(validObj.empty(frmList)):
                flash("field can't be empty!!")
                return redirect(url_for('user_profile'))
        
            if(validObj.checkAlpha(name)):
                flash("Name must be in alphabates!!")
                return redirect(url_for('user_profile'))
        
            if(validObj.checkDigit(mobile) or validObj.checkMobileLength(mobile)):
                flash("Mobile must be a number with length of 10 digits!!")
                userObj.user_profile_update(name,mobile)
                flash(" user profile is updated succesfully")
                return redirect(url_for('user_profile'))
        else:
        
            flash("please login to access this page")
            return redirect (url_for('user_login'))


@app.route('/user_change_password',methods=['GET','POST'])
def user_change_password():
    if 'email'  in session:
        if request.method=='GET':
            record=userObj.user_profile()
            return render_template('user_change_password.html',record=record)
        else:
            oldPassword=request.form['oldPassword']
            newPassword=request.form['newPassword']
            # -------------validation--------------------
            frmList=[oldPassword,newPassword]
            if(validObj.empty(frmList)):
                flash("field can't be empty!!")
                return redirect(url_for('user_change_password'))
            #--------------encryption---------------------
            oldPassword=encryptObj.convert('oldPassword')  #encryption
            newPassword=encryptObj.convert('newPassword')  #encryption
            r=userObj.user_change_password(oldPassword,newPassword)
            if(r==0):
                flash("your old password is not valid!!")
                return redirect(url_for('user_change_password'))
            else:
                session.clear()
                flash("your password is changed successfully!!")
                return redirect (url_for('user_login'))
    else:
        flash("please login to access this page..")
        return redirect (url_for('user_login'))


@app.route('/user_delete')
def user_delete():
    if 'email'  in session:
        userObj.user_delete()
        flash("Account deleted succesfully")
        return redirect(url_for('index'))
    else:
        flash("please login to access this page")
        return redirect (url_for('user_login'))
    
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/user_camp_explore',methods=['GET','POST'])
def user_camp_explore():
    if 'email'  in session:
         if request.method=='GET':
            record=userObj.user_camp_all()
            return render_template('user_camp_explore.html',record=record)
         else:
             city=request.form['city']
             record=userObj.user_camp_explore(city)
             return render_template('user_camp_explore.html',record=record)
    else:
        flash("please login to access this page")
        return redirect (url_for('user_login'))
    

@app.route('/user_camp_detail',methods=['GET','POST'])
def user_camp_detail():
    if 'email'  in session:
        if request.method=='GET':
            campID=request.args.get('campID')
            record=userObj.user_camp_detail(campID)
            return render_template('user_camp_detail.html',record=record)
        else:
            campID=request.args.get('campID')
            charges=int(request.args.get('charges'))
            person=int(request.form['person'])
            total=charges*person
            data={"amount": total*100,"currency":"INR","receipt":"order_rcptid"}
            payment=client.order.create(data=data)
            pdata=[total*100,payment["id"],person,campID]
            return render_template("payment.html",pdata=pdata)

    else:
        flash("please login to access this page")
        return redirect (url_for('user_login'))
    
@app.route('/success', methods=["POST"])
def success():
    if('email' in session):
        if(request.method=='POST'):
            campID=request.args.get('campID')
            person=request.args.get('person')
            amount=request.args.get('amount')
            pid=request.form.get("razorpay_payment_id")
            ordid=request.form.get("razorpay_order_id")
            sign=request.form.get("razorpay_signature")
            params={
            'razorpay_order_id': ordid,
            'razorpay_payment_id': pid,
            'razorpay_signature': sign
            }
            final=client.utility.verify_payment_signature(params)
            if final == True:
                
                userObj.booking(campID,pid,person,amount)
                flash("Payment Done Successfully!! payment ID is "+str(pid))
                return redirect(url_for('user_camp_explore'))
            else:
                flash("Something Went Wrong Please Try Again")
                return redirect(url_for('user_camp_explore'))
    else:
        flash("please login to access this page..")
        return redirect(url_for('user_login'))
    
@app.route('/user_booking_history')
def user_booking_history():
    if 'email'  in session:
         record= userObj.user_booking_history()
         return render_template('user_booking_history.html',record=record)
    else:
        flash("please login to access this page")
        return redirect (url_for('user_login'))
    
@app.route('/user_review',methods=['GET','POST'])
def user_review():
    if 'email'  in session:
         if request.method=='GET':
            campID=request.args.get('campID')
            record=userObj.user_review(campID)
            return render_template('user_review.html',record=record,campID=campID)
         else:
             campID=request.args.get('campID')
             star=request.form['star']
             comment=request.form['comment']
             userObj.user_review_insert(campID,star,comment)
             return redirect(url_for('user_review',campID=campID))
    else:
        flash("please login to access this page")
        return redirect (url_for('user_login'))
    


#-------------------------------Organiser----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------




@app.route('/org_signup',methods=['GET','POST'])
def org_signup():
    if request.method=='GET':
        return render_template('org_signup.html')
    else:
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        address=request.form['address']
        password=request.form['password']
        # -------------validation--------------------
        frmList=[name,email,mobile,address,password]
        if(validObj.empty(frmList)):
            flash("field can't be empty!!")
            return redirect(url_for('org_signup'))
        
      
        
        if(validObj.checkDigit(mobile) or validObj.checkMobileLength(mobile)):
            flash("Mobile must be a number with length of 10 digits!!")
            return redirect(url_for('org_signup'))


        password=encryptObj.convert(password)  # encryption


        organiserObj.org_signup(name,email,mobile,address,password)
        flash("Successfully Registered!! Login Now!!")   #temp session
        return redirect(url_for('org_login'))

@app.route('/org_login',methods=['GET','POST'])
def org_login():
    if request.method=='GET':
        return render_template('org_login.html')
    else:
        email=request.form['email']
        password=request.form['password']
        # -------------validation--------------------
        frmList=[email,password]
        if(validObj.empty(frmList)):
            flash("field can't be empty!!")
            return redirect(url_for('org_login'))
        
        password=encryptObj.convert(password)  # encryption

        row = organiserObj.org_login(email,password)
        if (row):
            session['org_name']=row[0][0]
            session['org_email']=row[0][1]
            return redirect (url_for('org_dashboard'))

        else:
            flash("invalid org & password!!")
            return redirect (url_for('org_login'))
        

@app.route('/org_logout')
def org_logout():
    session.clear()     #it will destroyed all activated session
    flash("succesfully logged out")
    return redirect(url_for('index'))       
        
@app.route('/org_dashboard')
def org_dashboard():
    if 'org_email'  in session:
     return render_template('org_dashboard.html')
    else:
        flash("please login to access this page")
        return redirect (url_for('org_login'))

@app.route('/org_profile',methods=['GET','POST'])
def org_profile():
    if 'org_email'  in session:
        if request.method=='GET':
            record=organiserObj.org_profile()
            return render_template('org_profile.html',record=record)
        else:
            name=request.form['name']
            mobile=request.form['mobile']
            address=request.form['address']

        
            # -------------validation--------------------
        frmList=[name,mobile,address]
        if(validObj.empty(frmList)):
                flash("field can't be empty!!")
                return redirect(url_for('org_profile'))
       
        
        if(validObj.checkDigit(mobile) or validObj.checkMobileLength(mobile)):
            flash("Mobile must be a number with length of 10 digits!!")
            return redirect(url_for('org_profile'))
        #---------- end validation------------------
        organiserObj.org_profile_update(name,mobile,address)
        flash(" organiser profile is updated succesfully")
        return redirect(url_for('org_profile'))
    else:
        flash("please login to access this page")
        return redirect (url_for('org_login'))
    
@app.route('/org_change_password',methods=['GET','POST'])
def org_change_password():
    if 'org_email'  in session:
        if request.method=='GET':
            record=organiserObj.org_profile()
            return render_template('org_change_password.html',record=record)
        else:
            oldPassword=request.form['oldPassword']
            newPassword=request.form['newPassword']
            # -------------validation--------------------
            frmList=[oldPassword,newPassword]
            if(validObj.empty(frmList)):
                flash("field can't be empty!!")
                return redirect(url_for('org_change_password'))
            #--------------encryption---------------------
            oldPassword=encryptObj.convert('oldPassword')  #encryption
            newPassword=encryptObj.convert('newPassword')  #encryption
            r=organiserObj.org_change_password(oldPassword,newPassword)
            if(r==0):
                flash("your old password is not valid!!")
                return redirect(url_for('org_change_password'))
            else:
                session.clear()
                flash("your password is changed successfully!!")
                return redirect (url_for('org_login'))
    else:
        flash("please login to access this page..")
        return redirect (url_for('org_login'))


@app.route('/org_delete')
def org_delete():
    if 'org_email'  in session:
     
        organiserObj.org_delete()
        flash("Account deleted succesfully")
        return redirect(url_for('index'))
    else:
    
        flash("please login to access this page")
        return redirect (url_for('org_login'))
    

@app.route('/org_new_camp',methods=['GET','POST'])
def org_new_camp():
    if 'org_email'  in session:
        if request.method=='GET':
            return render_template('org_new_camp.html')
        else:
            campName=request.form['campName']
            contact=request.form['contact']
            state=request.form['state']
            city=request.form['city']
            location=request.form['location']
            startDate=request.form['startDate']
            endDate=request.form['endDate']
            charges=request.form['charges']
            descp=request.form['descp']

        # -------------validation--------------------

            frmList=[campName,contact,location,startDate,endDate,charges,descp]
            if(validObj.empty(frmList)):
              flash("field can't be empty!!")
              return redirect(url_for('org_new_camp'))
        

            organiserObj.org_new_camp(campName,contact,state,city,location,startDate,endDate,charges,descp)
            flash("your new camp deatail submitted successfully!!")   #temp session
            return redirect(url_for('org_new_camp'))
    else:
        flash("please login to access this page")
        return redirect (url_for('org_login'))


@app.route('/org_view_camp')
def org_view_camp():
    if 'org_email'  in session:
         record=organiserObj.org_view_camp()
         return render_template('org_view_camp.html',record=record)
     
     
    else:
        flash("please login to access this page")
        return redirect (url_for('org_login'))


@app.route('/org_camp_delete')
def org_camp_delete():
    if 'org_email'  in session:
         if request.method=='GET':

             campID=request.args.get('campID')
             organiserObj.org_camp_delete(campID)
             flash("your camp is deleted successfully")
             return redirect(url_for('org_view_camp'))
    else:
    
        flash("please login to access this page...")
        return redirect (url_for('org_login'))


@app.route('/org_camp_detail',methods=['GET','POST'])
def org_camp_detail():
    if 'org_email'  in session:
        if request.method=='GET':
            campID=request.args.get('campID')
            record=organiserObj.org_camp_detail(campID)
            return render_template('org_camp_detail.html',record=record)
        
        else:
            campID=request.args.get('campID')
            campName=request.form['campName']
            contact=request.form['contact']
            city=request.form['city']
            location=request.form['location']
            startDate=request.form['startDate']
            endDate=request.form['endDate']
            charges=request.form['charges']
            descp=request.form['descp']

        # -------------validation--------------------

            frmList=[campName,contact,city,location,startDate,endDate,charges,descp]
            if(validObj.empty(frmList)):
              flash("field can't be empty!!")
              return redirect(url_for('org_camp_detail',campID=campID))
        

            organiserObj.org_new_camp(campName,contact,city,location,startDate,endDate,charges,descp)
            flash(" camp detail updated successfully!!")   #temp session
            return redirect(url_for('org_camp_detail',campID=campID))

    else:
        flash("please login to access this page!!")
        return redirect (url_for('org_login'))
    
    
@app.route('/org_camp_photo',methods=['GET','POST'])
def org_camp_photo():
    if 'org_email'  in session:
         if request.method=='GET':
             campID=request.args.get('campID')
             photo=organiserObj.org_camp_photo_view(campID)
             return render_template('org_camp_photo.html',campID=campID,photo=photo)
         
         else:
             campID=request.args.get('campID')
             photo=request.files['photo']
             p=photo.filename #retrieve photo name with extension
             if(p==''):
                 flash('must choose one photo!!')
                 return redirect(url_for('org_camp_photo',campID=campID))
             d=datetime.now() #current date time (import datetime)
             t=int(round(d.timestamp()))
             path=str(t)+'.'+p.split('.')[-1]
             photo.save("static/camp/"+path) #create camp folder inside static folder
             organiserObj.org_camp_photo(campID,path)
             flash("photo uploaded succesfully!!")
             return redirect (url_for('org_camp_photo',campID=campID))


    else:
        flash("please login to access this page...")
        return redirect (url_for('org_login'))
    
    
@app.route('/org_photo_delete')
def org_photo_delete():
    if 'org_email'  in session:
         campID=request.args.get('campID')
         campPhotoID=request.args.get('campPhotoID')
         organiserObj.org_photo_delete(campPhotoID)
         flash('photo deleted successfully!!')
         return redirect (url_for('org_camp_photo',campID=campID))
    else:
        flash("please login to access this page")
        return redirect (url_for('org_login')) 

    
@app.route('/org_booking_info')
def org_booking_info():
    if 'org_email'  in session:
         record= organiserObj.org_booking_info()
         return render_template('org_booking_info.html',record=record)
    else:
        flash("please login to access this page")
        return redirect (url_for('org_login'))   


if __name__=='__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0',port='5001',debug=True)

