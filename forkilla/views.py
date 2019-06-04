from django.db.models import Q
from django.shortcuts import render, reverse

from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Restaurant, ViewedRestaurants, RestaurantInsertDate, Reservation, Review
from .forms import ReservationForm, ReviewForm
from datetime import datetime

# Restful
from rest_framework import viewsets, permissions
from .serializers import RestaurantSerializer


@login_required
def add_comment(request, restaurant_number=""):
    restaurant = Restaurant.objects.get(restaurant_number=restaurant_number)
    if request.method == "POST":

        comment = request.POST['comment']
        ratio = request.POST['ratio']
        user = request.user

        review = Review()
        review.restaurant = restaurant
        review.user = user
        review.comment = comment
        review.ratio = ratio

        review.save()

    return details(request, restaurant_number)


def index(request):
    viewedrestaurants = _check_session(request)
    restaurants_by_city = Restaurant.objects.filter(is_promot="True")
    context = {
        'restaurants': restaurants_by_city,
        'viewedrestaurants': viewedrestaurants
    }

    return render(request, 'forkilla/home.html', context)


def restaurants(request, city="", category=""):
    viewedrestaurants = _check_session(request)
    promoted = False
    if city:
        if category:
            restaurants_by_city = Restaurant.objects.filter(city__iexact=city, category__iexact=category)
        else:
            restaurants_by_city = Restaurant.objects.filter(city__iexact=city).order_by('category')
    else:
        restaurants_by_city = Restaurant.objects.filter(is_promot="True")
        promoted = True

    context = {
        'city': city,
        'category': category,
        'restaurants': restaurants_by_city,
        'promoted': promoted,
        'viewedrestaurants': viewedrestaurants
    }

    return render(request, 'forkilla/restaurants.html', context)


def details(request, restaurant_number):
    try:
        viewedrestaurants = _check_session(request)
        restaurant = Restaurant.objects.get(restaurant_number=restaurant_number)
        lastviewed = RestaurantInsertDate(viewedrestaurants=viewedrestaurants, restaurant=restaurant)
        lastviewed.save()

        form = ReviewForm()

        reviews = Review.objects.filter(restaurant=restaurant)
        if reviews:
            print("there's a review")
            context = {
                'restaurant': restaurant,
                'viewedrestaurants': viewedrestaurants,
                'reviews': reviews,
                'form': form
            }
        else:
            print("No review")
            context = {
                'restaurant': restaurant,
                'viewedrestaurants': viewedrestaurants,
                'form': form
            }

    except Restaurant.DoesNotExist:
        return handler404(request)

    return render(request, 'forkilla/details.html', context)


@login_required
def reservation(request):
    try:
        if request.method == "POST":
            form = ReservationForm(request.POST)
            if form.is_valid():

                restaurant_number = request.session["reserved_restaurant"]
                restaurant = Restaurant.objects.get(restaurant_number=restaurant_number)
                user = request.user
                current_reservations = Reservation.objects.filter(restaurant=restaurant,
                                                                  time_slot=request.POST["time_slot"],
                                                                  day=request.POST["day"])

                reservations = sum([i.num_people for i in current_reservations])
                reservations += int(request.POST["num_people"]) # si falla el cast habria que mandar un 500

                if current_reservations:
                    if reservations > restaurant.capacity:
                        request.session["result"] = "Error"

                    else:
                        resv = form.save(commit=False)
                        resv.restaurant = restaurant
                        resv.user = user
                        resv.save()
                        request.session["reservation"] = resv.id
                        request.session["result"] = "OK"

                else:
                    resv = form.save(commit=False)
                    resv.restaurant = restaurant
                    resv.user = user
                    resv.save()
                    request.session["reservation"] = resv.id
                    request.session["result"] = "OK"

            else:
                request.session["result"] = form.errors

            return HttpResponseRedirect(reverse('checkout'))

        elif request.method == "GET":
            restaurant_number = request.GET["reservation"]
            restaurant = Restaurant.objects.get(restaurant_number=restaurant_number)
            request.session["reserved_restaurant"] = restaurant_number

            form = ReservationForm()

            viewedrestaurants = _check_session(request)
            context = {
                'restaurant': restaurant,
                'viewedrestaurants': viewedrestaurants,
                'form': form,
            }

    except Restaurant.DoesNotExist:
        return handler404(request)

    return render(request, 'forkilla/reservation.html', context)


def _check_session(request):
    if "viewedrestaurants" not in request.session:
        viewedrestaurants = ViewedRestaurants()
        viewedrestaurants.save()
        request.session["viewedrestaurants"] = viewedrestaurants.id_vr
    else:
        viewedrestaurants = ViewedRestaurants.objects.get(id_vr=request.session["viewedrestaurants"])
    return viewedrestaurants


def checkout(request):
    result = request.session["result"]

    restaurant_number = request.session["reserved_restaurant"]
    restaurant = Restaurant.objects.get(restaurant_number=restaurant_number)

    if result == "OK":
        current_reservation = Reservation.objects.get(id=request.session["reservation"])

        del request.session["reserved_restaurant"]
        del request.session["reservation"]
        del request.session["result"]

    else:
        current_reservation = None

    context = {
        'restaurant': restaurant,
        'reservation': current_reservation,
        'result': result
    }

    return render(request, 'forkilla/checkout.html', context)


@login_required
def reservation_list(request):
    user = request.user

    date = datetime.today()
    past_reservations = Reservation.objects.filter(user=user, day__lt=date).order_by("day", "time_slot")
    future_reservations = Reservation.objects.filter(user=user, day__gte=date).order_by("day", "time_slot")

    context = {
        'past_reservations': past_reservations,
        'future_reservations': future_reservations,
        'viewedrestaurants': _check_session(request)
    }

    return render(request, 'forkilla/my_reservations.html', context)


@login_required
def delete_reservation(request):
    reservation_id = request.GET['reservation_id']

    Reservation.objects.filter(id=reservation_id).delete()

    return HttpResponseRedirect(reverse('reservation_list'))


def search(request):

    query = request.GET.get('q', '')
    if query:
        found_restaurants = Restaurant.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query) |
            Q(category__icontains=query)
        ).distinct()

    else:
        found_restaurants = None
    context = {
        'restaurants': found_restaurants,
        'name': query,
        'viewedrestaurants': _check_session(request)
    }

    return render(request, 'forkilla/restaurants.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Restaurants to be viewed or edited.
    """
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        city = self.request.query_params.get('city', None)
        price_average = self.request.query_params.get('price_average', None)

        your_values = {'category': category, 'city': city}
        arguments = {}
        for k, v in your_values.items():
            if v:
                arguments[k] = v

        queryset = Restaurant.objects.filter(**arguments)

        if price_average:
            queryset = queryset.exclude(price_average__gt=price_average)

        return queryset


def handler404(request):
    response = render(request, 'forkilla/404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render(request,'forkilla/500.html', {})
    response.status_code = 500
    return response
