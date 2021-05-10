from django.shortcuts import render
import sys
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            original_stdout = sys.stdout 
            sys.stdout = open('file.txt','w')
            
            
            exec(codeareadata)
            
            sys.stdout.close() 
            sys.stdout = original_stdout 
            print("H1")
            print("j2)")

            output = open('file.txt','r').read()

        except Exception as e:
            sys.stdout = original_stdout 
            output = e
    return render(request,'testapp/index.html', {'code':codeareadata, 'output':output})
