from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'exams', ExamViewSet)
router.register(r'assistants', AssistantViewSet)


urlpatterns = router.urls
