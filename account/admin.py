from django.contrib import admin
from blocks.models import Block, Post, Comment
from account.models import Profile

# Register your models here.
admin.site.register(Block)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)