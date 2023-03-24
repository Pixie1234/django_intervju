from django import forms

TEXT_CHOICES = ((1, ("Yes")), (2, ("No")))
RATING_CHOICES = ((1, ("Highest First")), (2, ("Lowest First")))
MINIMUM_RATING_CHOICES = ((1, ("1")), (2, ("2")), (3, ("3")), (4, ("4")), (5, ("5")))
DATE_CHOICES = ((1, ("Newest First")), (2, ("Oldest First")))


class ReviewsForm(forms.Form):
    order_by_rating = forms.ChoiceField(choices=RATING_CHOICES)
    minimum_rating = forms.ChoiceField(choices=MINIMUM_RATING_CHOICES)
    order_by_date = forms.ChoiceField(choices=DATE_CHOICES)
    prioritize_by_text = forms.ChoiceField(choices=TEXT_CHOICES)
