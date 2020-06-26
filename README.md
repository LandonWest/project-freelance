## Project Freelance

### Dependencies

It's recommended to use a node version manager (NVM: 'https://github.com/nvm-sh/nvm')

npm / node : `nvm install node && nvm use node`

yarn       : `brew install yarn`   (brew: 'https://brew.sh/',  yarn: 'https://classic.yarnpkg.com/en/docs/install/#mac-stable')

It's recommended to use a Python version manager: `brew install pyenv` (pyenv: 'https://github.com/pyenv/pyenv')

python : `pyenv install 3.8.2`

### Project Setup

clone repo                   : `git clone git@github.com:LandonWest/project-freelance.git`

cd into repo                 : `cd project-freelance`

install node modules locally : `npm install`

create the api venv          : `yarn api-create-venv`

install api dependencies     : `yarn api-install-req`   # NOTE: it will source your venv and install, but when finished it takes you back out of your venv... so you'll have to `source api/venv/bin/activate` manually to activate it again...

install the db               : `yarn api-setup-db`

### Develop

#### Database

We are using Flask-Migrate which is a wrapper to use Alembic for db migrations in Flask (see: https://flask-migrate.readthedocs.io/en/latest/#api-reference )

Using `venv` and from within `/api`:

Create a migration file : `flask db migrate -m "add or change something"`

*Make sure to import your new model in `api/app/__init__.py`

Run the migration       : `flask db upgrade`

Each time the database models change repeat the migrate and upgrade commands. (inverse is `flask db downgrade` # only for development!)

#### Adding Client Dependencies

TODO

#### Adding API Dependencies

TODO

#### Code Formatting & Linting

We are using `Black` for PEP8-compliant and uniformly-styled code ( see: https://github.com/psf/black )

This is enforced using `pre-commit` hooks for git. This will run `black` on any changed files when commiting code.

\*each team member _may_ need to run `pre-commit install` once for it to work?

There are some nice plugins for SublimeText3 for Linting with black:
<pre>
{
  'sublack': {
      'description': 'Black integration for SublimeText',
      'link': 'https://github.com/jgirardet/sublack'
  }
  'SublimeLinter-addon-black-for-flake': {
      'description': 'Automatically configure flake8 for black',
      'link': 'https://github.com/kaste/SublimeLinter-addon-black-for-flake'
  },
  'SublimeLinter': {
      'description': 'The code linting framework for Sublime Text 3',
      'link': 'https://github.com/SublimeLinter/SublimeLinter' 
  },
  'SublimeLinter-flake8': {
      'description': 'linter plugin for SublimeLinter provides an interface to flake8',
      'link': 'https://github.com/SublimeLinter/SublimeLinter-flake8'
  }
}
</pre>

- While getting used to using `Black` it's helpful to lint files frequently _before_ commiting, but you don't need to. `cmd + shift + p --> Sublack: Format file`
