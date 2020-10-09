# COVID_Updater

Eventually we'll update the readme to be in the right
format, but for now, it'll just be a way for us to
talk about basic things

1. Firstly, I think it's a good idea to use virtual environments
    because it's good practice for every python project
    and we really don't know too much about Tweepy so it
    may update/install other packages and mess up your system-wide
    packages. (if you depend on them).
    https://docs.python.org/3/library/venv.html
    It basically creates a virtual environment with it's own site directories
    (packages) and package manager (pip). This way, if you install or update
    a package, for example "numpy", then not only does your project depend
    only your project's site directories, but it won't interfere with other
    site directories: System-wide vs. Project-wide

2. Secondly, I'm not too hip to Git and GitHub so I'm not exactly sure
    how the virtual environment plays into that, but I think the way to
    go is as follows:
    - As a collaborator, you want to clone the repository
    - create a virtual environment in that directory
    - after activating the virtual env, you can either install Tweepy via
        pip yourself, or use
        `pip install -r requirements.txt`
        This should work...
    - Now you're all good to go! Time for pull requests!

    This link has some more information for pulling and collaborating
    https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67
