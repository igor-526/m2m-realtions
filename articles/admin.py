from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Выберите тэги')
        main_counter = 0
        dels = 0
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                dels += 1
            print(form.cleaned_data)
            if form.cleaned_data.get('is_main') and not form.cleaned_data.get('DELETE'):
                main_counter += 1

        if dels == len(self.forms):
            raise ValidationError('Вы оставили новость без тэгов')
        if main_counter == 1:
            return super().clean()
        else:
            raise ValidationError('Главный тэг может быть только 1!')


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass