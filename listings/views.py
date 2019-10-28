from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, state_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paginated_listings = paginator.get_page(page)

    context = \
        {
            'listings': paginated_listings,
        }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = \
        {
            'listing': listing
        }

    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        search_params= request.GET['state']
        if search_params:
            queryset_list = queryset_list.filter(state__iexact=search_params)

    if 'bedrooms' in request.GET:
        # returns results UP TO the searched number of bedrooms
        # because people are searching for what they can afford
        search_params= request.GET['bedrooms']
        if search_params:
            queryset_list = queryset_list.filter(bedrooms__lte=search_params)

    if 'price' in request.GET:
        search_params= request.GET['price']
        if search_params:
            queryset_list = queryset_list.filter(price__lte=search_params)


    context = \
        {
            'price_choices': price_choices,
            'state_choices': state_choices,
            'bedroom_choices': bedroom_choices,
            'listings': queryset_list,
            'values': request.GET
        }

    return render(request, 'listings/search.html', context)