# python-final-project

## Installation
1. clone this repo
1. install requirements `pip install -r requirements.txt`

## Usage
```python app.py```
## Examples
```python app.py```
Open http://127.0.0.1:5000 using your browser. We have many routes.The main route is '/coin'  that has  input of some name of cryptocurrency. Had only one template of HTML file which named "index.html". Then there exists "/find" which have method allowed only "POST". Which have scrapper that finds all blogs or news and first of all it saves it then return the template with listes of news. Also we have '/db' route that shows the whole database within stored news and blogs url's and short summary. It has opportunity to delete all rows from database by going to '/db_delete_all'. 
To use application just go to '/coin' enter the name of crypto then press button 'send' after that you will receive all news in that WebPage. Also you should give personal token otherwise you can't get any news. So to get token please Login. If you provided token then it will give you all articles with summary of each of them.
Login page and Protected page. Login page has a form containing login and password fields where
an user is able to enter his or her data. If authorization process went successfully, 
route will return corresponding token, otherwise, it will show an error indicating that 
user with given data does not exists.

## License
MIT
