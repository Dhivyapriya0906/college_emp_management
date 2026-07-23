from django.db import models




class LeaveEntry(models.Model):

    LEAVE_TYPE_CHOICES = [
        ('OD', 'OD'),
        ('Casual Leave', 'Casual Leave'),
        ('Loss Of Pay', 'Loss Of Pay'),
    ]

    LEAVE_DURATION_CHOICES = [
        ('Single Day', 'Single Day'),
        ('Multiple Day', 'Multiple Day'),
    ]

    SESSION_CHOICES = [
        ('AM', 'AM'),
        ('PM', 'PM'),
        ('Both', 'Both'),
    ]

    LEAVE_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    leave_id = models.AutoField(primary_key=True, db_column='leave_id')

    emp_id = models.IntegerField(db_column='emp_id')

    leave_duration = models.CharField(
        max_length=20, choices=LEAVE_DURATION_CHOICES, db_column='leave_duration'
    )

    leave_type = models.CharField(
        max_length=20, choices=LEAVE_TYPE_CHOICES, db_column='leave_type'
    )

    single_leave_date = models.DateField(null=True, blank=True, db_column='single_leave_date')

    session = models.CharField(
        max_length=10, choices=SESSION_CHOICES, null=True, blank=True, db_column='session'
    )

    from_date = models.DateField(null=True, blank=True, db_column='from_date')
    to_date = models.DateField(null=True, blank=True, db_column='to_date')

    reason = models.TextField(db_column='reason')

    alternate_employee_id = models.IntegerField(null=True, blank=True, db_column='alternate_employee_id')

    leave_status = models.CharField(
        max_length=20, choices=LEAVE_STATUS_CHOICES, default='Pending', db_column='leave_status'
    )

    class Meta:
        db_table = 'leave_entry'
        managed = False   # table is created by the team's shared SQL script, not by Django

    def __str__(self):
        return f"Leave {self.leave_id} - Employee {self.emp_id}"



class WorkArrangement(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    arrangement_id = models.AutoField(
        primary_key=True,
        db_column='arrangement_id'
    )

    leave = models.ForeignKey(
        LeaveEntry,
        on_delete=models.CASCADE,
        db_column='leave_id'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
        db_column='status'
    )

    response_date = models.DateTimeField(
        null=True,
        blank=True,
        db_column='response_date'
    )

    remarks = models.CharField(
        max_length=255,
        blank=True,
        db_column='remarks'
    )

    class Meta:
        db_table = 'work_arrangement'

    def __str__(self):
        return f"Arrangement {self.arrangement_id}"
