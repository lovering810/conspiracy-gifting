import os, cmd
import bottle
import requests
import misaka

from bottle import run, get, static_file, route, request, response

MAILGUN_URL = os.environ.get('MAILGUN_URL', None)
MAILGUN_FROM = os.environ.get('MAILGUN_FROM', None)
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', None)

SUBJECT_TEMPLATE = '{name} - Conspiracy Gifting'
BODY_TEMPLATE = '''
Your mission, should you choose to accept it, is to select the most awesome of gift(s) for {name}. The details of the mission are simple:

* Reply-all to share information or cool stories about {name}
* Synthesize information and begin discussion of *awesome gift ideas*
* Gift ideas should fall under any of the following:
  * Relevant to their interests
  * Thoughtful or meaningful
  * Funny or cutesy
  * Just plain cool
* Sum price of gift(s) must stay under $20.
* Once a concensus is met, an appointed member will arrange to get said gift(s).
* Be careful not to leak the information to {name}, check which thread you are replying to and the to/cc/bcc addresses before sending!
* Gifting will happen 12/17, so make sure any online orders are delivered by then.

Good luck!
'''

hard_code_members = [
        [{"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""}],
         [{"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""}],
         [{"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "" ,"email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""}],
         [{"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""},
          {"name": "", "email": ""}]
        ]

class ConspiracyCreator(cmd.Cmd):
  def get_conspirator():
      member = {}
      members = []

      details = input("Enter name, email:")

      while details != '':
          details = details.split(",")
          member["name"] = member[0]
          member["email"] = member[1]
          members.append(member)
          if details == '':
              return members

  def start_conspiracy(members):

      # validate the members!
      valid_members = True

      if not members or not isinstance(members, list):
          valid_members = False

      for member in members:
          if not (isinstance(member, dict) and member.get('name') and member.get('email')):
              valid_members = False

      if len(members) > MAX_MEMBERS:
          valid_members = False

      if not valid_members:
          response.status = 403
          return {
              'success': False,
              'errors': ['Provide some JSON like [{"name": "Joe", "email": "joe@example.com"}]!']
          }

      MAILGUN_ENDPOINT = '{}/messages'.format(MAILGUN_URL)

      # now email the members!
      for member in members:
          pruned = [m for m in members if m != member]
          to = u','.join([m['email'] for m in pruned])
          subject = SUBJECT_TEMPLATE.format(**member)
          body = BODY_TEMPLATE.format(**member)

          html = misaka.html(body)
          payload = {
              'from': 'Conspiracy Gifting HQ <{}>'.format(MAILGUN_FROM),
              'to': to,
              'subject': subject,
              'html': html
          }
          response = requests.post(MAILGUN_ENDPOINT, data=payload, auth=('api', MAILGUN_API_KEY))
          response.raise_for_status()

      return {
          'success': True
      }



