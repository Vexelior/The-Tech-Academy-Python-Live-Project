from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.itemsApp_home, name="itemsApp_home"),
    path('new_item/', views.new_item, name="new_item"),
    path('details/', views.select_item, name="select_item"),
    path('<int:pk>/details/', views.item_details, name="item_details"),
    path('<int:pk>/edit_form/', views.edit_form, name="edit_items"),
    path('edit_item/', views.edit_page, name="edit_page"),
    path('details/<int:pk>/delete/', views.delete_item, name="delete_item"),
    path('api/', views.api, name="api"),
    path('scrape/', views.books_scraped, name="book_scrape"),
    path('login_modal/', views.login_modal, name="itemsApp_login_modal"),
    path('create_account/', views.register, name='create_account'),
    path('login/', LoginView.as_view(), name="itemsApp_login"),
    path('logout/', views.logout_account, name="itemsApp_logout"),
    path('favorites/', views.show_favorites, name="itemsApp_favorites"),
    path('favorites/remove_favorite/', views.remove_favorite, name='itemsApp_remove_favorite'),
]

