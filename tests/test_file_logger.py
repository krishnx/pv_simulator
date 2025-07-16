import os
import tempfile
from services.file_logger import FileLogger


def test_file_logger_writes_correct_format():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        logger = FileLogger(file_path=temp.name)
        logger.log({
            'timestamp': 1721144920.123,
            'meter': 5.0,
            'pv': 7.0,
            'net': 2.0
        })

    with open(temp.name) as f:
        content = f.read()
        assert '5.0' in content
        assert '7.0' in content
        assert '2.0' in content

    os.remove(temp.name)
