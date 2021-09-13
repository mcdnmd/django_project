from django.db import models


class Record(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    text = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'records'
