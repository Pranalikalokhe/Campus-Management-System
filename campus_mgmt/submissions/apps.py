from django.apps import AppConfig

class SubmissionsConfig(AppConfig):
    name = 'submissions'

    def ready(self):
        import submissions.signals
