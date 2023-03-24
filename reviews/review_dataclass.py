from dataclasses import dataclass
import datetime
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Review:
    id: int
    review_id: str | None
    review_full_text: str | None
    review_text: str | None
    num_likes: int | None
    num_comments: int | None
    num_shares: int | None
    rating: int | None
    review_created_on: str | None
    review_created_on_date: datetime.datetime | None
    review_created_on_time: int | None
    reviewer_id: int | None
    reviewer_url: str | None
    reviewer_name: str | None
    reviewer_email: str | None
    source_type: str | None
    is_verified: bool | None
    source: str | None
    source_name: str | None
    source_id: str | None
    tags: list
    href: str | None
    logo_href: str | None
    photos: list
