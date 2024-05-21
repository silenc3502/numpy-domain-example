from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=100)
    boardId = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
