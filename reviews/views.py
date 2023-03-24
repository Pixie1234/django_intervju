from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .forms import ReviewsForm


class MyFormView(FormView):
    template_name = "form_template.html"
    form_class = ReviewsForm
    success_url = reverse_lazy(
        "success"
    )  # URL to redirect to after successful form submission

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Process the form data here
            return redirect("google.com")
        return render(request, self.template_name, {"form": form})
