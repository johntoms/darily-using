import logging
import logstash
from logstash import handler_tcp, handler_udp
import sys

host = '192.168.168.121'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(handler_udp.LogstashHandler(host, port=5959, version=1))
# test_logger.addHandler(logstash.UDPLogstashHandler(host, 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info(b'python-logstash: test logstash info message.')
test_logger.warning(b'python-logstash: test logstash warning message.')

# add extra field to logstash message
# extra = {
# 'test_string': 'python version: ' + repr(sys.version_info),
# 'test_boolean': True,
# 'test_dict': {'a': 1, 'b': 'c'},
# 'test_float': 1.23,
# 'test_integer': 123,
# 'test_list': [1, 2, '3'],
# }
# test_logger.info('python-logstash: test extra fields', extra=extra)
