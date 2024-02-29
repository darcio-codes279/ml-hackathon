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
    location_active = models.BooleanField(default=True)
    number_people_live_in_household_active = models.BooleanField(default=True)
    who_is_in_household_active = models.BooleanField(default=True)
    income_active = models.BooleanField(default=True)

    @classmethod
    def get_default_pk(cls):
            template, created = cls.objects.get_or_create(code='default template')
            return template.pk

class FormDetail(models.Model):
    template = models.ForeignKey(FormTemplate, default=FormTemplate.get_default_pk, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=13, blank=True, default='n/a')
    pronouns = models.CharField(max_length=13, blank=True, default='n/a')
    age = models.CharField(max_length=13, blank=True, default='n/a')
    ethnicity = models.CharField(max_length=13, blank=True, default='n/a')
    disabilitiy = models.CharField(max_length=13, blank=True, default='n/a')
    employment_status = models.CharField(max_length=13, blank=True, default='n/a')
    location = models.CharField(max_length=13, blank=True, default='n/a')
    number_people_live_in_household = models.CharField(max_length=13, blank=True, default='n/a')
    who_is_in_household = models.CharField(max_length=13, blank=True, default='n/a')
    income = models.CharField(max_length=13, blank=True, default='n/a')