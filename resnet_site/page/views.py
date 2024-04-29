from django.shortcuts import render
from .forms import UploadFileForm
from .classify import classify

# Create your views here.
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            category = classify(form.cleaned_data['file'])
            return render(request, "success.html", {"form": form, 'category': category})
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
