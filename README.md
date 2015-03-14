# URL Shortener

This is a simple little project I put together one night while bored at work.  It uses Python and Django.

## Words of Warning
Don't be dumb and spin this software up on production systems.  I haven't done any sort of load testing nor security testing.  There *shouldn't* be any issues, but it's not my fault if you break something.

## Installation
- Make sure you've got Python (2.x or 3.x) installed along with Django (1.7).
- Clone this repository and CD into that directory.
- Edit `shorturl/settings.py`
 - **Change `SECRET_KEY` to something else!**
  - Make sure `TIME_ZONE` is correct
- './manage.py migrate'
- './manage.py runserver'

## TODO
- uWSGI
- Webserver setup instructions (nginx and Apache)
- Make the UI not ugly.
