import json

from reviews.forms import HIGHEST_FIRST, NEWEST_FIRST, PRIORITISE_BY_TEXT_YES
from .review_dataclass import Review


class ReviewService:
    filename = "reviews.json"

    def read_json_file(self) -> list[Review]:
        reviews = []
        with open(self.filename, "r") as file:
            json_data = json.load(file)
            reviews = [Review(**data) for data in json_data]
        return reviews

    def prioritise_by_text(
        self, prioritise_by_text: str, data: list[Review]
    ) -> list[Review]:
        if prioritise_by_text == PRIORITISE_BY_TEXT_YES:
            return sorted(data, key=lambda review: review.reviewFullText == "")
        return data

    def filter_by_minimum_rating(
        self, minimum_rating: str, data: list[Review]
    ) -> list[Review]:
        # list_reviews = []
        # for review in data:
        #     if review.rating >= rating:
        #         list_reviews.append(review)
        # return list_reviews
        minimum_rating_int = int(minimum_rating)
        return [review for review in data if review.rating >= minimum_rating_int]

    def order_by_date(self, order_by_date: str, data: list[Review]) -> list[Review]:
        if order_by_date == NEWEST_FIRST:
            reverse = True
        else:
            reverse = False
        return sorted(data, key=lambda review: review.created, reverse=reverse)

    def order_by_rating(self, order_by_rating: str, data: list[Review]) -> list[Review]:
        if order_by_rating == HIGHEST_FIRST:
            reverse = True
        else:
            reverse = False
        return sorted(data, key=lambda review: review.rating, reverse=reverse)

    def filter_and_sort_data(self, filters: dict[str, str], data: list[Review]):
        prioritise_by_text = filters["prioritize_by_text"]
        order_by_rating = filters["order_by_rating"]
        order_by_date = filters["order_by_date"]
        minimum_rating = filters["minimum_rating"]

        data = self.order_by_date(order_by_date=order_by_date, data=data)
        data = self.order_by_rating(order_by_rating=order_by_rating, data=data)
        data = self.filter_by_minimum_rating(minimum_rating=minimum_rating, data=data)
        data = self.prioritise_by_text(prioritise_by_text=prioritise_by_text, data=data)

        return data
