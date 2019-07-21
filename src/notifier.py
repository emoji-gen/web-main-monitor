# -*- coding: utf-8 -*-

import slackweb

class Notifier:
    def __init__(self, url):
        self.slack = slackweb.Slack(url=url)

    def notify(self, text):
        self.slack.notify(
            username='web-main-monitor',
            icon_emoji=':rotating_light:',
            attachments=[
                {
                    'color': 'danger',
                    'pretext': '<!channel>',
                    'text': str(text),
                },
            ]
        )
