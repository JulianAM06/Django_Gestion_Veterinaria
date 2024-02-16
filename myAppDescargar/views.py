from django.shortcuts import render

from django.http.response import HttpResponse
import mimetypes
import os

def archivo(request):
    return render(request, 'archivo2.html')

def descargar(request): 

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

    filename = 'formularioAdopciones.pdf'

    filepath = BASE_DIR + '/myAppDescargar/archivos/' + filename 

    path = open(filepath, 'rb') 

    mime_type, _ = mimetypes.guess_type(filepath)
    
    response = HttpResponse(path, content_type = mime_type)

    response['Content-Disposition'] = f"attachment; filename={filename}"

    return response 