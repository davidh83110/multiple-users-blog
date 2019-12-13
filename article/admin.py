from django.contrib import admin
from django.db import models

# Register your models here.
from .models import ArticlePost, ExampleModel
from. import models as demo_models
from mdeditor.widgets import MDEditorWidget

from .forms import Remark

admin.site.register(ArticlePost)

class RemarkAdmin(admin.ModelAdmin):
    list_display = ('subject','mail','topic','message')
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

admin.site.register(Remark,RemarkAdmin)


class ExampleModelAdmin (admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

admin.site.register(demo_models.ExampleModel, ExampleModelAdmin)