import pytest

from letters.tasks import send_letter


@pytest.mark.django_db
def test_send_letter(subscribers_factory, mailoutbox, settings):
    subscribers_factory.create_batch(10)
    send_letter()

    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    assert mail.subject == 'Subject'
    assert mail.to == [settings.EMAIL_TO]

