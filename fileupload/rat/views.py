from django.shortcuts import render
from django.http import HttpResponse
from fileupload.settings import MEDIA_ROOT
import json

def index(request):
    render('home.html')


def handle_uploaded_file(f, dest_path):
    with open(dest_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def import_allocation_data(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            _file = request.FILES['file']
            filename = _file.name
            handle_uploaded_file(_file, "{}/{}".format(MEDIA_ROOT, filename))
            # return HttpResponse(content={}, status=200, content_type='application/json')
            rlist = [['Jack', 'Chinese'], ['Mike', 'English'], ['Bob', 'Math'], ['Frank', 'Art'], ['Lucy', 'Music']]
            rjson = json.dumps(rlist)
            response = HttpResponse()
            response['Content-Type'] = "text/javascript"
            response.write(rjson)
            return response