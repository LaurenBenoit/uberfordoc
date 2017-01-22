from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels


# Create your views here.


class LandingView(TemplateView):
	template_name = "base/index.html"

class LocationListView(ListView):
	model = coremodels.Location
	template_name = "/location/list.html"

	# def get_queryset(self):
	# 	cache_mem = get_cache('django.core.cache.backends.memcached.MemcachedCache', **{
	# 		'LOCATION': 'unix:/var/run/memcached/memcached.sock', 'TIMEOUT': 120,
	# 	})
	# 	users_fans = cache_mem.get('salat_streaks')
	# 	# print users_fans
	# 	if users_fans:
	# 		return users_fans
	# 	else:
	# 		return []

	# def get_context_data(self, **kwargs):
	# 	context=super(LocationListView, self).get_context_data(**kwargs)
	# 	# if self.request.user.is_authenticated():
	# 	# 	context["girls"] = FEMALES
	# 	return context

class LocationDetailView(DetailView):
	model = coremodels.Location
	template_name = "/location/detail.html"
	context_object_name = "location"