from distutils.util import strtobool

from workfront_bridge.blocks.base import WFBlockParser
from workfront_bridge.blocks.display.ad_group_setup import WFDisplayAdGroupSetupBlock


class TTDBuilderMixin(object):
    def build_ad_groups(self, create_ad_group_class, creative_upload_class):
        ad_group_setup_blocks = []

        creative_native_params = getattr(self, "creative_native_params", [])
        for ad_group in self.ad_groups:
            ad_group_setup_block = WFDisplayAdGroupSetupBlock()

            for creative in ad_group['creatives']:
                creative_upload_dict = {k: creative[k]
                                        for k in (self.creative_upload_params
                                                  + creative_native_params)
                                        if k in creative}
                ad_group_setup_block.add_creative(block_class=creative_upload_class,
                                                  **creative_upload_dict)

            ad_group_setup_block.add_ad_group(block_class=create_ad_group_class,
                                              **ad_group)
            ad_group_setup_blocks.append(ad_group_setup_block)
            ad_group.update({
                'start_date_inclusive_utc': self._start_date_inclusive_utc,
                'end_date_exclusive_utc': self._end_date_exclusive_utc,
                'campaign_name': self._campaign_name,
                'campaign_overview': self._campaign_overview,
                'partner_cost_percentage_fee': self._partner_cost_percentage_fee,
                'availability': self._availability,
                'auto_allocator': self._auto_allocator,
                'ctv_targeting_and_attribution': self._ctv_targeting_and_attribution,
                'pacing_mode': self._pacing_mode,
                'partner_cpm_fee_amount': self._partner_cpm_fee_amount,
                'partner_cpm_fee_currency': self._partner_cpm_fee_currency,
                'partner_cpc_fee_amount': self._partner_cpc_fee_amount,
                'partner_cpc_fee_currency': self._partner_cpc_fee_currency,
                'max_bid_amount': self._max_bid_amount,
                'budget_in_impressions_pre_calc': self._budget_in_impressions_pre_calc,
                'daily_target_in_advertiser_currency': self._daily_target_in_advertiser_currency,
                'daily_target_in_impressions': self._daily_target_in_impressions,
            })
        return ad_group_setup_blocks

    def revise_ad_group(self, wf_project, ttd_adgroup_id, ttd_crt_ids_to_archive,
                        crts_to_upload):
        ad_group_setup_block = WFDisplayAdGroupSetupBlock()

        # Set TTDAdGroupID
        project_params = wf_project.get_param_values()
        is_mcrt = bool(strtobool(project_params["MultipleAdGroups"]))
        if is_mcrt:
            ad_group_setup_block.set_parameter(
                "Ad Group Setup",
                "TTDAdGroupID",
                ttd_adgroup_id,
            )
        else:
            wf_project.set_param_values({
                "TTDAdGroupID": ttd_adgroup_id,
            })

        # Archive deprecated creatives
        ad_group_setup_block.archive_creative(
            ttd_creative_id=",".join(ttd_crt_ids_to_archive)
        )

        # Upload new creatives
        creative_native_params = getattr(self, "creative_native_params", [])
        for creative in crts_to_upload:
            creative_upload_dict = {k: creative[k]
                                    for k in (self.creative_upload_params
                                              + creative_native_params)
                                    if k in creative}
            ad_group_setup_block.add_creative(block_class=self.creative_upload_class,
                                              **creative_upload_dict)

        # Add task to update AdGroup with new TTD creative ids
        ad_group_setup_block.update_ad_group()

        parser = WFBlockParser(self.wf)
        parser.attach_to_project(wf_project, ad_group_setup_block)
        return wf_project

    def ad_groups_build_and_attach(self, wf_project):
        ad_group_setup_blocks = self.build_ad_groups(
            create_ad_group_class=self.create_ad_group_class,
            creative_upload_class=self.creative_upload_class,
        )
        parser = WFBlockParser(self.wf)
        for block in ad_group_setup_blocks:
            wf_project = parser.attach_to_project(wf_project, block)
        return wf_project
