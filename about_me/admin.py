from django.contrib import admin
from models import Education, Location, PersonalInfo, Project, Skill, Technology, TechnologyCompetence, School


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


class TechnologyCompetenceInline(admin.StackedInline):
    model = TechnologyCompetence
    extra = 0


class PersonalInfoAdmin(admin.ModelAdmin):
    inlines = [EducationInline, TechnologyCompetenceInline]

admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register([Location, Project, Technology, School, Skill])