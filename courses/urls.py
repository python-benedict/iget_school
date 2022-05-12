from django.urls import path
from .import views
app_name = 'courses'

urlpatterns=[
    path('', views.index, name="homepage"),
    path('list-courses', views.listCoursesView, name="list-courses"),
    path('course-detail/<int:pk>', views.CourseDetailView, name="course-detail"),

    # user specific screens
    path("my-account", views.userAccountPage, name="account"),
    path("list-lessons", views.userRegisteredCourses.as_view(),name="list-lessons"),
    path("lesson/<int:pk>", views.userLessonsPage, name="lesson"),

    path("upload-course", views.uploadCourse, name="upload-course"),
    path("upload-episodes/<int:pk>", views.uploadEpisodes, name="upload-episodes"),

    path('delete-course/<int:pk>', views.deleteCourse, name='delete-course'),
    
    path("my-uploaded-courses-list", views.myUploadedCoursesList, name="my-uploaded-courses")
]