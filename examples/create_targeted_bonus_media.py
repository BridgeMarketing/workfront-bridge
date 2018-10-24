from workfront.workfront import Workfront
from workfront_bridge.projects import targeted_bonus_media_builder

wf = Workfront('notifications@wf.bridgemarketing.com',
               'beef6060',
               'thebridgecorp.sb01.workfront.com')

wf.login()

b = targeted_bonus_media_builder.TargetedBonusMediaProjectBuilder(
    wf,
    'Test Targeted Bonus Media Channel 2 (beta)')

prj = b.build()

prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})

print prj
