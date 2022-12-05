from django.shortcuts import render
from django.views.generic import TemplateView
# from .models import

class RegistrationView(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)
