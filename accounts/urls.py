from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('signout/', views.signout_view, name='signout'),
    path('donate/', views.donate_view, name='donate'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('donate-success/', views.donate_success, name='donate_success'),
    path('donate-cancel/', views.donate_cancel, name='donate_cancel'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', views.profile_view, name='profile'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),

]