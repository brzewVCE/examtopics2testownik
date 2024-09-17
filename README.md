# Script to scrape data from examtopics into Testownik format

## 1: Get questions from examtopic site
- Add ```view-source:``` before site address and press Enter
- Right click and **select file format as HTML ONLY, other options WILL NOT WORK**
- Save it to html directory
- Repeat if necessary

## 2: Run the script
- Open repo directory in commandline
- Install dependencies
```pip install -r requirements.txt```
- Run the script with python
```python ./main.py```

## 3: Open results in testownik
Testownik can be found in [this Github repo](https://github.com/kumalg/testownik-electron)
- from testownik app open the ```testo``` directory containing all the generated questions
