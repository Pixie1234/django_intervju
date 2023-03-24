from dataclasses import asdict
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from reviews.json_parsing import ReviewService
from .forms import ReviewsForm


class MyFormView(FormView):
    template_name = "form_template.html"
    form_class = ReviewsForm
    success_url = reverse_lazy(
        "success"
    )  # URL to redirect to after successful form submission

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            filters = form.cleaned_data
            service = ReviewService()
            data = service.read_json_file()
            filtered_and_ordered_reviews = service.filter_and_sort_data(
                filters=filters, data=data
            )
            dict_reviews = [asdict(review) for review in filtered_and_ordered_reviews]
            return JsonResponse(dict_reviews, safe=False)
        return render(request, self.template_name, {"form": form})
