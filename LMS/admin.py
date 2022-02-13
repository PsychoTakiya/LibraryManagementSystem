from django.contrib import admin

from LMS.models import Books, Readers, Borrowers

# Register your models here.
admin.site.register(Books)
admin.site.register(Readers)
admin.site.register(Borrowers)