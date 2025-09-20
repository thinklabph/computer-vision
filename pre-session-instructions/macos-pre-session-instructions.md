# MacOS Pre-session Instructions


# Make sure that `pipenv` will create the virtual environment in the project folder
```
grep -qxF 'export PIPENV_VENV_IN_PROJECT=1' ~/.zshrc || echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.zshrc
```

Reload the shell

```
source ~/.zshrc
```

Check that the virtual environment will be created in the project folder

```
echo $PIPENV_VENV_IN_PROJECT
```

This should output `1`.


Create the Virtual Environment and install the necessary python packages
```
pipenv install --dev
```

Activate the Pipenv Virtual environment

```
pipenv shell
```

Deactivate the Pipenv Virtual environment



Check which Pipenv environment is being used.

```
pipenv --venv
```

If the Pipenv environment is located in `~/.local/share/virtualenvs/<project-env-name>` then this is a user based environment. This is not what we want.

We want a virtual environment that is created inside the project folder because it keeps all dependencies isolated to the project, makes it easier to manage and share the environment with others, and avoids conflicts with global or user-based Python packages.

Remove the user based Pipenv environment

```
pipenv --rm
```

