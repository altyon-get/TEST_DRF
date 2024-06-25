from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    father_name = models.CharField(max_length=100)


#learning ORM:
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()



class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline



























