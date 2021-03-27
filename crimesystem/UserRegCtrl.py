from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as MySql

@xframe_options_exempt
def UserInterface(request):
    return render(request,"UserRegistration.html",{'msg':''})

@xframe_options_exempt
def userDetailSubmit(request):
    try:
        db = MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        smt = db.cursor()
        userusername = request.POST['userusername']
        pwd = request.POST['pwd']
        repeatpwd = request.POST['repeatpwd']
        fn = request.POST['fn']
        mn = request.POST['mn']
        ln = request.POST['ln']
        dob = request.POST['dob']
        gen = request.POST['gen']
        email = request.POST['email']
        mob = request.POST['mob']
        adhr = request.POST['adhr']
        state = request.POST['state']
        city = request.POST['city']
        add = request.POST['add']
        img = request.FILES['pic']
        if pwd==repeatpwd:
            query="insert into userlogin(userusername,password,repeatpassword,firstname,middlename,lastname,dob,gender,emailaddress,mobilenumber,aadharnumber,state,city,address,image) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(userusername,pwd,repeatpwd,fn,mn,ln,dob,gen,email,mob,adhr,state,city,add,img.name)
            smt.execute(query)
            db.commit()
            db.close()
            file=open("e:/crimesystem/asset/"+img.name,"wb")
            for chunk in img.chunks():
                file.write(chunk)
            file.close()
            msg='Record Submitted'
        elif pwd != repeatpwd:
            msg='Failed, Password Not Matched'
        return render(request, "UserRegistration.html", {'msg':msg})

    except Exception as e:
        print(e)
        return render(request,"UserRegistration.html",{'msg':'Fail to Submit Record'})