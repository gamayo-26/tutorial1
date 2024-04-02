from django.urls import path
from .views import (BlogListView, BlogCreateView, BlogDetailView, 
                    BlogUpdateView, BlogDeleteView)


'''archivo que se utiliza para definir las urls de la aplicacion.
Se importa la vista que se va a utilizar y 
se define la url que se va a utilizar para acceder a esta vista.'''

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    
    path('create/', BlogCreateView.as_view(), name='create'),

    # indicamos que la url va a recibir un parametro que va a ser el id del post
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),

    # path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),    
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),

    path('<int:pk>/delete/', BlogDeleteView.as_view(), name= 'delete')
]
