#Google Search Analytics Classification

## Data Sources:

1. Hourly  RSS feed fetch from  : https://trends.google.com/trends/trendingsearches/daily/rss?geo=US
2. Google NLP classifier - categories
https://cloud.google.com/natural-language/docs/categories
Try finding any othe ropen source repo as well
3. https://cloud.google.com/natural-language/pricing

#Libraries Used: 

- pip3 install pipenv
- pipenv install awsebcli
- pipenv install flask
- pipenv install SQLAlchemy
- pipenv install apscheduler
- pipenv install feedparser


#Notes:
1. Test API : https://cloud.google.com/natural-language#natural-language-api-demo
2. Upsert : https://docs.sqlalchemy.org/en/13/dialects/postgresql.html?highlight=conflict#sqlalchemy.dialects.postgresql.Insert.on_conflict_do_update.params.index_where
3. https://www.journaldev.com/23365/python-string-to-datetime-strptime
4. https://wiki.freepascal.org/RFC_1123_Time_Format
## Markdown

https://www.markdownguide.org/cheat-sheet/

##Pipenv:

# Pipenv Cheat Sheet

## Update requirements
```
pipenv lock -r > requirements.txt
```

## Install pipenv
```
pip3 install pipenv
```
## Activate
```
pipenv shell
```
## Check version of Python
```
python --version
```
## Check path
```
python
>>> import sys
>>> sys.executable
quit()
```
## Install a package
```
pipenv install camelcase
```
## Check local packages
```
pipenv lock -r
```
## Uninstall a package
```
pipenv uninstall camelcase
```
## Install a dev package
```
pipenv install nose --dev
```
## Install from requirements.txt
```
pipenv install -r ./requirements.txt
```
## Check security vulnerabilities
```
pipenv check
```
## Check dependency graph
```
pipenv graph
```
## Ignore pipfile
```
pipenv install --ignore-pipfile
```
## Set lockfile - before deployment
```
pipenv lock
```
## Exiting the virtualenv
```
exit
```
## Run with pipenv
```
pipenv run *
```