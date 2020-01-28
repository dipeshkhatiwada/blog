from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def customLengthValidator(value):
    if len(value) > 5:
        return True
    else:
        raise ValidationError("must have more than 5 chars")


def atValidator(value):
    if '@' in value:
        raise ValidationError("title cannot have @  chars")
    else:
        return True

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, validators=[customLengthValidator, atValidator, ])

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #  null is related to database and  blank is related to form
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    publish_date = models.DateField(auto_now=True)
    # auto now provide today date
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # django will atomically add _id in foreign key

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"
        # it will name the database table
