# Monitor
[![CircleCI](https://circleci.com/gh/emoji-gen/web-main-monitor/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/web-main-monitor/tree/master)
[![Requirements Status](https://requires.io/github/emoji-gen/web-main-monitor/requirements.svg?branch=master)](https://requires.io/github/emoji-gen/web-main-monitor/requirements/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c9ac48a753454e1c8209d040ad26260c)](https://www.codacy.com/app/pinemz/web-main-monitor?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=emoji-gen/web-main-monitor&amp;utm_campaign=Badge_Grade)

:rotating_light: E2E monitoring by Headless Chrome for Emoji Generator

## Requirements

- Python `$(cat .python-version)`

## Getting started

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt

$ python server.py # Run server
$ python worker.py # Run worker
```

## Deployment
### Requirements

- [Heroku account](https://heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Commands

```bash
$ heroku create your-app-name
$ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-multi.git
$ git push heroku master
```

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja/)
