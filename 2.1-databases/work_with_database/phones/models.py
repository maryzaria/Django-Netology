from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    image = models.CharField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exist}; {self.slug}"
