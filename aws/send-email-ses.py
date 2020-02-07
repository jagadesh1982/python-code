#!/usr/bin/python

# Send an Email Using Aws Ses, by 

import boto3

# Create SES client
ses = boto3.client('ses',region_name='eu-west-1')

response = ses.send_templated_email(
  Source='jagadishm.middleware@gmail.com',
  Destination={
    'ToAddresses': [
      'jagadish.manchala@gmail.com',
    ],
    'CcAddresses': [
      'jagadish.manchala@gmail.com',
    ]
  },
  ReplyToAddresses=[
    'importantmail82@gmail.com',
  ],
  Template='test-template',
  TemplateData='{ \"REPLACEMENT_TAG_NAME\":\"REPLACEMENT_VALUE\" }'
)

print(response)

