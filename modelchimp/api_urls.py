from django.conf.urls import include, url
from modelchimp.views.api import (project,
                                  ml_model,
                                  comment,
                                  invitation,
                                  decode_key,
                                  experiment_custom_object,
                                  experiment_mat_plot,
                                  project_dashboard,
                                  project_key,
                                  experiment_pull_params,
                                  experiment_image,
                                  experiment_label,
                                  experiment_param,
                                  experiment_metric,
                                  experiment_meta,
                                  experiment_code,
                                  experiment_gridsearch,
                                  experiment_asset,
                                  user)
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'project/$', project.ProjectAPI.as_view(), name='project'),
    url(r'project/(?P<project_id>\d+)/$', project.ProjectAPI.as_view(),
        name='project'),
    url(r'project/(?P<project_id>\d+)/dashboard/experiment-metric/$',
        project_dashboard.experiment_metric_chart,
        name='project_dashboard_metric_chart'),
    url(r'project/(?P<project_id>\d+)/dashboard/experiment-metric-filter/$',
        project_dashboard.experiment_metric_filter,
        name='project_dashboard_metric_filter'),
    url(r'project/(?P<project_id>\d+)/dashboard/experiment-duration/$',
        project_dashboard.experiment_duration_chart,
        name='project_dashboard_duration_chart'),
    url(r'project/(?P<project_id>\d+)/dashboard/experiment-duration-filter/$',
        project_dashboard.experiment_duration_filter,
        name='project_dashboard_duration_filter'),
    url(r'project/(?P<project_id>\d+)/dashboard/experiment-parameter-metric/$',
        project_dashboard.experiment_parameter_metric_chart,
        name='project_dashboard_parameter_metric_chart'),
    url(r'project/(?P<project_id>\d+)/dashboard/experiment-parameter-metric-filter/$',
        project_dashboard.experiment_parameter_metric_filter,
        name='project_dashboard_parameter_metric_filter'),
    url(r'project/key/(?P<project_id>\d+)/$',
        project_key.ProjectKeyAPI.as_view({'get': 'retrieve'}),
        name='project_dashboard_parameter_metric_filter'),
    url(r'ml-model/(?P<project_id>\d+)/$',ml_model.MLModelAPI.as_view(),
        name='ml_model'),
    url(r'ml-model/get-param/(?P<project_id>\d+)/$', ml_model.get_param_fields),
    url(r'ml-model/get-param-select-data/(?P<project_id>\d+)/$', ml_model.send_selected_param_data),
    url(r'create-experiment/(?P<project_id>\d+)/$', ml_model.CreateExperimentAPI.as_view(),
        name='create_experiment'),
    url(r'comment/(?P<model_id>\d+)$',  comment.CommentAPI.as_view(), name='comment_api'),
    url(r'decode-key/$', decode_key.decode_key,
        name='decode-key'),
    url(r'experiment-custom-object/create/(?P<project_id>\d+)/$',
        experiment_custom_object.ExperimentCustomObjectAPI.as_view(),
        name='experiment_custom_object_create'),
    url(r'experiment-custom-object/retrieve/(?P<project_id>\d+)/$',
        experiment_custom_object.ExperimentCustomObjectAPI.as_view(),
        name='experiment_custom_object_retrieve'),
    url(r'experiment-custom-object/details/(?P<model_id>\d+)/$',
        experiment_custom_object.ExperimentCustomObjectDetailAPI.as_view(),
        name='experiment_custom_object_details'),
    url(r'experiment-mat-plot/create/(?P<project_id>\d+)/$',
        experiment_mat_plot.ExperimentMatPlotAPI.as_view(),
        name='experiment_mat_plot_create'),
    url(r'experiment-mat-plot/details/(?P<model_id>\d+)/$',
        experiment_mat_plot.ExperimentMatPlotAPI.as_view(),
        name='experiment_mat_plot_details'),
    url(r'experiment-pull-param/$',
        experiment_pull_params.ExperimentPullParamAPI.as_view(),
        name='experiment_pull_params'),
    url(r'experiment-images/add-image/(?P<project_id>\d+)/$',
        experiment_image.ExperimentImageCreateAPI.as_view(),
        name='experiment_image_add_image'),
    url(r'experiment-images/data/(?P<model_id>\d+)/$',
        experiment_image.ExperimentImageListAPI.as_view(),
        name='experiment_image_data'),
    url(r'experiment-images/filter/(?P<model_id>\d+)/$',
        experiment_image.ExperimentImageFilterAPI.as_view(),
        name='experiment_image_filter'),
    url(r'experiment-label/(?P<model_id>\d+)/$',
        experiment_label.ExperimentLabelAPI.as_view(),
         name='experiment_label_create'),
    url(r'experiment-detail/(?P<model_id>\d+)/param$',
        experiment_param.ExperimentParamAPI.as_view({'get': 'retrieve'}),
         name='experiment_param'),
    url(r'experiment-detail/(?P<model_id>\d+)/metric$',
        experiment_metric.ExperimentMetricAPI.as_view({'get': 'retrieve'}),
         name='experiment_metric'),
    url(r'experiment-detail/(?P<model_id>\d+)/meta$',
        experiment_meta.ExperimentMetaAPI.as_view({'get': 'retrieve'}),
         name='experiment_meta'),
    url(r'experiment-detail/(?P<model_id>\d+)/code$',
        experiment_code.ExperimentCodeAPI.as_view({'get': 'retrieve'}),
         name='experiment_code'),
    url(r'experiment-detail/(?P<model_id>\d+)/object$',
        experiment_custom_object.ExperimentCustomObjectDetailAPI.as_view(),
        name='experiment_object'),
    url(r'experiment-detail/(?P<model_id>\d+)/gridsearch$',
        experiment_gridsearch.ExperimentGridSearchAPI.as_view({'get': 'retrieve'}),
        name='experiment_gridsearch'),
    url(r'experiment-detail/(?P<model_id>\d+)/asset$',
        experiment_asset.ExperimentAssetAPI.as_view(),
        name='experiment_asset'),
    url(r'experiment-detail/(?P<model_id>\d+)/asset/meta-fields/$',
        experiment_asset.get_asset_meta_fields,
        name='experiment_asset_meta'),
    url(r'user$',
        user.UserAPI.as_view({'get': 'retrieve', 'post': 'update'}),
         name='user'),
    url(r'register$',
        user.RegisterAPI.as_view({'post': 'create'}),
         name='register'),
    url(r'invite/create/(?P<project_id>\d+)/$', invitation.InviteAPI.as_view(),
         name='invite_create'),
    url(r'invite/(?P<invite_id>[0-9A-Za-z_\-]+)/$', invitation.InviteInfoAPI.as_view(),
         name='invite_info'),
    url(r'^rest-auth/password/reset/confirm/', user.PasswordResetConfirmAPIView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),

]
