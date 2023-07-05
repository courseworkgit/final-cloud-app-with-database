from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.ModelAdmin):
    list_display = ['question']
    
class ChoiceInline(admin.TabularInline):
    list_display = ['choice']
    
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None, {"fields": ["question_text"]}),
#        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ["question_text", "pub_date", "was_published_recently"]
#    list_filter = ["pub_date"]
#    search_fields = ["question_text"]


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
