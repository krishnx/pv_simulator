import pytest
from unittest.mock import patch
from utils.retry_exceptions import retry


# 1. Should return immediately on success
def test_retry_success_immediate():
    @retry(max_retries=3, delay=0.01)
    def successful_func():
        return 'ok'

    assert successful_func() == 'ok'


# 2. Should retry once then succeed
def test_retry_once_then_success():
    attempts = {'count': 0}

    @retry(max_retries=3, delay=0.01)
    def flaky_func():
        if attempts['count'] < 1:
            attempts['count'] += 1
            raise ValueError('temporary fail')

        return 'recovered'

    assert flaky_func() == 'recovered'


# 3. Should raise after exhausting retries
def test_retry_exceeds_max_retries():
    @retry(max_retries=2, delay=0.01)
    def always_fails():
        raise RuntimeError('fail always')

    with pytest.raises(Exception) as excinfo:
        always_fails()

    assert 'Max retries reached' in str(excinfo.value)


# 4. Should not catch unexpected exception type
def test_retry_ignores_unexpected_exception():
    @retry(max_retries=3, delay=0.01, exception_types=(ValueError,))
    def unexpected_exception():
        raise TypeError('This should not be retried')

    with pytest.raises(TypeError):
        unexpected_exception()


# 5. Test logging on retry
@patch('utils.retry_exceptions.logger')
def test_retry_logs_warning(mock_logger):
    calls = {'count': 0}

    @retry(max_retries=2, delay=0.01)
    def flaky():
        calls['count'] += 1
        raise ValueError('logged failure')

    with pytest.raises(Exception):
        flaky()

    # Should have logged warnings twice
    assert mock_logger.warning.call_count == 2
