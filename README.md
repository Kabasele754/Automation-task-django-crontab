# Automation-task-django-crontab

Django-crontab est une application qui permet d'automatiser l'exécution de tâches planifiées dans un projet Django en utilisant le système de tâches cron. Cela peut être particulièrement utile pour exécuter des tâches de fond, des scripts de maintenance, des notifications automatisées, etc. Voici comment vous pouvez automatiser une tâche avec django-crontab :

## Installation

Tout d'abord, installez django-crontab à l'aide de pip :

```commandline
pip install django
pip install django-crontab
```

Ajoutez ensuite 'django_crontab' à la liste des applications dans le fichier settings.py de votre projet Django.

```commandline
INSTALLED_APPS = [
    # ...
    'myapp',
    'django_crontab',
    
]
```

## Configuration
Dans votre fichier settings.py, ajoutez une configuration pour les tâches cron que vous souhaitez automatiser.

```commandline
# Exemple d'une tâche planifiée pour exécuter votre fonction toutes les heures
CRONJOBS = [
    ('*/5 * * * *', 'myapp.cron.message_print')
]
```

Dans cet exemple, la tâche est planifiée pour être exécutée toutes les 5 munites . Vous pouvez ajuster la chaîne cron selon vos besoins spécifiques.


## Appliquer la Configuration
Après avoir ajouté la configuration, appliquez-la à votre projet en exécutant la commande suivante :

```commandline
python manage.py crontab add
python manage.py crontab show
python manage.py crontab remove

```

## Exemple de Fonction à Automatiser
Voici un exemple simple de la fonction que vous pourriez automatiser :

```commandline
def message_print():
    task = SubTask(
        title = "Achille Task",
        description = "Description task"
    )
    task.save()
```

## Note Importante
Assurez-vous que votre serveur est configuré pour exécuter les tâches cron. La configuration dépend du serveur que vous utilisez. Par exemple, si vous utilisez le serveur de développement Django, il exécutera les tâches cron par défaut. Pour les environnements de production, assurez-vous que le système de tâches cron est configuré correctement pour exécuter les tâches planifiées.

N'oubliez pas de tester soigneusement cette configuration dans un environnement de développement avant de la déployer en production.





