import jenkins

j = jenkins.Jenkins('http://localhost:8080', 'admin', 'admin')
print j.get_jobs()


url=j.build_job_url('sample-java-job', parameters=None, token=None)
print url

last_build_number = j.get_job_info('sample-java-job')['lastCompletedBuild'] ['number']
print "last_build_number",last_build_number 


build_info=j.get_build_info('sample-java-job',last_build_number)
if build_info['result']=='FAILURE':
    print " Build Success "


build_info = j.get_build_info('sample-java-job', last_build_number)
print build_info
print j.get_resultset()
