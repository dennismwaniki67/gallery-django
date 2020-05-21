from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.dennis= Editor(first_name = 'Dennis', last_name ='Mwaniki', email ='dennismwaniki67@gmail.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.dennis,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.dennis.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
