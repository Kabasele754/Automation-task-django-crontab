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

```
Cette commande ajoute les tâches cron configurées dans votre fichier settings.py à la configuration cron du système. Elle est utilisée après avoir défini vos tâches planifiées avec le module django_crontab dans le fichier settings.py. Lorsque vous exécutez cette commande, elle enregistre ces tâches dans le système de tâches cron, et elles seront ensuite exécutées selon la planification que vous avez définie.

```commandline
python manage.py crontab show
```

Cette commande affiche la liste actuelle des tâches cron planifiées pour votre projet Django. Elle peut être utilisée pour vérifier quelles tâches ont été ajoutées au système de tâches cron. Cela vous permet de confirmer que les tâches planifiées ont été correctement enregistrées et qu'elles sont prêtes à être exécutées selon le calendrier défini.

```commandline
python manage.py crontab remove
```

Cette commande est utilisée pour supprimer les tâches cron associées à votre projet Django du système. Elle peut être utile si vous souhaitez arrêter l'exécution de tâches planifiées pour une raison quelconque. Notez que cela ne supprime pas la configuration de tâches de votre fichier settings.py, mais seulement les tâches planifiées actuelles dans le système de tâches cron.

Remarque : L'utilisation de remove n'est généralement pas nécessaire si vous ajustez simplement la configuration de vos tâches dans le fichier settings.py. Vous pouvez simplement exécuter à nouveau add pour mettre à jour la configuration du système de tâches cron.

Assurez-vous de comprendre les implications avant de supprimer des tâches planifiées, en particulier dans un environnement de production, pour éviter tout impact non souhaité sur le fonctionnement de votre application.

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





