from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from loginapp.models import questionBank
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from mysite.utils import render_to_pdf
import random
import datetime
from django.contrib import messages

def home(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Succesfully Logged out!")
        return redirect('home')
    return render(request, 'home.html')


def loginpage(request):
    return render(request, 'login.html')


def view_login(request):
    if request.method == "POST":
        loginusername = request.POST['username']
        loginpass = request.POST['password']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in!")
            return redirect('index')

    messages.warning(request, "Login Failed! Please Try Again")
    return render(request, 'login.html')


@login_required(login_url='home')
def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Succesfully Logged out!")
        return redirect('home')


@login_required(login_url='login')
def intermediate(request):
    nques = request.POST.get('nques')
    params = {"nques": nques}
    return render(request, 'intermediate.html', params)


@login_required(login_url='login')
def intermediate2(request):
    nq1 = request.POST.get('nq1')
    nq2 = request.POST.get('nq2')
    nq3 = request.POST.get('nq3')
    nq4 = request.POST.get('nq4')
    nq5 = request.POST.get('nq5')
    params = {"nq1": nq1, "nq2": nq2, "nq3": nq3, "nq4": nq4, "nq5": nq5}
    return render(request, 'intermediate2.html', params)


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        print('GenertePaperRequest2')
        l = []
        tmarks = 0
        dat = datetime.date.today().strftime("%d/%m/%Y")

        Year = request.GET.get('Year')
        Year = int(Year)
        sub = request.GET.get('subject')
        ayear = request.GET.get('ayear')
        dep = request.GET.get('dep')
        test_name = request.GET.get('test_name')
        term = request.GET.get('term')
        subcode = request.GET.get('subcode')
        div = request.GET.get('div')
        ttime = request.GET.get('ttime')

        m1_1 = request.GET.get('m1_1')
        q1_1 = request.GET.get('q1_1')
        m1_2 = request.GET.get('m1_2')
        q1_2 = request.GET.get('q1_2')
        m1_3 = request.GET.get('m1_3')
        q1_3 = request.GET.get('q1_3')

        m2_1 = request.GET.get('m2_1')
        q2_1 = request.GET.get('q2_1')
        m2_2 = request.GET.get('m2_2')
        q2_2 = request.GET.get('q2_2')
        m2_3 = request.GET.get('m2_3')
        q2_3 = request.GET.get('q2_3')

        m3_1 = request.GET.get('m3_1')
        q3_1 = request.GET.get('q3_1')
        m3_2 = request.GET.get('m3_2')
        q3_2 = request.GET.get('q3_2')
        m3_3 = request.GET.get('m3_3')
        q3_3 = request.GET.get('q3_3')

        m4_1 = request.GET.get('m4_1')
        q4_1 = request.GET.get('q4_1')
        m4_2 = request.GET.get('m4_2')
        q4_2 = request.GET.get('q4_2')
        m4_3 = request.GET.get('m4_3')
        q4_3 = request.GET.get('q4_3')

        m5_1 = request.GET.get('m5_1')
        q5_1 = request.GET.get('q5_1')
        m5_2 = request.GET.get('m5_2')
        q5_2 = request.GET.get('q5_2')
        m5_3 = request.GET.get('m5_3')
        q5_3 = request.GET.get('q5_3')

        my_list = ['a)', 'b)', 'c)', 'd)']
        ggs = 0

        fquestions1 = []
        qno1 = []
        l=[]

        or_fquestions1 = []

        if m1_1:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q1_1), marks=int(m1_1))
            question = a[random.randrange(1, len(a))]
            fquestions1.append(tuple((question, my_list[ggs])))
            l.append(question)
            or_question = question
            while or_question == question:
                or_question = a[random.randrange(1, len(a))]
            or_fquestions1.append(tuple((or_question, my_list[ggs])))
            l.append(or_question)
            ggs += 1
            tmarks+=int(m1_1)

        if m1_2:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q1_2), marks=int(m1_2))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions1.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions1.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m1_2)

        if m1_3:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q1_3), marks=int(m1_3))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions1.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions1.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m1_1)

        qno1 = len(fquestions1)

        ggs = 0

        fquestions2 = []
        qno2 = []
        l=[]

        or_fquestions2 = []

        if m2_1:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q2_1), marks=int(m2_1))
            question = a[random.randrange(1, len(a))]
            fquestions2.append(tuple((question, my_list[ggs])))
            l.append(question)
            or_question = question
            while or_question == question:
                or_question = a[random.randrange(1, len(a))]
            or_fquestions2.append(tuple((or_question, my_list[ggs])))
            l.append(or_question)
            ggs += 1
            tmarks+=int(m2_1)

        if m2_2:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q2_2), marks=int(m2_2))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions2.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions2.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m2_2)

        if m2_3:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q2_3), marks=int(m2_3))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions2.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions2.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m2_3)

        qno2 = len(fquestions2)

        ggs = 0

        fquestions3 = []
        qno3 = []
        l=[]

        or_fquestions3 = []

        if m3_1:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q3_1), marks=int(m3_1))
            question = a[random.randrange(1, len(a))]
            fquestions3.append(tuple((question, my_list[ggs])))
            l.append(question)
            or_question = question
            while or_question == question:
                or_question = a[random.randrange(1, len(a))]
            or_fquestions3.append(tuple((or_question, my_list[ggs])))
            l.append(or_question)
            ggs += 1
            tmarks+=int(m3_1)

        if m3_2:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q3_2), marks=int(m3_2))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions3.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions3.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m3_2)

        if m3_3:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q3_3), marks=int(m3_3))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions3.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions3.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m3_3)

        qno3 = len(fquestions3)

        ggs = 0

        fquestions4 = []
        qno4 = []
        l=[]

        or_fquestions4 = []

        if m4_1:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q4_1), marks=int(m4_1))
            question = a[random.randrange(1, len(a))]
            fquestions4.append(tuple((question, my_list[ggs])))
            l.append(question)
            or_question = question
            while or_question == question:
                or_question = a[random.randrange(1, len(a))]
            or_fquestions4.append(tuple((or_question, my_list[ggs])))
            l.append(or_question)
            ggs += 1
            tmarks+=int(m4_1)

        if m4_2:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q4_2), marks=int(m4_2))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions4.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions4.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m4_2)

        if m4_3:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q4_3), marks=int(m4_3))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions4.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions4.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m4_3)

        qno4 = len(fquestions4)

        ggs = 0

        fquestions5 = []
        qno5 = []
        l=[]

        or_fquestions5 = []

        if m5_1:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q5_1), marks=int(m5_1))
            question = a[random.randrange(1, len(a))]
            fquestions5.append(tuple((question, my_list[ggs])))
            l.append(question)
            or_question = question
            while or_question == question:
                or_question = a[random.randrange(1, len(a))]
            or_fquestions5.append(tuple((or_question, my_list[ggs])))
            l.append(or_question)
            ggs += 1
            tmarks+=int(m5_1)

        if m5_2:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q5_2), marks=int(m5_2))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions5.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions5.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m5_2)

        if m5_3:
            a = questionBank.objects.filter(
                year=int(Year), subname=sub, unit=int(q5_3), marks=int(m5_3))
            while(1):
                question = a[random.randrange(1, len(a))]
                if question not in l:
                    fquestions5.append(tuple((question, my_list[ggs])))
                    l.append(question)
                    break

            while(1):
                or_question = a[random.randrange(1, len(a))]
                if or_question not in l:
                    or_fquestions5.append(tuple((or_question, my_list[ggs])))
                    l.append(or_question)
                    break
            ggs += 1
            tmarks+=int(m5_3)

        qno5 = len(fquestions5)

        year_ = ''
        if Year == 1:
            year_ = 'FE'
        elif Year == 2:
            year_ = 'SE'
        elif Year == 3:
            year_ = 'TE'
        else:
            year_ = 'BE'

        data = {
            "sub": sub,
            "date": dat,
            "ayear": ayear,
            "dep": dep,
            "test_name": test_name,
            "term": term,
            "tmarks": tmarks,
            "subcode": subcode,
            "div": div,
            "ttime": ttime,
            "year": year_,
            "fquestions1": fquestions1,
            "or_fquestions1": or_fquestions1,
            "qno1": qno1,
            "fquestions2": fquestions2,
            "or_fquestions2": or_fquestions2,
            "qno2": qno2,
            "fquestions3": fquestions3,
            "or_fquestions3": or_fquestions3,
            "qno3": qno3,
            "fquestions4": fquestions4,
            "or_fquestions4": or_fquestions4,
            "qno4": qno4,
            "fquestions5": fquestions5,
            "or_fquestions5": or_fquestions5,
            "my_list": my_list,
            "qno5": qno5,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def generatePaper(request):
    print('GenertePaperRequest')
    return render(request, 'generatePaper.html')


@login_required(login_url='login')
def delete(request):
    return render(request, 'delete.html')


@login_required(login_url='login')
def deleteQuestion(request):
    year = request.POST.get('year')
    subname = request.POST.get('subname')
    unit = request.POST.get('unit')

    if year == '' and subname == '' and unit == '':
        a = questionBank.objects.all()
    elif year == '' and subname == '':
        a = questionBank.objects.filter(unit=unit)
    elif subname == '' and unit == '':
        a = questionBank.objects.filter(year=year)
    elif year == '' and unit == '':
        a = questionBank.objects.filter(subname=subname)
    elif unit == '':
        a = questionBank.objects.filter(year=year, subname=subname)
    elif year == '':
        a = questionBank.objects.filter(subname=subname, unit=unit)
    elif subname == 'L':
        a = questionBank.objects.filter(year=year, unit=unit)
    else:
        a = questionBank.objects.filter(year=year, subname=subname, unit=unit)

    print(a)
    params = {"a": a, "subname": subname, "year": year, "unit": unit}
    return render(request, 'deleteQuestion.html', params)


@login_required(login_url='login')
def deleteSuccess(request):
    id = request.GET.get('idtodelete')
    questionBank.objects.filter(id=id).delete()
    return render(request, 'deleteSuccess.html')
