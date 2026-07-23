from django.db import models

# Create your models here.
class WorkArrangement(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    arrangement_id = models.AutoField(primary_key=True)

    leave_id = models.ForeignKey(
        LeaveEntry,
        on_delete=models.CASCADE,
        db_column='leave_id'
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    response_date = models.DateTimeField(null=True, blank=True)

    remarks = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'work_arrangement'

    def __str__(self):
        return f"Arrangement {self.arrangement_id}"
