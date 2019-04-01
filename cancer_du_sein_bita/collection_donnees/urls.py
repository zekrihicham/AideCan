from django.urls import path , include
from django.conf.urls import url



from django.conf.urls.static import static
from django.conf import settings
from collection_donnees import views
from django.contrib.auth import views  as auth_views


urlpatterns = [
    path('',views.first_page,name='first_page'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('error/',views.Error,name='error'),
    path('activate/<str:uidb64>/<str:token>/<int:id>',views.activate,name='activate'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:id>/random_labeling',views.label_view,name='label_view'),
    path('<int:id>/add_label',views.add_mammo_and_label_view,name="add_mammo_and_label_view"),
    path('<int:id>/show_label/<int:id_label>',views.show_label,name='show_label'),
    path('<int:id>/profile', views.profile_view, name='profile'),
    path('<int:id>/profile/password', views.change_password, name='change_password'),

    path('random_labeling/<int:id>/r',views.valid,name="valid")
        #TODO:: all project paths here

]