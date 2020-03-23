import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import jinja2
from .devicetester import *
from django.contrib import messages
from uploadapp.models import studenttable, attendancetable
from viewattendance.models import Classroom, Course, Attendance, Student
global url
global statlist

def condformat(row):
    color = 'background-color: {}'.format('green' if row.Status == 'P' else 'red')
    return (color, color)


def uploadhome(request):
    if request.method == 'POST':
        if not test_device():
            messages.info(request, 'The device is not connected')
            return HttpResponseRedirect('/upload/')
        try:
            global classname
            classname = request.POST['class']
            global date
            date = request.POST['date']
            global hour
            hour = request.POST['hour']
            global course
            course = request.POST['course']
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
        # fs = FileSystemStorage()
        # name = fs.save(uploaded_file.name, uploaded_file)
        # todo capure data store in media and read

        global url
        url = "./media/out.csv"
        df = pd.read_csv(url, names=["UID"], header=None)
        classid = Classroom.objects.get(class_id=classname)
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
        context = {'loaded_data': s.render(), 'button': True}
        return render(request, 'showupload.html', context)
    context = {}
    context['classoptions'] = [str(elem[0]) for elem in list(Classroom.objects.all().values_list('class_id'))]
    context['courseoptions'] = [str(elem[0]) for elem in list(Course.objects.all().values_list('course_id'))]
    return render(request, 'index.html', context)


def result(request):
    df = pd.read_csv(url, names=["UID"], header=None)
    #  print(classname, date, hour, course)
    # todo student class validation course validation , date+hour entry check
    try:
        classid = Classroom.objects.get(class_id=classname)
        for ind in df.index:
            # studenttable.objects.filter(sid=str(df['UID'][ind])).update(status=df['Status'][ind])
            # obj = Student.objects.filter(roll_no=str(df['UID'][ind])).filter(class_id=classname)
            #  print(str(df['UID'][ind]))
            print("executed")
            obj = Student.objects.get(roll_no=df['UID'][ind], class_id=classid)
    except Exception as e:
        print(e)
        return render(request, 'resultpage.html', {'error': True})
    cobj = Course.objects.get(course_id=course)
    classobj = Classroom.objects.get(class_id=classname)
    dmy = date.split('/')
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
                                         date=datestring, class_id=classobj, hour=hour,
                                         status=stat)
    return render(request, 'resultpage.html', {'success': True})


def clear(request):
    studenttable.objects.update(status='A')
    return render(request, 'resultpage.html', {'success': True})


def testdevice(request):
    if test_device():
        messages.info(request, 'The device is connected')
        return HttpResponseRedirect('/upload/')
    messages.info(request, 'The device is not connected')
    return HttpResponseRedirect('/upload/')
