import os

from pybitrix24 import InboundWebhookClient

# You can try out this script with your own credentials
HOSTNAME = os.environ.get('HOSTNAME')
AUTH_CODE = os.environ.get('AUTH_CODE')


def main():
    # Instantiate a client that is designed for inbound webhooks
    b24 = InboundWebhookClient(HOSTNAME, AUTH_CODE)

    # Make a request
    print(b24.call("profile"))


if __name__ == '__main__':
    main()
