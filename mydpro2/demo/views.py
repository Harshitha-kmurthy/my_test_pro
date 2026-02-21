from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
from .forms import contactf

class HomeView(TemplateView):
    template_name = "demo/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Data coming from backend
        context["name"] = "Harshitha K"
        context["role"] = "MCA Student & Aspiring Software Developer"

        context["skills"] = [
            {"title": "Languages", "items": "Python, Java, PHP"},
            {"title": "Frontend", "items": "HTML, CSS, JavaScript, Bootstrap"},
            {"title": "Backend", "items": "Django"},
            {"title": "Database", "items": "MySQL, SQLite"},
        ]

        return context


class ContactView(View):

    def get(self, request):
        form = contactf()
        return render(request, "demo/contact.html", {"form": form})

    def post(self, request):
        form = contactf(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # PRINT IN TERMINAL
            print("----- CONTACT FORM SUBMITTED -----")
            print("Name:", name)
            print("Email:", email)
            print("Message:", message)
            print("----------------------------------")

        return render(request, "demo/contact.html", {"form": form})