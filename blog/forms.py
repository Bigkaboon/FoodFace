from .models import Comment, Post, Profile
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'featured_image')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Content - Write the content of your post here',
            'excerpt': 'Excerpt'
        }

        for field in self.fields:
            if field != 'featured_image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'post-form-style'
            self.fields[field].label = False
            self.fields['featured_image'].widget.attrs['class'] = 'img-btn'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
