# from django.contrib import admin
# from django.urls import path,include
# from employee import views 
# from django.shortcuts import redirect # Import your views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', lambda request: redirect('/emp')),
#     path('', views.home, name='home'), 
#     # path('', views.home, name='home'),  # Ensure this exists
#     path('emp', views.emp, name='emp'),
#     path('show', views.show, name='show'),
#     path('edit/<int:id>', views.edit, name='edit'),
#     path('update/<int:id>', views.update, name='update'),
#     path('delete/<int:id>', views.destroy, name='delete'),
#     # path('', views.home, name='home'),  # Ensure `home` exists in `employee/views.py`
#     # path('employee/', include('employee.urls')),
# ]
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Use home as the main page
    path('emp/', views.emp, name='emp'),  # Add trailing slashes consistently
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.destroy, name='delete'),
]

