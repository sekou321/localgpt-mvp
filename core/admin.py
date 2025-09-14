"""from django.contrib import admin
from .models import Category, Region, Info, Vote

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Info)
admin.site.register(Vote)"""

from django.contrib import admin
from .models import Info, Vote, Category,Region
# ---- Admin pour les votes ----
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('info', 'user', 'vote_type', 'created_at')
    list_filter = ('vote_type', 'created_at')
    search_fields = ('info__title', 'user__username')


# ---- Admin pour les infos ----
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'region', 'contributor', 'created_at', 'vote_score_admin', 'validated_admin')

    def vote_score_admin(self, obj):
        return obj.vote_score()  # ici on appelle la méthode avec ()
    vote_score_admin.short_description = 'Score'

    def validated_admin(self, obj):
        return obj.validated  # propriété, pas besoin de ()
    validated_admin.boolean = True
    validated_admin.short_description = 'Validée ?'

admin.site.register(Category)
admin.site.register(Region)
