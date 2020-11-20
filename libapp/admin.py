from django.contrib import admin

from libapp.models import Author
from libapp.models import Lang
from libapp.models import Book
from libapp.models import Genre

class AuthorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Author,AuthorAdmin)
class LangAdmin(admin.ModelAdmin):
	pass
admin.site.register(Lang,LangAdmin)

class GenreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Genre,GenreAdmin)

class BookAdmin(admin.ModelAdmin):
	pass
admin.site.register(Book,BookAdmin)

# Register your models here.
