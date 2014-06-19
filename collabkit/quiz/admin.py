from quiz.models import *
from django.contrib import admin


class SetAdmin(admin.ModelAdmin):
    pass


class QuestionAnswerChoiceAdmin(admin.ModelAdmin):
    pass


class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswerChoice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionAnswerInline]
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'set':
            sets = Set.objects.order_by("-id")
            kwargs['queryset'] = sets
            if len(sets) > 0:
                kwargs['initial'] = sets[0]

        return super(QuestionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Set, SetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionAnswerChoice, QuestionAnswerChoiceAdmin)