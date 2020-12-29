from http import HTTPStatus

from django.db import IntegrityError
from django.test import TestCase
from django.urls import resolve

from .models import Message
from .views import contact_view


class ViewContactTestCase(TestCase):

    def setUp(self):
        Message.objects.create(
            name='John Foo',
            email='john@foo.com',
            subject='test subject',
            content='test content'
        )

    def test_ok_url_contact(self):
        view = resolve('/contact/')
        self.assertEquals(view.func, contact_view)

    def test_ok_form_contact(self):
        response = self.client.post(
            '/contact/',
            data={'name': 'Jack Baz',
                  'email': 'jack@baz.com',
                  'subject': 'jack test subject',
                  'content': 'jack test content'
                  }
        )
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(Message.objects.get(name='Jack Baz').__str__(), 'jack test subject')


class ModelMessageTestCase(TestCase):

    def setUp(self):
        Message.objects.create(
            name='John Foo',
            email='john@foo.com',
            subject='test subject',
            content='test content'
        )

    def test_ok_message_str(self):
        message = Message.objects.get(name='John Foo')
        self.assertEquals(message.__str__(), 'test subject')

    def test_fail_message_empty(self):
        self.assertRaises(IntegrityError, Message.objects.create)

    def test_fail_message_email_empty(self):
        self.assertRaises(IntegrityError, Message.objects.create,
                          subject='test subject',
                          content='test content')

    def test_fail_message_subject_empty(self):
        self.assertRaises(IntegrityError, Message.objects.create,
                          email='john@foo.com',
                          content='test content')

    def test_fail_message_content_empty(self):
        self.assertRaises(IntegrityError, Message.objects.create,
                          email='john@foo.com',
                          subject='test subject')
