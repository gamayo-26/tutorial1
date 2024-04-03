from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

'''Este archivo se utiliza para definir las vistas de la aplicacion.
se creara una clase que hereda de View y se sebreescribira el metodo get
para que retorne la respuesta http, el nombre de la plantilla que se 
quiere mostrar y el contexto que se le quiere pasar a la plantilla'''

# Creamos una vista para la agina de los blogs
class BlogListView(View):
    def get(self, request, *args, **kwargs):

        # obtenemos los distintos post que hay en la base de datos
        posts = Post.objects.all()
        context = {
            # pasamos los post al contexto para mostrarlo luego en 
            # la plantilla html
            'posts':posts

        }

        return render(request, 'blog_list.html', context)
    
# creamos una nueva vista para crear post
class BlogCreateView(View):

    '''sobrescribimos el metodo get para que retorne el formulario
    que creamos en forms.py y lo pase como contexto a la plantilla
    para que se muestre en la pagina web.'''
    def get(self, request, *args, **kwargs):
        # referenciamos al formulario que creamos
        form=PostCreateForm()
        #creamos un contexto 
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)
    
    '''sobrescribimos el metodo post para que cuando se envie el
    formulario, se cree un nuevo objeto en la base de datos con los
    datos que se enviaron en el formulario.'''
    def post(self, request, *args,**kwargs):
        if request.method=='POST':
            # creamos un objeto del formulario con los datos que se enviaron
            form = PostCreateForm(request.POST)
            # comprobamos si el formulario es valido
            if form.is_valid():
                # obtenemos los datos del formulario que se enviaron
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                # con los datos que se obtuvieron, creamos un nuevo objeto

                p, created = Post.objects.get_or_create(title=title, content=content)
                # guardamos el objeto en la base de datos
                p.save()
                # redirigimos a la pagina de inicio
                # pasamos al redirect el nombre de la url a la que queremos redirigir
                return redirect('blog:home')
        context={

        }
        return render(request, 'blog_create.html', context)

# creamos una vista para ver los detalles de un post
class BlogDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        # obtenemos el post correspondiente al id (pk) proporcionado
        post = get_object_or_404(Post, pk=pk)
        context={
            # pasamos el post al contexto para mostrarlo en la plantilla html
            'post':post
        }
        # renderizamos la plantilla 'blog_detail.html' con el contexto proporcionado
        return render(request, 'blog_detail.html', context)
    
class BlogUpdateView(UpdateView):
    # indicamos en que modelo se va a hacer la actualizacion
    model = Post
    # indicamos que campos se van a actualizar
    fields =  [
        'title',
        'content',
    ]
    # indicamos el nombre de la plantilla que se va a utilizar
    template_name = 'blog_update.html'

    # indicamos el nombre de la url a la que se va a redirigir
    # una vez que se haya actualizado el post
    def get_success_url(self):
        # Obtenemos el valor de 'pk' de los argumentos de la vista
        pk = self.kwargs['pk']
        # Creamos la URL de redirección utilizando el valor de 'pk' en los argumentos de la vista
        return reverse_lazy('blog:detail', kwargs={'pk':pk})
    
class BlogDeleteView(DeleteView):
    model = Post

    # indicamos el nombre de la plantilla que se va a utilizar
    template_name = 'blog_delete.html'

    # indicamos la url a la que se va a redirigir una vez que se haya eliminado el post
    success_url = reverse_lazy('blog:home')