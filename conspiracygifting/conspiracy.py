import os, cmd
import bottle
import requests
import misaka

from bottle import run, get, static_file, route, request, response

class ConspiracyCreator:
  def __init__(self, mailgun_url, mailgun_from, mailgun_api_key, mailgun_endpoint, email_subject, email_body):
	'''Creates a ConspiracyCreator instance.
	Initializes with the following variables:
	mailgun_url       reads from .env file
	mailgun_from      reads from .env file
	mailgun_api_key   reads from .env file
	mailgun_endpoint  reads from .env file
	subject_template  the subject line of the generated email
	body_template     the body of the generated email
	max_members       the maximum number of conspirators
	'''
	self.mailgun_url = mailgun_url
	self.mailgun_from = mailgun_from
	self.mailgun_api_key = mailgun_api_key
	self.subject_template = email_subject
	self.body_template = email_body
	self.max_members = 100
	self.group_size = 9

  def _chunk_list(l, n):
	for i in xrange(0, len(l), n):
	  yield l[i:i+n]

  def validate_members(self, members):
	'''Takes members input and checks if
	the input is valid.
	The input must be a list of dicts.
	Each member must be a dict with keys "name" and "email".
	The maximum number of members is defined in max_members.
	'''
	self.members = members

	# start assuming the input is valid
	valid_members = True

	if not members or not isinstance(self.members, list):
	  # Check that there is input and the input is a list
	  valid_members = False

	for member in self.members:
	  if not (isinstance(member, dict) and member.get('name') and member.get('email')):
		# Check if each member is valid
		print str(member) + ' is not valid'
		valid_members = False

	if len(self.members) > self.max_members:
	  # Check that the number of members is valid
	  valid_members = False

	if not valid_members:
	  print 'provide some json like [{"name": "joe", "email": "joe@example.com"}]!'
	  return 'provide some json like [{"name": "joe", "email": "joe@example.com"}]!'
	else:
	  print 'Success!'

  def send_email(self):

	member_groups = _chunk_list(self.members)
	print list(member_groups)

	# now email the members!
	# for group in member_groups:
	  # for member in group:
		# pruned = [m for m in members if m != member]
		# print pruned
		# to = u','.join([m['email'] for m in pruned])
		# subject = self.email_subject.format(**member)
		# body = self.email_body.format(**member)

		# html = misaka.html(body)
		# payload = {
			# 'from': 'Conspiracy Gifting HQ <{}>'.format(self.mailgun_from),
			# 'to': to,
			# 'subject': subject,
			# 'html': html
		# }
		# response = requests.post(self.mailgun_endpoint, data=payload, auth=('api', self.mailgun_api_key))
		# response.raise_for_status()

	  # print 'Success'
	  # return 'Success'
