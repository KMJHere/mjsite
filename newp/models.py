from csv import writer
from django.db import models

# Create your models here.
class member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='') # 길이 제한이 있는 문자열 

    # 값이 출력되도록 출력 데이터 형식 변경
    def __str__(self): 
        return self.name

class board(models.Model):
    writer = models.ForeignKey(member, on_delete=models.CASCADE)
    content = models.TextField() # 길이 제한이 없는 문자열 
    crtdate = models.DateTimeField(auto_now_add=True) # 레코드 생성 시 현재 시간 자동 저장
    def __str__(self): 
        return self.content

class like(models.Model):
    content = models.ForeignKey(board, on_delete=models.CASCADE) # writer랑 연결.. 연습이라 그냥 하기
    rmk = models.CharField(max_length=200)
    like = models.IntegerField(default=0)

    # 형식 > 문자 출력되도록 변경
    def __str__(self):
        return self.rmk
     