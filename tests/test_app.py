import unittest
import app
from unittest.mock import patch

class InitAppTest(unittest.TestCase):

    #разбирали на лекции
    def test_upload_date(self):
        dirs, docs = {}, []
        self.assertFalse(dirs)
        dirs, docs = app.update_date()
        self.assertTrue(dirs)
        self.assertTrue(docs)

class AppTest(unittest.TestCase):

    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.input', return_value='q'):
            with patch('app.update_date') as mock_ud:
                mock_ud.return_value = self.dirs, self.docs
                app.secretary_program_start()

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf('10006')
        self.assertNotIn('10006', self.dirs['2'])

    def test_add_new_document(self):
        before_len = len(self.docs)
        user_input = ['12345', 'pasp', 'UserName', '4']
        with patch('app.input', side_effect=user_input):
            app.add_new_doc()
        self.assertGreater(len(self.docs), before_len)
        self.assertIn('4', self.dirs)

    def test_get_owner_name(self):
        user_input = '10006'
        with patch('app.input', return_value=user_input):
            resp = app.get_doc_owner_name()
        self.assertEqual(resp, 'Аристарх Павлов')

    def test_add_new_shelf(self):
        user_input = '4'
        with patch('app.input', return_value=user_input):
            app.add_new_shelf(shelf_number='')
        self.assertIn(user_input, self.dirs)

    def test_append_doc_to_shelf(self):
        user_doc_number = '121094'
        user_shelf_number = '3'
        user_other_shelf_number = '4'
        app.append_doc_to_shelf(user_doc_number, user_shelf_number)
        self.assertIn(user_doc_number, self.dirs[user_shelf_number])
        app.append_doc_to_shelf(user_doc_number, user_other_shelf_number)
        self.assertIn(user_other_shelf_number, self.dirs)

    def test_delete_doc(self):
        user_input = '10006'
        with patch('app.input', return_value=user_input):
            app.delete_doc()
        self.assertNotIn('10006', self.docs)
        self.assertNotIn('10006', self.dirs)

