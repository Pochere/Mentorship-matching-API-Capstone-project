from django.contrib import admin
from .models import Mentor, Mentee, MentorshipSession


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'expertise', 'availability')
    search_fields = ('user__username', 'expertise')
    list_filter = ('availability',)


@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'interests', 'goals')
    search_fields = ('user__username', 'interests')


@admin.register(MentorshipSession)
class MentorshipSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'mentor', 'mentee', 'topic', 'date', 'time', 'completed')
    search_fields = ('topic', 'mentor__user__username', 'mentee__user__username')
    list_filter = ('completed', 'date')
