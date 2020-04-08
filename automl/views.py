from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from howdoi import howdoi

# Create your views here.
@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/')
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("파일 업로드 성공")
    else:
        form = UploadFileForm()
    return render(request, 'fileupload.html', {'form': form})

@login_required(login_url='/')
def chart(request):
    return render(request, 'chart.html')

@login_required(login_url='/')
def table(request):
    return render(request, 'responsivetable.html')


@login_required(login_url='/')
def howdoi_view(request):
    if request.method == 'POST':
        query = request.POST['query']
        parser = howdoi.get_parser()
        args = vars(parser.parse_args(query.split(' ')))


        print(args)
        print(type(args))
        output = howdoi.howdoi(args)
        
        context = {"output": output}
        return render(request, 'howdoi_view.html',context)
    return render(request, 'howdoi_view.html')
    
        
    # return render(request, 'howdoi_view.html', {'form': form})