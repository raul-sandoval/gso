SELECT
    d.duns_number,
    d.country_name,
    d.domestic_ultimate_duns_number,
    d.global_ultimate_duns_number,
    d.hq_duns_number,
    d.parent_duns_number,
    n.gci,
    n.gci_name,
    n.addr_line1,
    n.addr_line2,
    n.city,
    n.state,
    n.zip,
    n.country,
    n.master_client_number,
    n.customer_organization_id,
    n.master_client_name AS account_name,
    CASE
        WHEN n.family_tree_apex_unique_yn = 'Y' THEN n.family_tree_apex_gci
        ELSE NULL
    END AS family_tree_apex_gci,
    CASE
        WHEN n.family_tree_apex_unique_yn = 'Y' THEN n.family_tree_apex_name
        ELSE NULL
    END AS family_tree_apex_name,
    m.owning_branch_code AS meeting_branch,
    b.country_name AS branch_country,
    COUNT(DISTINCT
        CASE
            WHEN m.meeting_method_code = 'INPERSON' THEN m.meeting_id
            ELSE NULL
        END
    ) AS in_person_meetings,
    COUNT(DISTINCT
        CASE
            WHEN m.meeting_method_code IN('PHONE','WEB') THEN m.meeting_id ELSE NULL
        END
    ) AS phone_meetings,
    o.owning_branch_code AS opportunity_branch,
    COUNT(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'WON' THEN o.opportunity_id
            ELSE NULL
        END
    ) AS won_opportunities,
    COUNT(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'ACTIVE' THEN o.opportunity_id
            ELSE NULL
        END
    ) AS active_opportunities,
    COUNT(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'LOST' THEN o.opportunity_id
            ELSE NULL
        END
    ) AS lost_opportunities,
    COUNT(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'ON_HOLD' THEN o.opportunity_id
            ELSE NULL
        END
    ) AS on_hold_opportunities,
    SUM(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'WON' THEN (
                CASE
                    WHEN o.estimated_total_monthly_revenue_from_service_items_amount IS NOT NULL THEN o.estimated_total_monthly_revenue_from_service_items_amount
                    ELSE o.user_estimated_total_monthly_revenue_amount
                END
            )
            ELSE NULL
        END
    ) AS won_opportunities_est_revenue,
    SUM(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'ACTIVE' THEN (
                CASE
                    WHEN o.estimated_total_monthly_revenue_from_service_items_amount IS NOT NULL THEN o.estimated_total_monthly_revenue_from_service_items_amount
                    ELSE o.user_estimated_total_monthly_revenue_amount
                END
            )
            ELSE NULL
        END
    ) AS active_opportunities_est_rev,
    SUM(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'LOST' THEN (
                CASE
                    WHEN o.estimated_total_monthly_revenue_from_service_items_amount IS NOT NULL THEN o.estimated_total_monthly_revenue_from_service_items_amount
                    ELSE o.user_estimated_total_monthly_revenue_amount
                END
            )
            ELSE NULL
        END
    ) AS lost_opportunities_est_rev,
    SUM(DISTINCT
        CASE
            WHEN o.opportunity_status_code = 'ON_HOLD' THEN (
                CASE
                    WHEN o.estimated_total_monthly_revenue_from_service_items_amount IS NOT NULL THEN o.estimated_total_monthly_revenue_from_service_items_amount
                    ELSE o.user_estimated_total_monthly_revenue_amount
                END
            )
            ELSE NULL
        END
    ) AS on_hold_opportunities_est_rev,
    COUNT(DISTINCT m.meeting_primary_external_contact_id) AS no_of_contacts
FROM
    dimensions.new_client_dimension n
LEFT JOIN
    sales.duns_market_insight d ON n.duns_number = d.duns_number
LEFT JOIN
    sales.meeting m ON n.gci = m.gci_number AND m.status_code = 'COMPLETED' AND DATE(m.meeting_start_date_time) >= DATE(DAYS(CURRENT_DATE) - 365)
LEFT JOIN
    sales.opportunity o ON n.gci = o.gci_number AND m.owning_branch_code = o.owning_branch_code AND DATE(o.last_modification_date_time) >= DATE(DAYS(CURRENT_DATE) - 365)
LEFT JOIN
    dimensions.new_branch_dimension b ON m.owning_branch_code = b.branch_code AND operational_branch_indicator = 'Y'
WHERE
    n.client_active_yn = 'Y'
    AND
    (n.gci LIKE 'G%' OR n.gci LIKE '0%')
    AND
    (n.customer_organization_id = '${Account_Id}' OR n.master_client_number = '${Account_Id}')
GROUP BY
    d.duns_number,
    d.country_name,
    d.domestic_ultimate_duns_number,
    d.global_ultimate_duns_number,
    d.hq_duns_number,
    d.parent_duns_number,
    n.gci,
    n.gci_name,
    n.addr_line1,
    n.addr_line2,
    n.city,
    n.state,
    n.zip,
    n.country,
    n.master_client_number,
    n.customer_organization_id,
    n.master_client_name,
    CASE
        WHEN n.family_tree_apex_unique_yn = 'Y' THEN n.family_tree_apex_gci
        ELSE NULL
    END,
    CASE
        WHEN n.family_tree_apex_unique_yn = 'Y' THEN n.family_tree_apex_name
        ELSE NULL
    END,
    m.owning_branch_code,
    b.country_name,
    o.owning_branch_code