from django.contrib import admin
from .models import Question, Choice

# forced stack visible (displays each field as a new line) >> admin.StackedInline
# tabular inline (displays more compact) >> admin.TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	# reorder fields >>
	#fields = ['pub_date', 'question_text']
	# reorder fields splitting into fieldsets
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	# add choices in question management
	inlines = [ChoiceInline]
	# specify what to show on admin model elements view
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# add filter sidebar by given fields, in this case, pub_date
	list_filter = ['pub_date']
	# add search field to questions list page
	search_fields = ['question_text']
	# set elements per page, by default 100
	list_per_page = 20

### ANOTATION
# if Choice is added as inline in Questions
# it can not be displayed as element itself


admin.site.register(Question, QuestionAdmin)
