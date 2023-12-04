from django_cron import CronJobBase, Schedule
from django.core.management import call_command
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from myapp.models import Task, SubTask


class ExpiredTaskNotification(CronJobBase):
    RUN_EVERY_MINS = 2  # Exécute la tâche toutes les heures

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

        # Récupérer toutes les tâches expirées dans les deux jours (y compris celles déjà récupérées)
        upcoming_tasks = Task.objects.filter(
            expiration_date__lte=timezone.now() + timezone.timedelta(days=2),
            expiration_date__gt=timezone.now()  # Filtrer les tâches qui ont expiré dans les 2 jours
        )

        for task in upcoming_tasks:
            user = task.user
            send_mail(
                'Votre tâche a expiré dans deux jour',
                'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
        call_command('runcrons')


def expired_task_notification():
    # Affiche un message indiquant la préparation de l'envoi des e-mails
    print("prepare mail send")

    # Récupère toutes les tâches expirées
    expired_tasks = Task.objects.filter(expiration_date__lte=timezone.now())

    # Itère sur chaque tâche expirée et envoie un e-mail à l'utilisateur
    for task in expired_tasks:
        user = task.user
        send_mail(
            'Votre tâche a expiré',
            'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    # Récupère toutes les tâches expirées dans les deux jours (y compris celles déjà récupérées)
    upcoming_tasks = Task.objects.filter(
        expiration_date__lte=timezone.now() + timezone.timedelta(days=2),
        expiration_date__gt=timezone.now()  # Filtrer les tâches qui ont expiré dans les 2 jours
    )

    # Itère sur chaque tâche à venir dans les deux jours et envoie un e-mail à l'utilisateur
    for task in upcoming_tasks:
        user = task.user
        send_mail(
            'Votre tâche expire dans deux jours',
            'La tâche "{}" va expirer dans deux jours. Veuillez la compléter, s\'il vous plaît.'.format(task.title),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    # Affiche un message indiquant que les e-mails ont été envoyés
    print("See mail send")


def message_print():
    task = SubTask(
        title = "Achille Task",
        description = "Description task"
    )
    task.save()

    # send_mail(
    #     'Votre tâche a expire dans deux jour Achille Task',
    #     'La tâche "{}" a expiré. Veuillez la mettre à jour.'.format(task.title),
    #     settings.EMAIL_HOST_USER,
    #     ['pepexykabasele@gmail.com',],
    #     fail_silently=False,
    # )

    print("Save task")
