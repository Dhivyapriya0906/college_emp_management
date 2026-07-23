from django.shortcuts import render, redirect, get_object_or_404
from .models import LeaveEntry
from .forms import LeaveEntryForm
from django.contrib import messages
from .models import WorkArrangement
from .forms import WorkArrangementForm
from django.utils import timezone
from .models import WorkArrangement
from django.shortcuts import render


def work_arrangement_list(request):
    arrangements = WorkArrangement.objects.select_related('leave').all()

    return render(
        request,
        'leave_management/work_arrangement_list.html',
        {'arrangements': arrangements}
    )
def arrangement_list(request):
    arrangements = WorkArrangement.objects.all()
    return render(request, 'leave_management/work_arrangement.html', {'arrangements': arrangements})


def arrangement_create(request):
    if request.method == "POST":
        form = WorkArrangementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Arrangement Created")
            return redirect('arrangement_list')
    else:
        form = WorkArrangementForm()

    return render(request, 'leave_management/arrangement_form.html', {'form': form})


def arrangement_update_status(request, pk):
    arrangement = get_object_or_404(WorkArrangement, pk=pk)

    if request.method == "POST":
        new_status = request.POST.get('status')
        arrangement.status = new_status
        arrangement.response_date = timezone.now()
        arrangement.save()
        messages.success(request, f"Arrangement {new_status}")
        return redirect('arrangement_list')

    return render(request, 'leave_management/arrangement_update.html', {'arrangement': arrangement})
def leave_list(request):
    leaves = LeaveEntry.objects.all()
    return render(request, 'leave_management/leave_list.html', {'leaves': leaves})



def leave_create(request):
    if request.method == "POST":
        form = LeaveEntryForm(request.POST)
        if form.is_valid():

            leave = form.save()

            WorkArrangement.objects.create(
                leave=leave,
                status="Pending"
            )

            messages.success(request, "Leave Applied Successfully")
            return redirect('leave_list')

    else:
        form = LeaveEntryForm()

    return render(request, 'leave_management/leave_form.html', {'form': form})


def leave_update(request, pk):
    leave = get_object_or_404(LeaveEntry, pk=pk)

    # Allow update only when status is Pending
    if leave.leave_status != "Pending":
        messages.error(request, "Only pending leave requests can be edited.")
        return redirect('leave_list')

    if request.method == "POST":
        form = LeaveEntryForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, "Leave Updated Successfully")
            return redirect('leave_list')
    else:
        form = LeaveEntryForm(instance=leave)

    return render(request, 'leave_management/leave_update.html', {
        'form': form
    })
def leave_delete(request, pk):
    leave = get_object_or_404(LeaveEntry, pk=pk)

    # Allow delete only when status is Pending
    if leave.leave_status != "Pending":
        messages.error(request, "Only pending leave requests can be deleted.")
        return redirect('leave_list')

    if request.method == "POST":
        leave.delete()
        messages.success(request, "Leave Deleted Successfully")
        return redirect('leave_list')

    return render(
        request,
        'leave_management/leave_delete.html',
        {'leave': leave}
    )
def update_work_arrangement(request, pk, status):

    arrangement = get_object_or_404(
        WorkArrangement,
        pk=pk
    )

    arrangement.status = status
    arrangement.response_date = timezone.now()
    arrangement.save()

    return redirect('work_arrangement_list')