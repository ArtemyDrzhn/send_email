import pytest

from letters.models import TrackedEmail
from letters.tasks import get_logs


@pytest.fixture()
def request_mailgun_api_mock(mocker, all_data_log):
    return mocker.patch(
        'letters.tasks.get_data_log', return_value=all_data_log
    )


@pytest.mark.django_db
def test_get_logs(request_mailgun_api_mock):
    initial_count = TrackedEmail.objects.count()
    get_logs()
    assert initial_count == 0
    assert TrackedEmail.objects.count() == 3
