from django.conf import settings
from django.db import models


class Student_content(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    resume = models.TextField()
    mis_id = models.CharField(max_length=10)

    def __str__(self):
        return self.student.username


class Entrepreneur_content(models.Model):
    entrepreneur = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    companytitle = models.CharField(max_length=100)
    introduction = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.entrepreneur.username


class Post(models.Model):
    postid = models.IntegerField(primary_key=True)
    entrepreneur = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    jobtype = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    detail = models.TextField()
    condition = models.TextField()
    benefit = models.TextField()
    contact = models.TextField()
    min_salary = models.PositiveIntegerField()
    viewed = models.IntegerField()
    like = models.IntegerField()
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class QA(models.Model):
    qaid = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student_content, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(
        Entrepreneur_content, on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class LikeList(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return self.post.title


class ViewList(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return self.post.title