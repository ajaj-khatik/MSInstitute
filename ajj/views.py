from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm
# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Successfully')
            return render(request, 'index.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'index.html', {'form':form})
    return render(request, 'index.html', {'form':form})

