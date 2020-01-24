from workfront.workfront import Workfront
from workfront_bridge.projects import targeted_bonus_media_builder
from datetime import datetime

wf = Workfront('notifications@wf.bridgemarketing.com',
               'beef6060',
               'thebridgecorp.sb01.workfront.com')

wf.login()

b = targeted_bonus_media_builder.TargetedBonusMediaProjectBuilder(
    wf,
    'Targeted Bonus Media Channel (DEMO)')
b.set_links(['https://k0ch.github.io/', 'https://k0ch.github.io/peppe'])
b.set_weights([50, 50])
b.set_links_ids([112, 225])

b.set_curve_type(1)
b.set_project_type('Display - Desktop & Mobile')
b.set_total_click_goal(20)
b.set_ttd_advertiser_id('xc7votu')
b.set_ttd_bonus_media_advertiser_id('xc7votu')
b.set_lr_account_id('xc7votu')
b.set_lr_bonus_media_account_id('xc7votu')
b.set_start_date_inclusive_utc(datetime.utcnow())
b.set_image_s3_url('s3://bridge-file-assets/API_files/orderID_10000129/Channel_2/mobile_banner.png')
b.set_landing_page_url('http://dummy.com')

b.set_adg_base_bid_amount(1.12)
b.set_adg_max_bid_amount(2.25)

b.set_budget_in_impressions_pre_calc(80000)
b.set_open_tier('O1')
b.set_open_tier_value(0.10)
b.set_click_tier('CL')
b.set_click_tier_value(0.05)
b.set_overage(True)
b.set_campaign_type("CPM Deployment")  # Options are: Match and Deploy | Reblast | CPM Deployment
b.geo_target = "State"
b.geo_target_state = ["Alaska", "Connecticut"]

prj = b.build()

prj.set_fields({"portfolioID": "5b45ff9b000aa3a5db15b2e269976a4c"})
prj.set_fields({"programID": "5c4629f700440656e233af5c28a1bc99"})

print prj
