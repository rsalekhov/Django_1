from django.contrib import admin
from django.urls import path

from app.views import home_view, time_view, workdir_view

urlpatterns = [
    path('', home_view, name='home'),
    path('current_time/', time_view, name='current_time'),  # Раскомментируйте эту строку, если вы хотите добавить URL для current_time
    path('workdir/', workdir_view, name='workdir'),  # Раскомментируйте эту строку, если вы хотите добавить URL для workdir
    path('admin/', admin.site.urls),
]

