from django.db import models

# Create your models here.


class Restaurant(models.Model):
    # 식당 이름
    name = models.CharField(max_length=50)
    # 음식 종류 (한식, 일식 등)
    category = models.CharField(max_length=20)
    # 식당 위치
    location = models.CharField(max_length=100)
    # 식당 한줄 설명 
    description = models.TextField(blank=True)
    
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)

    def __str__(self):
        return self.name
    
# restaurants/models.py

class Comment(models.Model):
    # 댓글 내용 
    comment = models.CharField(max_length=200) 
    # 작성일 (자동 생성) 
    date = models.DateTimeField(auto_now_add=True) 
    # 어떤 맛집 게시글에 달린 댓글인지 연결 (외래키) 
    article = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='comments') 

    def __str__(self):
        return self.comment 