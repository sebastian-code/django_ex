from django. conf.urls import patterns, urls
from userprofiles.views import LoginView

urlpatterns = patterns('',
	url(r'^login/$', LoginView.as_view(), name='login'),
	
)