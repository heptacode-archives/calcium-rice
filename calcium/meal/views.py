from meal.models import Meal

from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    model = Meal
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal'] = ['meal', ]
        return context

class DetailView(TemplateView):
    model = Meal
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal'] = ['meal', ]
        return context