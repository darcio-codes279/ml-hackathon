from django.db import models

# Create your models here.
class FormTemplate(models.Model):
    code = models.CharField(max_length = 10, primary_key=True)
    gender_active = models.BooleanField(default=True)
    pronouns_active = models.BooleanField(default=True)
    age_active = models.BooleanField(default=True)
    ethnicity_active = models.BooleanField(default=True)
    disabilitiy_active = models.BooleanField(default=True)
    employment_status_active = models.BooleanField(default=True)

    @classmethod
    def get_default_pk(cls):
            template, created = cls.objects.get_or_create(code='default template')
            return template.pk

class FormDetail(models.Model):
    template = models.ForeignKey(FormTemplate, default=FormTemplate.get_default_pk, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=3, blank=True, default='n/a')
    pronouns = models.CharField(max_length=3, blank=True, default='n/a')
    age = models.CharField(max_length=3, blank=True, default='n/a')
    ethnicity = models.CharField(max_length=3, blank=True, default='n/a')
    disabilitiy = models.CharField(max_length=3, blank=True, default='n/a')
    employment_status = models.CharField(max_length=3, blank=True, default='n/a')