from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Cat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    breed = models.CharField(max_length=120)
    color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    MALE = "MA"
    FEMALE = "FE"
    PET_SEX = [
        (MALE, "MA"),
        (FEMALE, "FA"),
    ]
    SMALL = "SM"
    MEDIUM = "MD"
    LARGE = "LG"
    PET_SIZE = [
        (SMALL, "SM"),
        (MEDIUM, "MD"),
        (LARGE, "LG"),
    ]
    LONG = "long"
    SHORT = "short"
    MEDIUM = "medium"
    PET_HAIR = [
        (LONG, "long"),
        (SHORT, "short"),
        (MEDIUM, "medium"),
    ]
    size = models.CharField(max_length=2, choices=PET_SIZE, blank=True)
    sex = models.CharField(max_length=2, choices=PET_SEX, blank=True)
    hair = models.CharField(max_length=2, choices=PET_HAIR, blank=True)
    dateCreation = models.DateTimeField()
    # slug = AutoSlugField(max_length=50, populate_from=get_slug, unique=True)

    # def get_absolute_url(self):
    #     return reverse("CATHUB:detail", kwargs={"pk_or_slug": self.slug})

    # def get_sex(self):
    #     return dict(self.PET_SEX).get(self.sex)
    #
    # def get_size(self):
    #     return dict(self.PET_SIZE).get(self.size)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-dateCreation"]
        # unique_together = ("name", "owner")

# Create your models here.
