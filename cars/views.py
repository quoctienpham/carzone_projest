from django.shortcuts import render, get_object_or_404
from  .models import  Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
	cars = Car.objects.order_by('-created_date')

	paginator = Paginator(cars, 4)
	page = request.GET.get('page')
	paged_cars = paginator.get_page(page)

	search_fields = Car.objects.values('brand', 'model', 'city', 'year', 'body_style')
	unique_brands = list(set(brand['brand'] for brand in search_fields ))

	# brand_search = Car.objects.values_list('brand', flat=True).distinct()
	model_search = Car.objects.values_list('model', flat=True).distinct()
	city_search = Car.objects.values_list('city', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct()
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

	data = {
		'cars' : paged_cars,
		'search_fields' : search_fields,
		'unique_brands' : unique_brands,
		# 'brand_search' : brand_search,
		'model_search' : model_search,
		'city_search' : city_search,
		'year_search' : year_search,
		'body_style_search' : body_style_search,
	}

	return render(request, 'cars/cars.html', data)

def cars_detail(request, id):
	single_car = get_object_or_404(Car, pk=id)
	data = {
	'single_car' : single_car
	}

	return render(request, 'cars/cars_detail.html', data)

def search(request):
	cars = Car.objects.order_by('-created_date')

	search_fields = Car.objects.values('brand', 'model', 'city', 'year', 'body_style')
	unique_brands = list(set(brand['brand'] for brand in search_fields ))

	# brand_search = Car.objects.values_list('brand', flat=True).distinct()
	model_search = Car.objects.values_list('model', flat=True).distinct()
	city_search = Car.objects.values_list('city', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct()
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			cars  = cars.filter(description__icontains=keyword)

	if 'brand' in request.GET:
		brand = request.GET['brand']
		if brand:
			cars  = cars.filter(brand__iexact=brand)

	if 'model' in request.GET:
		model = request.GET['model']
		if model:
			cars  = cars.filter(model__iexact=model)

	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			cars  = cars.filter(city__iexact=city)

	if 'year' in request.GET:
		year = request.GET['year']
		if year:
			cars  = cars.filter(year__iexact=year)

	if 'body_style' in request.GET:
		body_style = request.GET['body_style']
		if body_style:
			cars  = cars.filter(body_style__iexact=body_style)

	if 'min_price' in request.GET:
		min_price = request.GET['min_price']
		max_price = request.GET['max_price']
		if max_price:
			cars  = cars.filter(price_discount__gte=min_price, price_discount__lte=max_price)	
	
	data = {
		'cars' : cars,

		'search_fields' : search_fields,
		'unique_brands' : unique_brands,
		# 'brand_search' : brand_search,
		'model_search' : model_search,
		'city_search' : city_search,
		'year_search' : year_search,
		'body_style_search' : body_style_search,
	}
	return render(request, 'cars/search.html', data)