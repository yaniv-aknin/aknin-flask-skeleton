# aknin-flask-skeleton

Usually I don't like using other people's skeleton projects, but I do learn some from reading them. So I figured I'd post my skeleton Flask project. I'm not that much of a flask veteran, but I'm fairly happy with this skeleton and I hope so will you.

## Features

This skeleton comes pre-baked with:

1. `flask-assets` - configured to handle SCSS and CoffeeScript
2. `flask-restful` - my choice of RESTful API maker for flask
3. `flask-sqlalchemy` - by default configured to use a local Postgres database
4. `flask-script` - the basics plus a simple `recreatedb` command
5. CoffeeScript's compiler at the client side when in debug mode. Helps with sketching stuff.
6. basic directory structure for statics and templates, handling of favicon.ico and robots.txt

In other words, this skeleton is geared towards full features websites with an SQL backing store and substantial frontend code (that's what the assets and API are for). I guess an obvious omission here is Alembic, SQLAlchemy's migration toolkit.

## Installation

You could do something like:

    $ virtualenv .venv
    $ source .venv/bin/activate
    $ source runcommands.sh
    $ pip install -r requirements.txt
    $ ./manage.py runserver

But you'd be happier if you just ran `source <(curl sandalstrap.aknin.name)`, which does the above. `sandalstrap` is my suggested Python application directory bootstrapper. It will patch the created virtualenv to always source `runcommands.sh` when it's activated (p.s.: only shell activator is patched).

## Opinions

Skeleton projects are opinionated by nature. Beyond package selection (see above in *Features*) Here's a quick rundown of the 'opinions' I'm shoving down your throat if you choose to use this skeleton:

1. Configuration should come from the environment. Hence the `runcommands.sh` file. You can and should put development (read: worthless) credentials or other configuration items there, and should *not* load it in production. Let your production deployment environment (be it something you concocted or something like Heroku or AWS Beanstalk) be in charge of setting these environment variables for you. When it's time to deploy, read `runcommands.sh` for an idea of what's necessary from your production environment. If you're working in a team, and you want some machine-local settings for *your* environment, just write them in `runcommands.local.sh` which will be sourced from `runcommands.sh`. I really drank @hirodusk's awesome [cool-aid](http://www.12factor.net/) about this.

2. Usually when splitting `app.py` into `views.py`, `models.py` etc, you will need to solve the problem of circular dependency (views need the app to register on, the app must import the views so registration will happen). Since app creation code is usually shorter than all your views and all your models etc, I prefer putting the app in a factory. But since I also want to be able to just `from app import app` in modules that need it, I set a global `app` variable in `app.py`. This of course makes less (read: no) sense in an app multi-tenancy environment.

3. A couple of words on layout:
First, I suggest you should avoid project-specific words in your code and layout (i.e, if working on the product *Angus* for the company *McDonalds*, refrain, up to reason, from using either of these terms in your code base. Names change. Hence, when cloning this skeleton into a real project, I suggest sticking with `application` for the core application Python package, and probably something equally bland if you feel you need to create a non-application specific library package next to it.
Second, The static directory layout is borrowed from what I read about RoR. Your app code should go in `static/js/app`. Library code (which you wrote, but is independent from your application logic and problem domain) should go in `static/js/lib`. 3rd party code you choose to streamline into a single JS (say, `backbone.js`) should go in `static/js/vendor`. 
