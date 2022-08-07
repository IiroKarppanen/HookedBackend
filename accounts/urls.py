from django.urls import path
from . views import RegisterView, LoginView, UserView, LogoutView, WatchlistAddView, WatchlistDeleteView, UpdateAccountName, UpdateAccountPassword


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('watchlist/add', WatchlistAddView.as_view()),
    path('watchlist/delete', WatchlistDeleteView.as_view()),
    path('updateName', UpdateAccountName.as_view()),
    path('updatePassword', UpdateAccountPassword.as_view())

]


