from django.db import models

class Author(models.Model):
	auth_name=models.CharField(max_length=50)
	dob=models.DateField()
	dod=models.DateField()
        no_of_books=models.IntegerField()
	def __str__(self):
		return self.auth_name

class Genre(models.Model):
	gen_name=models.CharField(max_length=30)
	def __str__(self):
		return self.gen_name

class Lang(models.Model):
	lang_name=models.CharField(max_length=20)
	def __str__(self):
		return self.lang_name



class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
	summary=models.CharField(max_length=100)
	isbn=models.CharField(primary_key=True,help_text='unique code required',max_length=10)
	genre=models.ManyToManyField(Genre)
	language=models.ForeignKey(Lang,on_delete=models.SET_NULL,null=True)
	def __str__(self):
		return self.title

class bookinstance(models.Model):
	uniqueid=models.CharField(primary_key=True,max_length=20)
	due_back=models.DateField()
	LOAN_STATUS=(("i","issued"),
		("a","available"),	("r","reserved"))	
	status=models.CharField(max_length=1,choices=LOAN_STATUS)
	book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)









# Create your models here.
