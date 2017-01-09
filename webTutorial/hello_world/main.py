# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import logging

form = """
<form  action="/testform">
  <!- On pressing enter this name and value entered in box gets appeneded to the url-->
  <!-file:///Users/shonababu/Documents/webTutorial/formsandInputs.html?test=dfsd-->
  <input type="password" name="q">
  <!-submit is same as pressing enter-->
  <input type="submit">
</form>
"""

bdayForm = """
<form method=post>
  When is your B'Day?
  <br>
  <label>
    Month
    <input type="text" name="month" value="%(month)s">
  </label>
  <label>
    Day
    <input type="text" name="day" value="%(day)s">
  </label>
  <label>
    Year
    <input type="text" name="year" value="%(year)s">
  </label>
  <div style = "color:red">%(error)s</div>
  <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self,error="" , month="", day="" , year =""):
      self.response.out.write(bdayForm % {"error": escape_html(error),
                                      "month": escape_html(month),
                                      "day": escape_html(day),
                                      "year": escape_html(year)})

    def get(self):
    	##by deafault this is text/html
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(form)
        self.write_form()
    def post(self):
      user_month  = self.request.get('month')
      user_day  = self.request.get('day')
      user_year  = self.request.get('year')

      month = valid_month(user_month)
      day  = valid_day(user_day)
      year = valid_year(user_year)


      logging.warn(user_month)
      logging.warn(month)
      logging.warn(day)
      if not (month and day and year):
        self.write_form("That is not a valid entry.",user_month,user_day,user_year)
      else:
        self.redirect("/thanks")

class TestHandlr(webapp2.RequestHandler):
	##this indicates method type = get/post
	def get(self):
	    #q = self.request.get("q")
	    #self.response.write(q)
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write(self.request)

class ThanksHandlr(webapp2.RequestHandler):
  ##this indicates method type = get/post
  def get(self):
      self.response.out.write("Thanks that was valid date")


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
# using dictionary to accomodate spelling mistake's
month_abbvs = dict((m[:3].lower(),m) for m in months)
def valid_month(month):  
  short_month = month[:3].lower()
  logging.warn(month_abbvs)
  logging.warn(short_month)
  return month_abbvs.get(short_month)


# is digit ensure's that input is indeed only digits
def valid_day(day):
  if day and day.isdigit():
    day = int(day)
    if day > 0 and day <=31:
      return day

# is digit ensure's that input is indeed only digits
def valid_year(year):
  if year and year.isdigit():
    year = int(year)
    if year >= 1900 and year <=2020:
      return year      

import cgi
def escape_html(s):
  return cgi.escape(s,quote=True)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform',TestHandlr),
    ('/thanks',ThanksHandlr)
], debug=True)
