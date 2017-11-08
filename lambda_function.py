import os
import json
import requests


# Robin Powered configuration
robin_space_id = os.environ['ROBIN_SPACE_ID']
robin_user_id = os.environ['ROBIN_USER_ID']  # The Density Presence Bot user_id
robin_api_token = os.environ['ROBIN_API_TOKEN']
robin_session_ttl = 120  # TTL in seconds
robin_base_url = "https://api.robinpowered.com/v1.0"
robin_space_presence_endpoint = '{}/spaces/{}/presence'.format(robin_base_url, robin_space_id)

# Density API configuration
density_space_id = os.environ['DENSITY_SPACE_ID']


def lambda_handler(event, context):
    webhook = json.loads(event.get('body'))
    webhook_space_id = webhook.get('space_id')
    current_count = webhook.get('count')

    if webhook_space_id != density_space_id:
        return

    space_is_occupied = False
    if current_count > 0:
        space_is_occupied = True

    if space_is_occupied is True:
        send_presence_request()
    else:
        clear_presence_request()

    return


def send_presence_request():
    data = {
      'user_id': robin_user_id,
      'session_ttl': robin_session_ttl
    }
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Access-Token {}'.format(robin_api_token)
    }
    requests.post(
        robin_space_presence_endpoint,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    return


def clear_presence_request():
    data = {
      'user_id': robin_user_id
    }
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Access-Token {}'.format(robin_api_token)
    }
    requests.delete(
        robin_space_presence_endpoint,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    return
