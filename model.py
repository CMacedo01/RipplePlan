import datetime

def get_month():
  month = datetime.datetime.now()
  return month.strftime("%B")


def get_year():
  year = datetime.datetime.now()
  return year.strftime("%Y")

def get_weekday():
  weekday = datetime.datetime.now()
  return weekday.strftime("%A")

def get_day():
  day = datetime.datetime.now()
  return day.strftime("%d")

def list_days():
  for i in range(13):
    i+=1
    html_tag_one = "<li<a href=\"#\" title=\""
    add_class = ""
    if i == 12: #get_day()
        add_class = 'class="selected"'

    html_tag = html_tag_one + str(i) + "\" data-value=\"" + str(i) + "\"" + add_class + ">" + str(i) + "</a></li>"
    return html_tag

def test_case():
  return "<li><a href=\"#\" title=\"Mon\" data-value=\"1\">Mon</a></li>"