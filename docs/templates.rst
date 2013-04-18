#########
Templates
#########

Note that many of the templates provided are simply there to give you the bare
functionality to get started. 

For example, the ``detail.html`` and ``plugin_detail`` templates place the
form's ``title`` in an ``<h2>``; this is unlikely to be exactly what you need.

Put any such templates that you want to override into your project's
``templates`` directory, and edit them there, rather than edit the ones in the
application.   

You may also need to attend to your site's templates - see "Handling messages"
below.

Form template
=============

A form's template is set in its ``form_template_name``.

If none is provided, ``form_designer.settings.DEFAULT_FORM_TEMPLATE`` will be
used (whch itself defaults to ``html/formdefinition/forms/as_p.html``).

When a form renders, it renders to the ``html/formdefinition/detail.html``
template. This *includes* ``form_template_name``, and *extends*
``html/formdefinition/base.html``.

In the case of a django CMS plugin, it renders to
``html/formdefinition/plugin_detail.html``.

Base template
=============

Unless you're using django CMS plugins to deliver your forms, you'll need to
override ``html/formdefinition/detail.html`` so that the forms Django Form
Designer publishes match your site's page structure and appearance.

Handling messages
-----------------

You should also make sure that your site's base templates are able to handle
the messages created by Django Form Designer.

The provided ``html/formdefinition/base.html`` shows one way to do this. 

There is currently an issue in the system that means messages will not be displayed correctly when using plugin forms, unless:

* the form has the ``HTTP redirect after successful submission`` option
  enabled
* ``form_designer.middleware.RedirectMiddleware`` is enabled in
  ``settings.MIDDLEWARE_CLASSES``
  
See: https://github.com/Raumkraut/django-form-designer/issues/7
