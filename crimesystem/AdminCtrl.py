from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql as MySql
from django.http import JsonResponse
from django.contrib import auth

@xframe_options_exempt
def AdminLogin(request):
    return render(request,"AdminLogin.html",{'msg':''})

@xframe_options_exempt
def checkAdminLogin(request):
    db = MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
    smt = db.cursor()
    adminusername = request.POST['adminusername']
    pwd = request.POST['pwd']
    query="select * from adminlogin where adminusername='{}' and password='{}'".format(adminusername,pwd)
    smt.execute(query)
    row=smt.fetchone()
    db.close()
    if(row):
        request.session['ADMIN_SES']=row
        return render(request, "Admindashboard.html", {'admin': request.session['ADMIN_SES']})
    else:
        return render(request, "AdminLogin.html", {'msg': 'Invalid Admin Username/Password'})

@xframe_options_exempt
def ActionSearchComplaintspage(request):
    try:
        rec=request.session['ADMIN_SES']
        return render(request,"displayall.html")
    except:
        return render(request,"Adminlogin.html")

def ActionComplaintThanaJson(request):
    try:
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select distinct city from complaint"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)


def ActionDisplayComplaintjson(request):
    try:
        city=request.GET['city']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select * from complaint where city='{}'".format(city)
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def Actiondisplayall(request):
    try:
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select * from complaint"
        cmd.execute(q)
        rows=cmd.fetchall()
        dbe.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def Actionadminlogout(request):
    auth.logout(request)
    return render(request,"Adminlogin.html",{'msg':''})

@xframe_options_exempt
def ActionEditStatus(request):
    try:
        complaintid=request.GET['complaintid']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="select * from complaint where complaintid={}".format(complaintid)
        cmd.execute(q)
        row=cmd.fetchone()
        return render(request,"adminviewcomplaint.html",{'row':row})
    except Exception as e:
        print(e)
        return render(request,"displayall.html",{'row':''})

@xframe_options_exempt
def ActionSaveStatus(request):
    try:
        status=request.GET['status']
        complaintid=request.GET['complaintid']
        dbe=MySql.connect(host='localhost', port=3306, user='root', password='211998', db='crimedashboard')
        cmd=dbe.cursor()
        q="update complaint set status='{}' where complaintid={}".format(status,complaintid)
        cmd.execute(q)
        dbe.commit()
        dbe.close()
        return render(request,"displayall.html")
    except Exception as e:
        print(e)
        return render(request,"displayall.html")