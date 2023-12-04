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

Les étoiles dans la chaîne cron (*/5 * * * *) spécifient la fréquence d'exécution d'une tâche. Dans le contexte de cron, chaque astérisque * correspond à un champ spécifique qui détermine quand une tâche doit être exécutée. La syntaxe complète d'une chaîne cron est la suivante 

```commandline
┌───────── minute (0 - 59)
│ ┌─────── heure (0 - 23)
│ │ ┌───── jour du mois (1 - 31)
│ │ │ ┌─── mois (1 - 12)
│ │ │ │ ┌─ jour de la semaine (0 - 6) (dimanche à samedi; 7 est également dimanche)
│ │ │ │ │
│ │ │ │ │
* * * * *

```
Dans votre exemple, la chaîne cron '*/5 * * * *' est interprétée comme suit :

*/5 pour les minutes : Cela signifie "toutes les 5 minutes". Donc, cette tâche sera exécutée toutes les cinq minutes.

Voici une explication détaillée de chaque astérisque dans la chaîne */5 * * * * :

1. Minute (*/5) : Cela signifie "toutes les 5 minutes". Ainsi, la tâche serait exécutée toutes les 5 minutes.

2. Heure (*) : Cela signifie "à chaque heure". L'astérisque ici indique que la tâche sera exécutée à chaque heure, indépendamment de l'heure spécifique.

3. Jour du mois (*) : Cela signifie "chaque jour du mois". L'astérisque ici indique que la tâche sera exécutée tous les jours du mois, indépendamment du jour spécifique.

4. Mois (*) : Cela signifie "chaque mois". L'astérisque ici indique que la tâche sera exécutée tous les mois, indépendamment du mois spécifique.

5. Jour de la semaine (*) : Cela signifie "chaque jour de la semaine". L'astérisque ici indique que la tâche sera exécutée tous les jours de la semaine, indépendamment du jour spécifique de la semaine.

En résumé, la chaîne cron */5 * * * * configure une tâche pour s'exécuter toutes les 5 minutes, indépendamment de l'heure, du jour du mois, du mois ou du jour de la semaine.



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





