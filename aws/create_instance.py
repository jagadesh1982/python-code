#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
 ImageId='ami-0adab12dcddc251ea',
 MinCount=1,
 MaxCount=1,
 InstanceType='t2.small')

print(instance[0].id)
