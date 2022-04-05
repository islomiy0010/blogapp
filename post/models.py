from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img=models.ImageField(default='default.png',upload_to='post')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.all().count()

    # def comments(self):
    #     return self.comment_set.all()
    class Meta:
        verbose_name_plural='Postlar'

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

