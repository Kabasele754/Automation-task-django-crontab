from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Task


def task_list(request):
    expired_tasks = Task.objects.filter(expiration_date__lte=timezone.now())
    upcoming_tasks = Task.objects.filter(expiration_date__lte=timezone.now() + timezone.timedelta(days=2))

    # for task in expired_tasks:
    #     user = task.user
    #     send_mail(
    #         'Votre tâche a expiré',
    #         'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
    #         settings.EMAIL_HOST_USER,
    #         [user.email],
    #         fail_silently=False,
    #     )

    return render(request, 'myapp/task_list.html', {'expired_tasks': expired_tasks, 'upcoming_tasks': upcoming_tasks})
