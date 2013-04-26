from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import reverse

from cms.models.placeholdermodel import Placeholder
from cms.api import add_plugin         

from form_designer.contrib.cms_plugins.form_designer_form.models import CMSFormDefinition
from form_designer.models import FormDefinition
from form_designer import settings

class FormViewTests(TestCase):
    def setUp(self):
        # create a form
        self.form = FormDefinition(name = "testform")
        self.form.save()

    def test_default_form_template(self):
        response = self.client.get("/forms/testform/")   
        self.assertEquals(
            response.context["form_template_name"], 
            settings.DEFAULT_FORM_TEMPLATE
            ) 

    def test_custom_form_template(self):
        self.form.form_template_name = "html/formdefinition/forms/custom.html"
        self.form.save()
        response = self.client.get("/forms/testform/")   
        self.assertEquals(
            response.context["form_template_name"], 
            "html/formdefinition/forms/custom.html"
            ) 

class FormPluginTests(TestCase):
    def setUp(self):
        # create a placeholder
        self.placeholder = Placeholder(slot=u"some_slot")

        # create a fake context and request
        request = HttpRequest()
        self.context = {"request": request}

        # create a form
        self.form = FormDefinition(name = "testform")
        self.form.save()

        # add the plugin
        self.plugin = add_plugin(
            self.placeholder, 
            u"FormDesignerPlugin", 
            u"en",
            form_definition=self.form
            )
        self.plugin.save()

    def test_default_plugin_template(self):
        instance = self.plugin.get_plugin_instance()[1] 
        self.assertEquals(
            instance.render(self.context, self.plugin, self.placeholder)["form_template_name"], 
            settings.DEFAULT_FORM_TEMPLATE
            ) 
        
    def test_custom_plugin_template(self):
        self.form.form_template_name = "html/formdefinition/forms/custom.html"
        instance = self.plugin.get_plugin_instance()[1] 
        self.assertEquals(
            instance.render(self.context, self.plugin, self.placeholder)["form_template_name"], 
            "html/formdefinition/forms/custom.html"
            ) 
        