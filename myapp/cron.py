from django_cron import CronJobBase, Schedule
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from myapp.models import Task, SubTask


class ExpiredTaskNotification(CronJobBase):
    RUN_EVERY_MINS = 60  # Exécute la tâche toutes les heures

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.expired_task_notification'  # Nom de la tâche

    def do(self):
        expired_tasks = Task.objects.filter(expiration_date__lte=timezone.now())

        for task in expired_tasks:
            user = task.user
            send_mail(
                'Votre tâche a expiré',
                'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
        upcoming_tasks = Task.objects.filter(expiration_date__lte=timezone.now() + timezone.timedelta(days=2))

        for task in upcoming_tasks:
            user = task.user
            send_mail(
                'Votre tâche a expiré dans deux jour',
                'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )


def expired_task_notification():
    print("prepare mail send")
    expired_tasks = Task.objects.filter(expiration_date__lte=timezone.now())

    for task in expired_tasks:
        user = task.user
        send_mail(
            'Votre tâche a expiré',
            'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    upcoming_tasks = Task.objects.filter(expiration_date__lte=timezone.now() + timezone.timedelta(days=2))

    for task in upcoming_tasks:
        user = task.user
        send_mail(
            'Votre tâche a expire dans deux jour',
            'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    print("See mail send")


def message_print():
    task = SubTask(
        title = "Achille Task",
        description = "Description task"
    )
    task.save()

    send_mail(
        'Votre tâche a expire dans deux jour',
        'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
        settings.EMAIL_HOST_USER,
        ['pepexykabasele@gmail.com',],
        fail_silently=False,
    )

    print("Save task")
