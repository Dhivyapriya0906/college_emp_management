from django.db import models


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    mobile_no = models.CharField(max_length=15)
    alternate_mobile_no = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    religion = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    community = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    dob = models.DateField()

    p_door_no = models.CharField(max_length=20, blank=True, null=True)
    p_street = models.CharField(max_length=100, blank=True, null=True)
    p_town = models.CharField(max_length=100, blank=True, null=True)
    p_district = models.CharField(max_length=100, blank=True, null=True)
    p_state = models.CharField(max_length=100, blank=True, null=True)
    p_country = models.CharField(max_length=100, blank=True, null=True)

    t_door_no = models.CharField(max_length=20, blank=True, null=True)
    t_street = models.CharField(max_length=100, blank=True, null=True)
    t_town = models.CharField(max_length=100, blank=True, null=True)
    t_district = models.CharField(max_length=100, blank=True, null=True)
    t_state = models.CharField(max_length=100, blank=True, null=True)
    t_country = models.CharField(max_length=100, blank=True, null=True)

    marital_status = models.CharField(max_length=8, blank=True, null=True)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)

    password = models.CharField(max_length=255)

    employee_type = models.CharField(max_length=13)
    employee_shift = models.CharField(max_length=7)

    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.emp_name

    class Meta:
        managed = False
        db_table = "employee"