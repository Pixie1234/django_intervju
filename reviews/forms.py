from django import forms

PRIORITISE_BY_TEXT_YES = "1"
PRIORITISE_BY_TEXT_NO = "2"

HIGHEST_FIRST = "1"
LOWEST_FIRST = "2"

NEWEST_FIRST = "1"
OLDEST_FIRST = "2"

TEXT_CHOICES = ((PRIORITISE_BY_TEXT_YES, ("Yes")), (PRIORITISE_BY_TEXT_NO, ("No")))
RATING_CHOICES = ((1, ("Highest First")), (2, ("Lowest First")))
MINIMUM_RATING_CHOICES = ((1, ("1")), (2, ("2")), (3, ("3")), (4, ("4")), (5, ("5")))
DATE_CHOICES = ((HIGHEST_FIRST, ("Newest First")), (OLDEST_FIRST, ("Oldest First")))


class ReviewsForm(forms.Form):
    order_by_rating = forms.ChoiceField(choices=RATING_CHOICES)
    minimum_rating = forms.ChoiceField(choices=MINIMUM_RATING_CHOICES)
    order_by_date = forms.ChoiceField(choices=DATE_CHOICES)
    prioritize_by_text = forms.ChoiceField(choices=TEXT_CHOICES)
