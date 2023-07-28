from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=mymodel)
        if form.is_valid():
            form.save()
            print('saved')
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})
