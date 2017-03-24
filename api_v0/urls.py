from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'get_exam_list', ExamViewSet)
router.register(r'get_assistant_list', AssistantViewSet)


urlpatterns = router.urls
