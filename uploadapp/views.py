import pandas as pd
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import jinja2
from uploadapp.models import studenttable


def condformat(row):
    color = 'background-color: {}'.format('green' if row.Status == 'P' else 'red')
    return (color, color)


def uploadhome(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
        except:
            return render(request, 'uploadhome.html', {'error': True})
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        global url
        url = "." + fs.url(name)
        df = pd.read_csv(url)
        s = df.style.apply(condformat, axis=1).hide_index().set_properties(**{'text-align': 'center',
                                                                              'border-color': 'Black',
                                                                              'border-width': 'thin',
                                                                              'border-style': 'dotted'})
        context = {'loaded_data': s.render(), 'button': True}
        return render(request, 'showupload.html', context)
    return render(request, 'uploadhome.html')


def result(request):
    df = pd.read_csv(url)
    try:
        for ind in df.index:
            # studenttable.objects.filter(sid=str(df['UID'][ind])).update(status=df['Status'][ind])
            obj = studenttable.objects.get(sid=str(df['UID'][ind]))
            obj.status = str(df['Status'][ind])
            obj.save()
    except:
        return render(request, 'resultpage.html', {'error': True})
    return render(request, 'resultpage.html', {'success': True})


def clear(request):
    studenttable.objects.update(status='-')
    return render(request, 'resultpage.html', {'success': True})