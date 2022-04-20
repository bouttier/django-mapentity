from django.test import TestCase

from mapentity.forms import MapEntityForm
from ..models import DummyModel


class DummyForm(MapEntityForm):
    class Meta:
        model = DummyModel
        fields = '__all__'


class MapEntityFormTest(TestCase):

    def test_can_delete_actions(self):
        sample_object = DummyModel.objects.create()
        delete_url = sample_object.get_delete_url()
        form = DummyForm(instance=sample_object)
        self.assertTrue(form.can_delete)
        self.assertTrue(('<a class="btn btn-danger delete" href="%s">' % delete_url) in form.helper.layout[1][0].html)

        form = DummyForm(instance=sample_object, can_delete=False)
        self.assertFalse(form.can_delete)
        self.assertTrue('<a class="btn disabled delete" href="#">' in form.helper.layout[1][0].html)

    def test_max_characters(self):
        """Test if help text is set with MAX_CHARACTERS setting"""
        sample_object = DummyModel.objects.create()
        form = DummyForm(instance=sample_object)
        self.assertIn('1200 characters maximum recommended', form.fields['description'].help_text)
