import pytest

from letters.utils import get_letter_data


@pytest.mark.django_db
def test_get_letter_data(subscribers_factory):
    subscribers_factory.create_batch(10)
    assert len(get_letter_data()) == 10
