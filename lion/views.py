from django.shortcuts import render

# Create your views here.
def pagina_inicial(request):
    context = {
    "nome":"deniza", "obede", ""}
    return render(request, 'index.html', context)



