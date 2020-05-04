from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    """ 
    This function renders an indiviual listing after hitting listings/:listing_id,
    get_object_or_404 is a django shortcut that is imported at the top. https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
    """
    listing = get_object_or_404(Listing, pk=listing_id)
    print(f"listing: {listing.photos_main.url}")
    context = {
        'listing': listing

    }  


    return render(request, 'listings/listing.html', context)

def search(request):
    print(f"\nrequest: {request} \n")
    queryset_list = Listing.objects.order_by('-list_date')
    print("queryset_list (ABOVE)" ,queryset_list)
    # keyword 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    print("queryset_list (BELOW)" ,queryset_list)
    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }

    return render(request, 'listings/search.html', context)