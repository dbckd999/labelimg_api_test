from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel
from .forms import UploadFileForm, TestForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        mymodel = MyModel()
        form = UploadFileForm(request.POST, request.FILES, instance=mymodel)
        if form.is_valid():
            form.save()
            print('saved')
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})

    # if request.method == 'POST':
    #     form = TestForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         print('saved')

    # form = TestForm()
    # return render(request, 'index.html', {'form': form})
