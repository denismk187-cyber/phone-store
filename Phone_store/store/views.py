from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Cart

def home(request):
    category = request.GET.get('category')
    search = request.GET.get('search')
    products = Product.objects.filter(is_available=True)
    
    if category:
        products = products.filter(category=category)
    
    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__icontains=search)
        )

    # 💰 Convert USD to KSh
    exchange_rate = 130  # you can adjust based on current rate
    for product in products:
        product.price_ksh = product.price * exchange_rate

    categories = Product.CATEGORY_CHOICES
    
    context = {
        "products": products,
        "categories": categories,
        "current_category": category,
        "search_query": search
    }
    return render(request, "store/home.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # convert price to KSh for display (keep price in DB as base currency)
    exchange_rate = 130
    product.price_ksh = product.price * exchange_rate
    return render(request, "store/product_detail.html", {"product": product})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username} 🚀")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password ❌")
            return redirect("login")

    return render(request, "store/login.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to Phone Store, {user.username}! 🎉")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully 👋")
    return redirect("home")

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, f"{product.name} added to cart! 🛒")
    return redirect('product_detail', pk=product_id)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart! ✨")
    return redirect('cart')
