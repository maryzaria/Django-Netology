from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        firts_form = self.forms[0].cleaned_data
        article = firts_form.get('article')
        if not article:
            raise ValidationError('Непредвиденная ошибка')

        old_tags = article.tags.all()
        tags = {}
        main_tag = None

        for tag in old_tags:
            old_tag = Scope.objects.filter(tag=tag).first()
            if old_tag.is_main:
                main_tag = old_tag

        for form in self.forms:
            res = form.cleaned_data
            new_tag = res.get('tag', '')
            is_main = res.get('is_main')

            if not isinstance(new_tag, Tag):
                raise ValidationError('Разделы не должны быть пустыми')

            if new_tag in tags or new_tag in old_tags:
                raise ValidationError('Каждый раздел может быть добавлен только 1 раз')

            if is_main:
                if not main_tag:
                    main_tag = new_tag
                else:
                    raise ValidationError('Основным может быть только 1 раздел')

            if new_tag not in old_tags:
                tags[new_tag] = is_main

        if not main_tag:
            raise ValidationError('Укажите основной раздел')

        for tag, is_main in tags.items():
            Scope.objects.create(article=article, tag=tag, is_main=is_main)

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    fields = []
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
