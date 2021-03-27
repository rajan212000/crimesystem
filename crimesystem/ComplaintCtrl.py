from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as MySql

@xframe_options_exempt
def compalintInterface(request):
    try:
        rec=request.session['USER_SES']
        return render(request,"FileComplaint.html",{'rec':rec})
    except:
        return render(request,"Userlogin.html",{'msg':''})

@xframe_options_exempt
def userDetailSubmit(request):
    try:              
        db = MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        smt = db.cursor()
        userusername = request.POST['userusername']
        name=request.POST['name']
        ctype = request.POST['ctype']
        cdetail = request.POST['cdetail']
        date = request.POST['date']
        email = request.POST['email']
        mob = request.POST['mob']
        city=request.POST['city']
        status='Pending'
        query="insert into complaint(userusername,complainttype,complaintdetail,date,emailaddress,mobilenumber,city,status,victimname) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(userusername,ctype,cdetail,date,email,mob,city,status,name)
        smt.execute(query)
        db.commit()
        db.close()
        return render(request,"FileComplaint.html",{'msg':'Record Submitted'})

    except Exception as e:
        print(e)
        return render(request,"FileComplaint.html",{'msg':'Fail to Submit Record'})
