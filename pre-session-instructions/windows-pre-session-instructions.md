# MacOS Pre-session Instructions



### Install Windows Subsystem for Linux (WSL) - Windows only

https://learn.microsoft.com/en-us/windows/wsl/install

### Open WSL Terminal

Run this command

```
lsb_release -a
```

## Install Visual Studio Code

https://code.visualstudio.com/

### Install WSL Extension in Visual Studio Code

https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl

For full instructions use this

https://code.visualstudio.com/docs/remote/wsl

## Install `pyenv`

Install the necessary packages for `pyenv`

``` shell
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev
```

Run the command below.

``` shell
curl -fsSL https://pyenv.run | bash
```

This will take a while to install.

Add pyenv to bashrc

``` shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
```

Close all Terminal windows and open a new one.

Run the command below to check whether `pyenv` was successfully installed.

``` shell
pyenv --version
```

## Install Pipenv

``` shell
sudo apt update
sudo apt install -y pipx python3-venv
pipx install pipenv
pipx ensurepath
```

Set creation of virtual environments to be created in the project folder.

``` shell
grep -qxF 'export PIPENV_VENV_IN_PROJECT=1' ~/.bashrc || echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.bashrc
```

Close all Terminal windows and open a new one.

Run the command below to check whether `pipenv` has successfully installed.

``` shell
pipenv --version
```

## Install Python 3.13

Run the command below.

``` shell
pyenv install 3.13
```

Note: This will only install Python 3.13 but it will not modify the python version that is currently being used by the system.

## Clone this repository

Open the terminal and go to Home directory.

``` shell
cd ~
```

Clone this repository

``` shell
git clone https://github.com/thinklabph/computer-vision.git
```

## Installing Virtual Environment and Dependencies

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

# Preload the Computer Vision Models

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

