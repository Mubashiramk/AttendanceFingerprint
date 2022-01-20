import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import jinja2
from .devicetester import *
from django.contrib import messages
from uploadapp.models import studenttable
from viewattendance.models import Classroom, Course, Attendance, Student

global statlist
global context


def condformat(row):
    color = 'background-color: {}'.format('green' if row.Status == 'P' else 'red')
    return (color, color)


def uploadhome(request):
    if not test_device():
        return render(request, "laucherror.html")
    if request.method == 'POST':
        try:
            global context
            classname = request.POST['class']
            context['classname'] = classname
            date = request.POST['date']
            context['date'] = date
            hour = request.POST['hour']
            context['hour'] = hour
            course = request.POST['course'].split(" - ")[0]
            context['course'] = course
            # uploaded_file = request.FILES['document']
            if classname == "" or date == "" or hour == "" or course == "":
                context = {}
                context['classoptions'] = [str(elem[0]) for elem in
                                           list(Classroom.objects.all().values_list('class_id'))]
                context['courseoptions'] = [str(elem[0]) for elem in
                                            list(Course.objects.all().values_list('course_id'))]
                context['error'] = True
                return render(request, 'index.html', context)
        except:
            context = {}
            context['classoptions'] = [str(elem[0]) for elem in list(Classroom.objects.all().values_list('class_id'))]
            context['courseoptions'] = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_id'))]
            context['error'] = True
            return render(request, 'index.html', context)
        return redirect('/upload/waiting/')
    context = {}

    context['classoptions'] = [str(elem[0]) for elem in list(Classroom.objects.all().values_list('class_id'))]
    courseids = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_id'))]
    coursenames = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_name'))]
    courseoptions = []
    for i in range(len(courseids)):
        courseoptions.append(courseids[i]+" - "+coursenames[i])
    context['courseoptions'] = courseoptions
    return render(request, 'index.html', context)


def show(request):
    url = "./media/out.csv"
    df = pd.read_csv(url, names=["UID"], header=None)
    classid = Classroom.objects.get(class_id=context['classname'])
    absentadd = Student.objects.filter(class_id=classid)
    df = df.drop_duplicates(subset=["UID"], keep='first')
    l = [int(x) for x in df['UID']]
    global statlist
    statlist = ['P' for elem in df['UID']]
    df['Status'] = statlist
    for elem in absentadd:
        if elem.roll_no not in l:
            df = df.append({'UID': elem.roll_no, 'Status': 'A'}, ignore_index=True)

    s = df.style.apply(condformat, axis=1).hide_index().set_properties(**{'text-align': 'center',
                                                                          'border-color': 'Black',
                                                                          'border-width': 'thin',
                                                                          'border-style': 'dotted'})
    context['loaded_data'] = s.render()
    context['button'] = True
    return render(request, 'showupload.html', context)


def result(request):
    url = "./media/out.csv"
    df = pd.read_csv(url, names=["UID"], header=None)
    #  print(classname, date, hour, course)
    # todo student class validation course validation , date+hour entry check
    try:
        classid = Classroom.objects.get(class_id=context['classname'])
        for ind in df.index:
            # studenttable.objects.filter(sid=str(df['UID'][ind])).update(status=df['Status'][ind])
            # obj = Student.objects.filter(roll_no=str(df['UID'][ind])).filter(class_id=classname)
            #  print(str(df['UID'][ind]))
            obj = Student.objects.get(roll_no=df['UID'][ind], class_id=classid)
    except Exception as e:
        print(e)
        return render(request, 'resultpage.html', {'error': True})
    cobj = Course.objects.get(course_id=context['course'])
    classobj = Classroom.objects.get(class_id=context['classname'])
    dmy = context['date'].split('/')
    datestring = dmy[2]+"-"+dmy[1]+"-"+dmy[0]
    absentadd = Student.objects.filter(class_id=classid)
    l = [int(x) for x in df['UID']]
    df['Status'] = statlist
    for elem in absentadd:
        if elem.roll_no not in l:
            df = df.append({'UID': elem.roll_no, 'Status': 'A'}, ignore_index=True)
    for ind in df.index:
        if df['Status'][ind] == 'P':
            stat = 'Present'
        elif df['Status'][ind] == 'A':
            stat = 'Absent'
        else:
            stat = '-'
        sobj = Student.objects.get(roll_no=df['UID'][ind], class_id=classid)
        inst = Attendance.objects.create(student_id=sobj, course_id=cobj,
                                         date=datestring, class_id=classobj, hour=context['hour'],
                                         status=stat)
    return render(request, 'resultpage.html', {'success': True})


def clear(request):
    studenttable.objects.update(status='A')
    return render(request, 'resultpage.html', {'success': True})


def waitscreen(request):
    if not test_device():
        return render(request, "laucherror.html")
    return render(request, 'waitpress.html', {})


def upload(request):
    use_device()
    return redirect('/upload/show/')
