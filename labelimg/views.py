from django.http import HttpResponse
from .forms import UploadFileForm
from .models import MyModel
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=MyModel())
        if form.is_valid():
            form.save()
            print('saved')

    return HttpResponse()
