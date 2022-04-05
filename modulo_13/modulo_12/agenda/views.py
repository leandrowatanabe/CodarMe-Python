from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from datetime import date

from agenda.models import Evento, Categoria


# Create your views here.
def listar_eventos(request):    
    
    eventos = Evento.objects.exclude(data__lt = date.today())

    return render(
        request=request,
        context={"eventos":eventos},
        template_name="agenda/listar_eventos.html"
    )
 
def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento = Evento.objects.get(id=id)
    # template = loader.get_template("agenda/exibir_evento.html")
    # rendered_template = template.render(context={"evento":evento}, request=request)
    # return HttpResponse(rendered_template)

    return render(
        request=request,
        context={"evento":evento},
        template_name="agenda/exibir_evento.html"
    )

def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))

def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request=request,
        context={"categorias":categorias},
        template_name="agenda/listar_categorias.html"
    )

def exibir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria = Categoria.objects.get(id=id)
    # template = loader.get_template("agenda/exibir_evento.html")
    # rendered_template = template.render(context={"evento":evento}, request=request)
    # return HttpResponse(rendered_template)

    return render(
        request=request,
        context={"categoria":categoria},
        template_name="agenda/exibir_categoria.html"
    )