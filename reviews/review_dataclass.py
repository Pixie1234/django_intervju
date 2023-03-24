from dataclasses import dataclass
import datetime


@dataclass
class Review:
    id: int
    reviewId: str | None
    reviewFullText: str | None
    reviewText: str | None
    numLikes: int | None
    numComments: int | None
    numShares: int | None
    rating: int | None
    reviewCreatedOn: str | None
    reviewCreatedOnDate: datetime.datetime | None
    reviewCreatedOnTime: int | None
    reviewerId: int | None
    reviewerUrl: str | None
    reviewerName: str | None
    reviewerEmail: str | None
    sourceType: str | None
    isVerified: bool | None
    source: str | None
    sourceName: str | None
    sourceId: str | None
    tags: list
    href: str | None
    logoHref: str | None
    photos: list

    @property
    def created(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(self.reviewCreatedOnDate)
