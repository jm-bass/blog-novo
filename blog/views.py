from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Blog, Mensagem

def index(request):
    context = {
        "posts" : Post.objects.all(),
        "blog" : Blog.objects.first(),
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post" : Post.objects.get(pk=post_id),
        "blog" : Blog.objects.first(),

    }
    return render(request, "post.html", context)

def sobre(request):
    context = {
        "blog" : Blog.objects.first(),
    }
    return render(request, "sobre.html", context)

def contato(request):
    context = {
            "blog" : Blog.objects.first(),
    }

    if request.method == "POST":
        print(request.POST['nome'])
        print(request.POST['email'])
        print(request.POST['telefone'])
        print(request.POST['cidade'])
        print(request.POST['mensagem'])


        context['erro'] = {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['mensagem']:
            context['erro']['mensagem'] = True
        if context['erro']:
            return render(request, "contato.html", context)


        mensagem = Mensagem(nome=request.POST['nome'],
                            email = request.POST['email'],
                            telefone = request.POST['telefone'],
                            cidade = request.POST['cidade'],
                            mensagem = request.POST['mensagem']
                            )
        mensagem.save()

        return render(request, "contato.html", context)

    else:
        return render(request, "contato.html", context)

def mensagem(request):
    context = {
        "mensagem" : Mensagem.objects.all(),
        "blog" : Blog.objects.first(),
    }
    return render(request, "mensagem.html", context)

def editar_mensagem(request, mensagem_id):
    context = {
        "blog" : Blog.objects.first(),
        "mensagem" : Mensagem.objects.get(pk=mensagem_id),
    }

    if request.method == "POST":
        print(request.POST['nome'])
        print(request.POST['email'])
        print(request.POST['telefone'])
        print(request.POST['cidade'])
        print(request.POST['mensagem'])


        context['erro'] = {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['mensagem']:
            context['erro']['mensagem'] = True
        if context['erro']:
            return render(request, "editar_mensagem.html", context)
        
        mensagem = context["mensagem"]
        mensagem.nome = request.POST["nome"]
        mensagem.email = request.POST["email"]
        mensagem.telefone = request.POST["telefone"]
        mensagem.cidade = request.POST["cidade"]
        mensagem.mensagem = request.POST["mensagem"]
        mensagem.save()

    return render(request, "editar_mensagem.html", context)

def deletar_mensagem(request, mensagem_id):
    context = {
        "blog" : Blog.objects.first(),
        "mensagem" : Mensagem.objects.get(pk=mensagem_id),
    }

    if request.method=="POST":
        context["mensagem"].delete()
        return redirect('mensagem')
    else:
        return render(request, "deletar_mensagem.html", context)