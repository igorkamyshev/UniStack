from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'get_exam_list', ExamViewSet)
router.register(r'get_assistant_list', AssistantViewSet)
router.register(r'get_training_direction_list', TrainingDirectionViewSet)
router.register(r'get_training_direction_group_list', TrainingDirectionGroupViewSet)
router.register(r'get_country_list', CountryViewSet)
router.register(r'get_region_list', RegionViewSet)
router.register(r'get_city_list', CityViewSet)


urlpatterns = router.urls
