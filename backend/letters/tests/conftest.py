import pytest


@pytest.fixture()
def all_data_log():
    return {
        "items": [
            {
                "event": "delivered",
                "id": "hK7mQVt1QtqRiOfQXta4sw",
                "timestamp": 1529692199.626182,
                "log-level": "info",
                "envelope": {
                    "transport": "smtp",
                    "sender": "sender@example.org",
                    "sending-ip": "123.123.123.123",
                    "targets": "john@example.com"
                },
                "flags": {
                    "is-routed": False,
                    "is-authenticated": False,
                    "is-system-test": False,
                    "is-test-mode": False
                },
                "delivery-status": {
                    "tls": True,
                    "mx-host": "aspmx.l.example.com",
                    "code": 250,
                    "description": "",
                    "session-seconds": 0.4367079734802246,
                    "utf8": True,
                    "attempt-no": 1,
                    "message": "OK",
                    "certificate-verified": True
                },
                "message": {
                    "headers": {
                        "to": "team@example.org",
                        "message-id": "20180622182958.1.48906CB188F1A454@exmple.org",
                        "from": "sender@exmple.org",
                        "subject": "Test Subject"
                    },
                    "attachments": [],
                    "size": 586
                },
                "storage": {
                    "url": "https://se.api.mailgun.net/v3/domains/example.org/messages/eyJwI...",
                    "key": "eyJwI..."
                },
                "recipient": "john@example.com",
                "recipient-domain": "example.com",
                "campaigns": [],
                "tags": [],
                "user-variables": {}
            },
            {
                "event": "accepted",
                "id": "jxVuhYlhReaK3QsggHfFRA",
                "timestamp": 1529692198.641821,
                "log-level": "info",
                "method": "smtp",
                "envelope": {
                    "targets": "team@example.org",
                    "transport": "smtp",
                    "sender": "sender@example.org"
                },
                "flags": {
                    "is-authenticated": False
                },
                "message": {
                    "headers": {
                        "to": "team@example.org",
                        "message-id": "20180622182958.1.48906CB188F1A454@exmple.org",
                        "from": "sender@example.org",
                        "subject": "Test Subject"
                    },
                    "attachments": [],
                    "recipients": [
                        "team@example.org"
                    ],
                    "size": 586
                },
                "storage": {
                    "url": "https://se.api.mailgun.net/v3/domains/example.org/messages/eyJwI...",
                    "key": "eyJwI..."
                },
                "recipient": "team@example.org",
                "recipient-domain": "example.org",
                "campaigns": [],
                "tags": [],
                "user-variables": {}
            },
            {
                "event": "opened",
                "id": "-laxIqj9QWubsjY_3pTq_g",
                "timestamp": 1377047343.042277,
                "log-level": "info",
                "recipient": "recipient@example.com",
                "geolocation": {
                    "country": "US",
                    "region": "Texas",
                    "city": "Austin"
                },
                "tags": [],
                "campaigns": [],
                "user-variables": {},
                "ip": "111.111.111.111",
                "client-info": {
                    "client-type": "mobile browser",
                    "client-os": "iOS",
                    "device-type": "mobile",
                    "client-name": "Mobile Safari",
                    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B143"
                },
                "message": {
                    "headers": {
                        "message-id": "20130821005614.19826.35976@samples.mailgun.org"
                    }
                },
            }

        ]
    }
