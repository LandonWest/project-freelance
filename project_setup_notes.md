## README Notes

### Dependencies

It's recommended to use a node version manager { NVM: 'https://github.com/nvm-sh/nvm' })

npm / node : `nvm install node && nvm use node`
yarn       : `brew install yarn`   ({ brew: 'https://brew.sh/', yarn: '')

It's recommended to use a Python version manager: `brew install pyenv` { pyenv: 'https://github.com/pyenv/pyenv' }

python : `pyenv install 3.8.2`

### Project Setup

clone repo    : `git clone git@github.com:LandonWest/project-freelance.git`
cd into repo  :  "cd project-freelance"

install node modules locally : `npm install`

create the api venv      : `yarn api-create-venv`
install api dependencies : `yarn api-install`        # NOTE: it will source your venv and install, but when finished it takes you back out of your venv... so you'll have to `source api/venv/bin/activate` manually...

### Develop

##### Adding API Dependencies

##### Adding Client Dependencies
