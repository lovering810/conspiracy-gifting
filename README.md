## Conspiracy Gifting Email Generator

A simple command-line tool to generate emails to start a round of conspiracy gifting*.

### Installing and running

To install:
```bash
https://github.com/rcackerman/conspiracy-gifting.git
mkvirtualenv conspiracygifting
cd conspiracy-gifting
workon conspiracygifting # note that if you work in a virtualenv, you'll need to make sure your env variables are accessible to your virtualenv
pip install -r requirements.txt
python setup.py install
```

To use:
```bash
# with a list
conspiracycmd -l {"name": "Rebecca", "email": "rebecca@example.com"}, {"name": "Lawrence of Arabia", "email": "lawrence@thedesert.in"}

# with a json file
conspiracycmd -f list.json
```

And that's all there is!


*This is a project forked from Conspiracy Santa. I renamed it because I don't particularly celebrate Christmas. Feel free to fork and rename. Just do a find and replace.
