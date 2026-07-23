from django import forms
from .models import LeaveEntry
from .models import WorkArrangement

class WorkArrangementForm(forms.ModelForm):

    class Meta:
        model = WorkArrangement
        fields = ['leave', 'status', 'remarks']

        widgets = {
            'leave': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class LeaveEntryForm(forms.ModelForm):

    class Meta:
        model = LeaveEntry
        fields = [
            'emp_id',
            'leave_type',
            'leave_duration',
            'single_leave_date',
            'session',
            'from_date',
            'to_date',
            'reason',
            'alternate_employee_id',
        ]

        widgets = {
            'emp_id': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'leave_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'leave_duration': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_leave_duration'
            }),

            'single_leave_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'from_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'to_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'session': forms.Select(attrs={
                'class': 'form-control'
            }),

            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'alternate_employee_id': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean(self):

        cleaned_data = super().clean()

        leave_duration = cleaned_data.get("leave_duration")
        single_leave_date = cleaned_data.get("single_leave_date")
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if leave_duration == "Single Day":

            if not single_leave_date:
                self.add_error(
                    "single_leave_date",
                    "Please select the leave date."
                )

        elif leave_duration == "Multiple Day":

            if not from_date:
                self.add_error(
                    "from_date",
                    "Please select From Date."
                )

            if not to_date:
                self.add_error(
                    "to_date",
                    "Please select To Date."
                )

            if from_date and to_date:

                if from_date > to_date:
                    raise forms.ValidationError(
                        "From Date cannot be greater than To Date."
                    )

        return cleaned_data