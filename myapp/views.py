from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Task


def task_list(request):
    expired_tasks = Task.objects.filter(expiration_date__lte=timezone.now())
    # Récupérer toutes les tâches expirées dans les deux jours (y compris celles déjà récupérées)
    upcoming_tasks = Task.objects.filter(
        expiration_date__lte=timezone.now() + timezone.timedelta(days=2),
        expiration_date__gt=timezone.now()  # Filtrer les tâches qui ont expiré dans les 2 jours
    )

    # for task in upcoming_tasks:
    #     user = task.user
    #     send_mail(
    #         'Votre tâche expire dans deux jour',
    #         'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
    #         settings.EMAIL_HOST_USER,
    #         [user.email],
    #         fail_silently=False,
    #     )

    return render(request, 'myapp/task_list.html', {'expired_tasks': expired_tasks, 'upcoming_tasks': upcoming_tasks})
