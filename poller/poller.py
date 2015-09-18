import requests
import logging
from functools import partial

url = 'http://localhost:10799/bbdspipereadsvc'
logger = logging.getLogger(__name__)


def build_request(name, session_id):

    pass

def process(messages):
    pass


def handler_builder(name):

    def handle_poll(poll):
        if poll:
            map(process, poll['messages'])

    def handle_error(error):
        if error:
            logger.error(error)

    handlers = {
        'poll': handle_poll,
        'error': handle_error
    }
    return handlers.get(name)


def create_session_id(http_session):
    response = http_session.post(url, data=build_request('createSession', session_id))
    return response['createSession']['sessionId']


def close_session(http_session, session_id):
    http_session.post(url, data=build_request('closeSession', session_id))


def poll(http_session, session_id):
    response = http_session.post(url, data=build_request('poll', session_id))
    map(handler_builder('poll'), response['poll'])
    map(handler_builder('error'), response['error'])


def ack(http_session, session_id):
    response = http_session.post(url, data=build_request('ack', session_id))
    map(handler_builder('ack'), response['poll'])


with requests.Session() as http_session:
    for session_id in iter(partial(create_session_id(http_session=http_session)), None):
        poll_with_session_id = partial(poll, http_session=http_session, session_id=session_id)
        for result in iter(poll_with_session_id, None):
            if result > 0:
                ack(http_session, session_id)
        close_session(http_session=http_session, session_id=session_id)
