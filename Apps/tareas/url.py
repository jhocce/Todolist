from django.conf.urls import url
from .views import createtarea, agenda, tarea_detail, tarea_update_status, tarea_eliminar, tarea_editar


urlpatterns =[
	url(r'^tarea/crear/$', createtarea.as_view(), name="crear"),
	url(r'^agenda/$', agenda.as_view(), name="agenda"),
	url(r'^tarea/actualizar/$', tarea_update_status, name="tarea_update_status"),
	url(r'^tarea/editar/(?P<pk>[^/]+)/$', tarea_editar.as_view(), name="tarea_editar"),
	url(r'^tarea/eliminar/(?P<pk>[^/]+)/$', tarea_eliminar.as_view(), name="tarea_eliminar"),
	url(r'^tarea/(?P<pk>[^/]+)/$', tarea_detail.as_view(), name="tarea_detail"),
	

]