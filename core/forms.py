from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            return [tag.strip().lower() for tag in tags.split(',') if tag.strip()]
        return []

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_tags(instance)
        return instance

    def save_tags(self, instance):
        instance.tags.clear()
        tags = self.cleaned_data.get('tags', [])
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
