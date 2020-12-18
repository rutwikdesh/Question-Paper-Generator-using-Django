from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from loginapp.models import questionBank
import random
from docx import Document
from datetime import datetime

import pdb

from django.views.generic import View

from mysite.utils import render_to_pdf #created in step 4

def intermediate(request):
    nques = request.POST.get('nques')
    params = {"nques":nques}
    return render(request, 'intermediate.html', params)

def intermediate2(request):
    nq1 = request.POST.get('nq1')
    nq2 = request.POST.get('nq2')
    nq3 = request.POST.get('nq3')
    nq4 = request.POST.get('nq4')
    nq5 = request.POST.get('nq5')
    params = {"nq1":nq1, "nq2":nq2, "nq3":nq3, "nq4":nq4, "nq5":nq5}
    return render(request, 'intermediate2.html', params)

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        print('GenertePaperRequest2')
        l = []
        dat = datetime.today().strftime("%Y-%m-%d")
        Year = request.GET.get('Year')
        Year = int(Year)
        sub = request.GET.get('subject')
        ayear = request.GET.get('ayear')
        dep = request.GET.get('dep')
        test_name = request.GET.get('test_name')
        term = request.GET.get('term')
        tmarks = request.GET.get('tmarks')
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

        my_list = ['a)','b)','c)','d)']
        ggs = 0

        fquestions1 = []
        qno1 = []
        mks1 = []

        if m1_1:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q1_1), marks=int(m1_1))
            question = a[random.randrange(1,len(a))]
            fquestions1.append(tuple((question,my_list[ggs])))
            ggs += 1

        if m1_2:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q1_2), marks=int(m1_2))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions1:
                    fquestions1.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break

        if m1_3:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q1_3), marks=int(m1_3))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions1:
                    fquestions1.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break
        
        qno1 = len(fquestions1)
        ggs = 0
            

        ggs = 0

        fquestions2 = []
        qno2 = []
        mks2 = []

        if m2_1:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q2_1), marks=int(m2_1))
            question = a[random.randrange(1,len(a))]
            fquestions2.append(tuple((question,my_list[ggs])))
            ggs += 1

        if m2_2:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q2_2), marks=int(m2_2))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions1:
                    fquestions2.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break

        if m2_3:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q2_3), marks=int(m2_3))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions2:
                    fquestions2.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break
        
        qno2 = len(fquestions2)

        fquestions3 = []
        qno3 = []
        mks3 = []

        if m3_1:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q1_1), marks=int(m1_1))
            question = a[random.randrange(1,len(a))]
            fquestions3.append(tuple((question,my_list[ggs])))
            ggs += 1

        if m3_2:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q3_2), marks=int(m3_2))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions3:
                    fquestions3.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break

        if m3_3:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q3_3), marks=int(m3_3))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions3:
                    fquestions3.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break
        
        qno3 = len(fquestions3)

        fquestions4 = []
        qno4 = []
        mks4 = []

        if m4_1:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q4_1), marks=int(m4_1))
            question = a[random.randrange(1,len(a))]
            fquestions4.append(tuple((question,my_list[ggs])))
            ggs += 1

        if m4_2:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q4_2), marks=int(m4_2))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions4:
                    fquestions4.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break

        # if m4_3:
        #     a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q4_3), marks=int(m1_3))
        #     while(1):
        #         question = a[random.randrange(1,len(a))]
        #         if question not in fquestions4:
        #             fquestions4.append(question)
        #             mks4.append(m4_3)
        #             break
        
        qno4 = len(fquestions4)

        fquestions5 = []
        qno5 = []
        mks5 = []

        if m5_1:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q5_1), marks=int(m5_1))
            question = a[random.randrange(1,len(a))]
            fquestions5.append(tuple((question,my_list[ggs])))
            ggs += 1

        if m5_2:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q5_2), marks=int(m5_2))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions5:
                    fquestions5.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break

        if m5_3:
            a = questionBank.objects.filter(year=int(Year), subname=sub, unit=int(q5_3), marks=int(m5_3))
            while(1):
                question = a[random.randrange(1,len(a))]
                if question not in fquestions5:
                    fquestions5.append(tuple((question,my_list[ggs])))
                    ggs += 1
                    break
        
        qno5 = len(fquestions5)
        


        # unit_one = request.GET.get('1', '') == 'on'
        # if unit_one:
        #     l.append(1)
        # unit_two = request.GET.get('2', '') == 'on'
        # if unit_two:
        #     l.append(2)
        # unit_three = request.GET.get('3', '') == 'on'
        # if unit_three:
        #     l.append(3)
        # unit_four = request.GET.get('4', '') == 'on'
        # if unit_four:
        #     l.append(4)
        # unit_five = request.GET.get('5', '') == 'on'
        # if unit_five:
        #     l.append(5)
        # unit_six = request.GET.get('6', '') == 'on'
        # if unit_six:
        #     l.append(6)


        # a1 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[0]))
        # if len(l)>1:
        #     a2 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[1]))
        # if len(l)>2:
        #     a3 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[2]))
        # if len(l)>3:
        #     a4 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[3]))
        # if len(l)>4:
        #     a5 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[4]))
        # if len(l)>5:
        #     a6 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[5]))

        # print(l)

        # final_list1 = []
        # z = 1
        # for i in a1:
        #     k = "Q" + str(z) + ". " + i.question + " " + str(i.marks) + " marks"
        #     final_list1.append(k)
        #     z=z+1            

        # sub = request.GET.get('subject')
        # ayear = request.GET.get('ayear')
        # dep = request.GET.get('dep')
        # test_name = request.GET.get('test_name')
        # term = request.GET.get('term')
        # tmarks = request.GET.get('tmarks')
        # subcode = request.GET.get('subcode')
        # div = request.GET.get('div')
        # ttime = request.GET.get('ttime')

        data = {
            "sub":sub,
            "date":dat,
            "ayear":ayear,
            "dep":dep,
            "test_name":test_name,
            "term":term,
            "tmarks":tmarks,
            "subcode":subcode,
            "div":div,
            "ttime":ttime,
            "year":Year,
            "fquestions1":fquestions1,
            "mks1":mks1,
            "qno1":qno1,
            "fquestions2":fquestions2,
            "mks2":mks2,
            "qno2":qno2,
            "fquestions3":fquestions3,
            "mks3":mks3,
            "qno3":qno3,
            "fquestions4":fquestions4,
            "mks4":mks4,
            "qno4":qno4,
            "fquestions5":fquestions5,
            "mks5":mks5,
            "my_list":my_list,
            "qno5":qno5,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def index(request):
    return render(request, 'index.html')

def generatePaper(request):
    print('GenertePaperRequest')
    return render(request, 'generatePaper.html')

# def generatePaper2(request):
#     print('GenertePaperRequest2')
#     l = []
#     Year = request.POST.get('Year')
#     sub = request.POST.get('subject')
#     nques = request.POST.get('nques')

#     Year = int(Year)

#     unit_one = request.POST.get('1', '') == 'on'
#     if unit_one:
#         l.append(1)
#     unit_two = request.POST.get('2', '') == 'on'
#     if unit_two:
#         l.append(2)
#     unit_three = request.POST.get('3', '') == 'on'
#     if unit_three:
#         l.append(3)
#     unit_four = request.POST.get('4', '') == 'on'
#     if unit_four:
#         l.append(4)
#     unit_five = request.POST.get('5', '') == 'on'
#     if unit_five:
#         l.append(5)
#     unit_six = request.POST.get('6', '') == 'on'
#     if unit_six:
#         l.append(6)


#     a1 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[0]))
#     if len(l)>1:
#         a2 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[1]))
#     if len(l)>2:
#         a3 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[2]))
#     if len(l)>3:
#         a4 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[3]))
#     if len(l)>4:
#         a5 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[4]))
#     if len(l)>5:
#         a6 = questionBank.objects.filter(year=Year, subname=sub, unit=int(l[5]))

#     print(l)

#     params = {"a1":a1}
#     return render(request, 'pdf/invoice.html', params)

def about(request):
    mytext = request.POST.get('ques1', 'default')    #get the text from text box
    noOfQues = request.POST.get('noOfQues', 'NULL')
    print("mytext: "+mytext)
    print("noOFQes: "+noOfQues)

    k=''
    l=[]
    for i in mytext:
        k=k+i
        if i=='\n':
            k = k.strip()
            l.append(k)
            k=''

    finalListOfQues = []
    
    print(l)
    i = 0
    while i < int(noOfQues):
        rand = random.choice(3)
        if rand not in finalListOfQues:
            finalListOfQues.append(rand)
            i=i+1

    print(finalListOfQues)

    lastString = ''
    z = 1
    for i in finalListOfQues:
        i = "Q" + str(z) + ". " + i
        lastString = lastString + i + "\n"
        z = z+1

    params = {"q1" : lastString}
    return render(request, 'questions.html', params)


def addQuestion(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
    params = {"a":search}
    return HttpResponse(search)
    # return render(request, 'addQuestion.html', params)

def addSuccess(request):
    questionBan = questionBank()
    questionBan.question = request.POST.get('question', 'default')
    questionBan.bt = request.POST.get('bt', 0)
    questionBan.co = request.POST.get('co', 'NULL')
    questionBan.marks = request.POST.get('marks', 0)
    questionBan.unit = request.POST.get('unit',0)
    questionBan.year = request.POST.get('year', 0)
    questionBan.subname = request.POST.get('subname', 'default')
    questionBan.save()
    print(questionBan.subname)
    return render(request, 'addSuccess.html')

def delete(request):
    return render(request, 'delete.html')

def deleteQuestion(request):
    year = request.POST.get('year')
    subname = request.POST.get('subname')
    unit = request.POST.get('unit')

    if year=='' and subname=='' and unit=='':
        a = questionBank.objects.all()
    elif year=='' and subname=='':
        a = questionBank.objects.filter(unit=unit)
    elif subname=='' and unit=='':
        a = questionBank.objects.filter(year=year)
    elif year=='' and unit=='':
        a = questionBank.objects.filter(subname=subname)
    elif unit=='':
        a = questionBank.objects.filter(year=year, subname=subname)
    elif year=='':
        a = questionBank.objects.filter(subname=subname, unit=unit)
    elif subname=='L':
        a = questionBank.objects.filter(year=year, unit=unit)
    else:
        a = questionBank.objects.filter(year=year, subname=subname, unit=unit)

    print(a)
    params = {"a":a, "subname":subname, "year": year, "unit":unit}
    return render(request, 'deleteQuestion.html', params)

def deleteSuccess(request):
    id = request.GET.get('idtodelete')
    questionBank.objects.filter(id=id).delete()
    return render(request, 'deleteSuccess.html')

def displayQuestionBank(request):
    questionBank = questionBank.objects.all()
    year = request.POST.get('year')
    subname = request.POST.get('subname')
    l=[]
    for i in questionBank:
        if i.year == year and i.subname == subname:
            l.append(i.question)
    random.shuffle(l)
    params = {"ques":l}
    return render(request, 'showQuestions')

# def generatePaper2(request):
#     subname = request.POST.get('subname')
#     chapterstoinclude = request.POST.get('unit')
#     marks = request.POST.get('marks')
#     time = request.POST.get('time')
#     totalQuestions = request.POST.get('ques')
#     return render(request, 'generatePaper2.html')
    
