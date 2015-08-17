from django.contrib import admin

from .models import Term, Uri

class UriOnTerms(admin.TabularInline):
	model = Uri
	extra = 1

class TermAdmin(admin.ModelAdmin):
	inlines = [UriOnTerms]
	search_fields = ['term_text']

admin.AdminSite.site_header = "Irreconcileable Admin"

admin.site.register(Term, TermAdmin)
admin.site.register(Uri)