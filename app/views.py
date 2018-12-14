from django.shortcuts import render, redirect
from django.http import HttpResponse
from .post import post
from django.contrib.auth.models import User
from .models import Post, Tipo
from .forms import TipoForm

def inicio (request):

	post1, post2, post3 = post()


	ids = []
	try : 
		usuario = User.objects.get(username = post3)
	except User.DoesNotExist : 
		usuario = User.objects.create_user(username = post3 , password = 'romerobrito')
		usuario.save()

	for i in range(len(post1)):
		try:
			publicacao = Post.objects.get(id_publicacao=post1[i]['id'])
		except:
			publicacao = Post()
			publicacao.id_publicacao = post1[i]['id']
			publicacao.mensagem = post1[i]['message']
			publicacao.user = usuario
			publicacao.save()
			ids.append(publicacao.id_publicacao)

	categorias = []
	for l in Tipo.objects.exclude(tipo='Sem categoria'):
		categorias.append(l)

	contador = 0
	for m in ids:
		publicacao = Post.objects.get(id_publicacao=m)
		print(not(publicacao.tipo.all()))
		for k in range(len(categorias)):
			for n in categorias[k].palavras_chaves.split(','):
				if n in publicacao.mensagem:
					print(categorias[k])
					publicacao.tipo.add(categorias[k])
					publicacao.save()

		if not(publicacao.tipo.all()):
			publicacao.tipo.add(Tipo.objects.get(tipo='Sem categoria'))
			publicacao.save()


	pub = Post.objects.filter(user=usuario)

	return render(request, 'app/home.html', {'pub': pub})