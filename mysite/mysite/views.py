from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from loginapp.models import questionBank
import random
from docx import Document
import datetime

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
    nq6 = request.POST.get('nq6')
    nq7 = request.POST.get('nq7')
    nq8 = request.POST.get('nq8')
    nq1 = int(nq1)
    params = {"nq1":range(1,nq1), "nq2":nq2, "nq3":nq3, "nq4":nq4}
    return render(request, 'intermediate2.html', params)

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        print('GenertePaperRequest2')
        l = []
        Year = request.GET.get('Year')
        Year = int(Year)
        sub = request.GET.get('subject')

        m1_1 = request.GET.get('m1_1')
        q1_1 = request.GET.get('q1_1')
        q1_2 = request.GET.get('q1_2')
        q1_3 = request.GET.get('q1_3')

        fquestions = []
        xx = ""

        x = 1
        if m1_1:
            a = questionBank.objects.filter(year=Year, subname=sub, unit=int(q1_1)
        

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

        subject_name = sub

        data = {
            "title":subject_name,
            "year":Year,
            "fquestions":fquestions,
            "pointer":xx,
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
    questionBan.chapter = request.POST.get('chapter', 0)
    questionBan.difficulty = request.POST.get('difficulty', 0)
    questionBan.marks = request.POST.get('marks', 0)
    questionBan.unit = request.POST.get('unit',0)
    questionBan.sem = request.POST.get('sem', 0)
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
    chapter = request.POST.get('chapter')

    if year=='' and subname=='' and chapter=='':
        a = questionBank.objects.all()
    elif year=='' and subname=='':
        a = questionBank.objects.filter(chapter=chapter)
    elif subname=='' and chapter=='':
        a = questionBank.objects.filter(year=year)
    elif year=='' and chapter=='':
        a = questionBank.objects.filter(subname=subname)
    elif chapter=='':
        a = questionBank.objects.filter(year=year, subname=subname)
    elif year=='':
        a = questionBank.objects.filter(subname=subname, chapter=chapter)
    elif subname=='L':
        a = questionBank.objects.filter(year=year, chapter=chapter)
    else:
        a = questionBank.objects.filter(year=year, subname=subname, chapter=chapter)

    print(a)
    params = {"a":a, "subname":subname, "year": year, "chapter":chapter}
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
#     chapterstoinclude = request.POST.get('chapter')
#     marks = request.POST.get('marks')
#     time = request.POST.get('time')
#     totalQuestions = request.POST.get('ques')
#     return render(request, 'generatePaper2.html')
    
