from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Activity,Class,School
from .forms import ActivityForm,ClassForm,SchoolForm
def help(request):
    return render(request, 'main/help.html')
def index(request):
    return render(request, 'main/index.html')
@login_required
def schools(request):
    schools = School.objects.filter().order_by('school_name')
    context = {'schools': schools}
    return render(request, 'main/schools.html', context)
@login_required
def delete_school(request,school_id):
    if School.objects.get(id=school_id).owner!=request.user:
        raise Http404
    if request.method != 'POST':
        School.objects.filter(id=school_id).delete()
    else:
        raise Http404
    return redirect('/schools/')
@login_required
def edit_school(request, school_id):
    school = School.objects.get(id=school_id)
    if School.objects.get(id=school_id).owner!=request.user:
        raise Http404
    if request.method != 'POST':
        form = SchoolForm(instance=school)
    else:
        form = SchoolForm(instance=school, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/schools/')
    context = {'school': school, 'form': form}
    return render(request, 'main/edit_school.html', context)
@login_required
def new_school(request):
    if not request.user.is_superuser:
        raise Http404
    if request.method != 'POST':
        form = SchoolForm()
    else:
        form = SchoolForm(data=request.POST)
        if form.is_valid():
            new_school = form.save(commit=False)
            new_school.owner = request.user
            new_school.save()
            return redirect('main:schools')
    context = {'form': form}
    return render(request, 'main/new_school.html', context)
@login_required
def school(request, school_id):
    school = School.objects.get(id=school_id)
    classes = school.class_set.order_by('class_name')
    context = {'school': school, 'classes': classes}
    return render(request, 'main/school.html', context)
@login_required
def class_(request, class_id):
    class_ = Class.objects.get(id=class_id)
    activities = class_.activity_set.order_by('start_time')
    context = {'class': class_, 'activities': activities}
    return render(request, 'main/class.html', context)
@login_required
def new_class(request,school_id):
    if School.objects.get(id=school_id).owner!=request.user:
        raise Http404
    if request.method != 'POST':
        form = ClassForm()
    else:
        form = ClassForm(data=request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.school=School.objects.get(id=school_id)
            new_class.save()
            return redirect('/school/'+str(school_id))
    context = {'form': form,'schid': school_id}
    return render(request, 'main/new_class.html', context)
@login_required
def new_activity(request, class_id):
    class_ = Class.objects.get(id=class_id)
    if Class.objects.get(id=class_id).school.owner!=request.user:
        raise Http404
    if request.method != 'POST':
        form = ActivityForm()
    else:
        form = ActivityForm(data=request.POST)
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            if start_time and end_time and start_time >= end_time:
                form.add_error(None, '开始时间必须小于结束时间！')
            else:
                new_activity = form.save(commit=False)
                new_activity._class = class_
                new_activity.save()
                return redirect('main:class', class_id=class_id)
    context = {'class': class_, 'form': form}
    return render(request, 'main/new_activity.html', context)
@login_required
def delete_class(request, class_id):
    schid=Class.objects.get(id=class_id).school.id
    if Class.objects.get(id=class_id).school.owner!=request.user:
        raise Http404
    if request.method != 'POST':
        Class.objects.filter(id=class_id).delete()
    else:
        raise Http404
    return redirect('/school/'+str(schid))
@login_required
def edit_class(request, class_id):
    class_ = Class.objects.get(id=class_id)
    sid=class_.school.id
    if Class.objects.get(id=class_id).school.owner!=request.user:
        raise Http404
    if request.method != 'POST':
        form = ClassForm(instance=class_)
    else:
        form = ClassForm(instance=class_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/school/'+str(sid))
    context = {'class': class_, 'form': form}
    return render(request, 'main/edit_class.html', context)
@login_required
def edit_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    class_ = activity._class
    if Activity.objects.get(id=activity_id)._class.school.owner!=request.user:
        raise Http404
    if request.method != 'POST':
        form = ActivityForm(instance=activity)
    else:
        form = ActivityForm(instance=activity, data=request.POST)
        if form.is_valid():
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            if start_time and end_time and start_time >= end_time:
                form.add_error(None, '开始时间必须小于结束时间！')
            else:
                form.save()
                return redirect('main:class', class_id=class_.id)
    context = {'activity': activity, 'class': class_, 'form': form}
    return render(request, 'main/edit_activity.html', context)
@login_required
def delete_activity(request, activity_id):
    if Activity.objects.get(id=activity_id)._class.school.owner!=request.user:
        raise Http404
    if request.method != 'POST':
        a=str(Activity.objects.get(id=activity_id)._class.id)
        Activity.objects.filter(id=activity_id).delete()
    else:
        raise Http404
    return redirect('/classes/'+a)