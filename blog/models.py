from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

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
