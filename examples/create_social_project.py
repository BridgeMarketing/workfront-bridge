from workfront.workfront import Workfront
from workfront_bridge.projects import social_builder


wf = Workfront("notifications@wf.bridgemarketing.com", 'beef6060', 'thebridgecorp.sb01.workfront.com')
wf.login()
b = social_builder.SocialProjectBuilder(wf, "Test - Social project")
prj = b.build()
prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
print(prj)
