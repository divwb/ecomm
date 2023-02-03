from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from django.contrib.auth import views as auth_view
from .forms import MyPasswordResetForm,LoginForm,MypasswordChangeForm

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
    path('category-name/<val>', views.CategoryName.as_view(), name="category-name"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(),name="product-detail"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    path('orders/',views.orders,name='orders'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('orders',views.orders,name='orders'),

    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),

                  #  login authentication

    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),

    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MypasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),

    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),

    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    path('password-reset',auth_view.PasswordResetView.as_view(template_name='passwordreset.html',form_class=MyPasswordResetForm),name='password_reset'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
