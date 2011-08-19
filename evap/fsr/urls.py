from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('fsr.views',
    url(r"^$", 'semester_index', name="fsr_root"),
    
    url(r"^semester$", 'semester_index'),
    url(r"^semester/create$", 'semester_create'),
    url(r"^semester/(\d+)$", 'semester_view'),
    url(r"^semester/(\d+)/create$", 'course_create'),
    url(r"^semester/(\d+)/edit$", 'semester_edit'),
    url(r"^semester/(\d+)/import$", 'semester_import'),
    url(r"^semester/(\d+)/(\d+)/edit$", 'course_edit'),
    
    url(r"^questiongroup$", 'questiongroup_index'),
    url(r"^questiongroup/create$", 'questiongroup_create'),
    url(r"^questiongroup/(\d+)$", 'questiongroup_view'),
    url(r"^questiongroup/(\d+)/edit$", 'questiongroup_edit'),
)