from django.shortcuts import render,redirect
from .models import  Tâche
from .forms import TaskForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()    
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)  
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')          
            return redirect('index')
    else :
        form = UserForm()
    return render(request,'register.html',{'form' : form}) 
def login(request,user):
    error = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = UserForm()

    return render(request, 'login.html', locals())

@login_required
def index(request):
    context ={
	'taches': Tâche.objects.filter(userpk=request.user)
	}
    return render(request, 'index.html',context)


# def index(request):
#     form = TaskForm()
#     #vérifier la méthode HTTP
#     if request.method == "POST":
#         #instancier le formulaire avec les données
#         form = TaskForm(request.POST)
#         #tester la validité du formulaire
#         if form.is_valid():
#             #enregister les données
#             form.save()
#             #rediriger vers l'URL "index"
#             return redirect("index")
#     tasks =  Tâche.objects.all()
#     return render(request, "index.html",{"tasks": tasks,"task_form": form})
# def index2(request):
#     if request.method == "POST":
#         #instancier le formulaire avec les données
#         form = TaskForm(request.POST)
#         #tester la validité du formulaire
#         if form.is_valid():
#             form.save()
#             userpk = form.cleaned_data["username"]
#             user = authenticate(username=userpk)
#             #enregister les données
#             if user:
#                 tasks =  Tâche.objects.get(userpk=user)
#             else:    
#             #rediriger vers l'URL "index"
#                 return redirect("index")
#     # tasks =  Tâche.objects.get(userpk= user)
#     return render(request, "index2.html")    
def ajoutertache(request):
    form =TaskForm()
    # insertion
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form': form}
    return render(request, 'ajoutertache.html', context) 
def connexion(request):
    return render(request,'connexion.html')

def utilisateur(request):
    form = UserForm()
    # insertion
    if request.method=='POST':
        formUser = UserForm(request.POST)
        if formUser.is_valid():
            formUser.save()
    context={'form': form}
    return render(request, 'inscription.html', context)  

def update(request, pk):
	task = Tâche.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect("index")
	return render(request, "update.html", {"edit_task_form": form})
def delete(request, pk):
	task = Tâche.objects.get(id=pk)
	if request.method == "POST":
		task.delete()
		return redirect("index")
	return render(request,"delete.html",{"task":task})






    
    
    
    
    
    
        
    
            
        
            
        
                
	        
                            
            

         
    

# Create your views here.
