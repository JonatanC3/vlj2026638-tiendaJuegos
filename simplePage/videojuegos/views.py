from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from .models import Videogame, Order
from .forms import VideogameForm, OrderForm

def is_staff(user):
    return user.is_staff

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False  # Ensure new users are not staff by default
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def videogame_list(request):
    videogames = Videogame.objects.all()  # Show all games to all users
    return render(request, 'videogames/videogame_list.html', {'videogames': videogames})

@login_required
def videogame_create(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = VideogameForm(request.POST)
        if form.is_valid():
            videogame = form.save(commit=False)
            videogame.admin = request.user
            videogame.save()
            messages.success(request, 'VideoJuego Creado!')
            return redirect('videogame_list')
        else:
            messages.error(request, 'Por favor, corrija los errores anteriores.')
    else:
        form = VideogameForm()
    return render(request, 'videogames/videogame_form.html', {'form': form})

@user_passes_test(is_staff)
@login_required
def videogame_update(request, pk):
    videogame = get_object_or_404(Videogame, pk=pk)
    if request.method == 'POST':
        form = VideogameForm(request.POST, instance=videogame)
        if form.is_valid():
            form.save()
            return redirect('videogame_list')
    else:
        form = VideogameForm(instance=videogame)
    return render(request, 'videogames/videogame_form.html', {'form': form})

@user_passes_test(is_staff)
@login_required
def videogame_delete(request, pk):
    videogame = get_object_or_404(Videogame, pk=pk)
    if request.method == 'POST':
        videogame.delete()
        return redirect('videogame_list')
    return render(request, 'videogames/videogame_confirm_delete.html', {'videogame': videogame})

@require_http_methods(["GET", "POST"])
def custom_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    carousel_images = [
        'https://content.api.news/v3/images/bin/498b7272b1fbb3933fd78564abb03125',
        'https://images.nintendolife.com/c53e532e0ae06/pokemon.original.jpg',
        'https://wallpapercave.com/wp/wp4705310.jpg',
    ]
    return render(request, 'home.html', {'carousel_images': carousel_images})

@login_required
def create_order(request, videogame_id):
    videogame = get_object_or_404(Videogame, pk=videogame_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.videogame = videogame
            order.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'videogames/create_order.html', {'form': form, 'videogame': videogame})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, 'videogames/order_detail.html', {'order': order})

@login_required
def videogame_detail(request, pk):
    videogame = get_object_or_404(Videogame, pk=pk)
    return render(request, 'videogames/videogame_detail.html', {'videogame': videogame})

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'videogames/user_orders.html', {'orders': orders})
