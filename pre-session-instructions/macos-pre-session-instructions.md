# MacOS Pre-session Instructions

## Install Visual Studio Code

https://code.visualstudio.com/

## Install `git`

https://github.com/git-guides/install-git

# Install `pyenv`

Open `Terminal` app.

Follow the instructions in the link below to install `pyenv`.

https://github.com/pyenv/pyenv?tab=readme-ov-file#macos

Restart the Terminal

``` shell
source ~/.zshrc
```

Check if `pyenv` has been successfully installed.

``` shell
pyenv --version     # pyenv 2.6.7
```

If the above command returned an error, run the command below to add `pyenv` to the PATH variables.

``` shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
```

# Install Python 3.13 via `pyenv`

``` shell
pyenv install 3.13
```

If you don't have a previous installation of python, run the command below. This will set the default version of Python to 3.13
``` shell
pyenv global 3.13
```

Verify has successfully run.

``` shell
python --version    # Python 3.13.7
pip --version       # pip 25.2 from /Users/.../python3.13/site-packages/pip (python 3.13)
```

## Install pipenv

``` shell
pip install pipenv
```

Make sure that `pipenv` will create the virtual environment in the project folder

``` shell
grep -qxF 'export PIPENV_VENV_IN_PROJECT=1' ~/.zshrc || echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.zshrc
```

Reload the shell

``` shell
source ~/.zshrc
```

## Clone this repository

Open the terminal and go to the Desktop directory.

``` shell
cd ~/Desktop
```

Clone this repository

``` shell
git clone https://github.com/thinklabph/computer-vision.git
```

## Install Virtual Environment and Dependencies

Go inside the project folder.

``` shell
cd computer-vision
```

Install Virtual Environment and it's dependencies

``` shell
pipenv install --dev
```

Check Python version before activating virtual environment

``` shell
python --version
```

Activate the virtual environment

``` shell
pipenv shell
```

Check Python version with activate virtual environment

``` shell
python --version
```

## Preload the Computer Vision Models

Run the command

``` shell
python 00_pre-session.py
```

This will download the computer vision models. Wait for it to finish downloading.


# ────────────────────────────────
# 🎉 You're all set! 🎉
# 
# See you in the **AI Computer Vision Workshop!**
# ────────────────────────────────



