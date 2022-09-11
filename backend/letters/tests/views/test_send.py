import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture()
def send_letter_mock(mocker):
    return mocker.patch('letters.views.send_letter.delay')


def test_send(send_letter_mock):
    response = Client().get(reverse('send'))
    assert response.status_code == 302
    send_letter_mock.assert_called_once()
