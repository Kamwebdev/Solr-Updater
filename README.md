# Solr-Updater
The application allows for periodical updating of all indexes of the solr program

Usage
-----------

```
usage: solrUpdater.py [-h] [--ip IP] [--mode MODE] [--wait WAIT] [--debug]

optional arguments:
  -h, --help   show this help message and exit
  --ip IP      Solr serwer ip adres (default: 127.0.0.1)
  --mode MODE  Import mode: delta-import, full-import (default: full-import)
  --wait WAIT  Time between update next core (default: 0s)
  --debug      Show full response
```
Basic usage
```
python solrUpdater.py --mode delta-import
```
```
python solrUpdater.py --ip 10.0.0.1 --mode full-import --debug --wait 2
```
Linux requirements:
```
yum/apt install python-requests
```

You can add an app to cron for daily calling
```
0 1 * * * python /home/developer/solrUpdate.py
```
Tested on python 2.7
