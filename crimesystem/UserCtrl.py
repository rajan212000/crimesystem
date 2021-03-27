from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as MySql
from django.contrib import auth

@xframe_options_exempt
def UserLogin(request):
    return render(request,"Userlogin.html",{'msg':''})

@xframe_options_exempt
def checkUserLogin(request):
    db = MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
    smt = db.cursor()
    userusername = request.POST['userusername']
    pwd = request.POST['pwd']
    query="select * from userlogin where userusername='{}' and password='{}'".format(userusername,pwd)
    smt.execute(query)
    row=smt.fetchone()
    db.close()
    if(row):
        request.session['USER_SES']=row
        return render(request, "Userdashboard.html", {'user': request.session['USER_SES']})
    else:
        return render(request, "Userlogin.html", {'msg': 'Invalid Username/Password'})

def Actionuserlogout(request):
    auth.logout(request)
    return render(request,"Userlogin.html",{'msg':''})

@xframe_options_exempt
def ActionDisplayAllComplaint(request):
    try:
        rec=request.session['USER_SES']
        userusername=request.GET['userusername']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select * from complaint where userusername='{}'".format(userusername)
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return render(request,"userdisplaycomplaints.html",{'rows':rows})
    except Exception as e:
        print(e)
        return render(request,"Userlogin.html",{'rows':''})

@xframe_options_exempt
def ActionViewComplaintUser(request):
    try:
        complaintid=request.GET['complaintid']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select * from complaint where complaintid='{}'".format(complaintid)
        cmd.execute(q)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"viewcomplaintuser.html",{'row':row})
    except Exception as e:
        print(e)
        return render(request,"userdisplaycomplaints.html",{'row':''})

@xframe_options_exempt
def ActionUserProfile(request):
    try:
        userusername=request.GET['userusername']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select * from userlogin where userusername='{}'".format(userusername)
        cmd.execute(q)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"userprofile.html",{'row':row})
    except Exception as e:
        print(e)
        return render(request,"userdashboard.html",{'row':''})

@xframe_options_exempt
def ActionUserSaveProfile(request):
    try:
        oldusername=request.POST['oldusername']
        userusername=request.POST['userusername']
        fname=request.POST['fname']
        mname=request.POST['mname']
        lname=request.POST['lname']
        email=request.POST['email']
        dob=request.POST['dob']
        mob=request.POST['mob']
        city=request.POST['city']
        state=request.POST['state']
        add=request.POST['add']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="update userlogin set userusername='{}', firstname='{}', middlename='{}', lastname='{}', dob='{}', emailaddress='{}', mobilenumber='{}', state='{}', city='{}', address='{}' where userusername='{}'".format(userusername,fname,mname,lname,dob,email,mob,state,city,add,oldusername)
        cmd.execute(q)
        dbe.commit()
        c="select * from userlogin where userusername='{}'".format(userusername)
        cmd.execute(c)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"userprofile.html",{'row':row})

    except Exception as e:
        print(e)

@xframe_options_exempt
def ActionUserSavePic(request):
    try:
        userusername=request.POST['userusername']
        img=request.FILES['pic']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="update userlogin set image='{}' where userusername='{}'".format(img.name,userusername)
        cmd.execute()
        dbe.commit()
        file=open("e:/crimesystem/asset/"+img.name,"wb")
        for chunk in img.chunks():
            file.write(chunk)
        file.close()
        c="select * from userlogin where userusername='{}'".format(userusername)
        cmd.execute(c)
        row=cmd.fetchone()
        dbe.close()
        return render(request,"userprofile.html",{'row':row})

    except Exception as e:
        print(e)

@xframe_options_exempt
def ActionChangePassword(request):
    try:
        userusername=request.GET['userusername']
        return render(request,"changepassword.html",{'userusername':userusername})
    except Exception as e:
        print(e)

@xframe_options_exempt
def ActionSavePassword(request):
    try:
        userusername=request.GET['userusername']
        cpwd=request.GET['cpwd']
        pwd=request.GET['pwd']
        repeatpwd=request.GET['repeatpwd']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        if pwd==repeatpwd:
            c="select * from userlogin where userusername='{}' and password='{}'".format(userusername,cpwd)
            cmd.execute(c)
            row=cmd.fetchone()
            q="update userlogin set password='{}', repeatpassword='{}' where userusername='{}' and password='{}'".format(pwd,repeatpwd,userusername,cpwd)
            cmd.execute(q)
            dbe.commit()
            dbe.close()
            if row:
                msg='Record Submitted'
            else:
                msg='Wrong Password'
        elif pwd != repeatpwd:
            msg='Failed, Password Not Matched'
        return render(request,"changepassword.html",{'msg':msg,'userusername':userusername})
    except Exception as e:
        print(e)
        msg='Wrong Password'
        return render(request,"changepassword.html",{'msg':msg})