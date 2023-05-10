SELECT DISTINCT
    O.ACCOUNT_ID AS "ACCOUNT_ID"
    ,O.OPPORTUNITY_STATUS_CODE AS "OPPORTUNITY_STATUS_CODE"
    ,O.OPPORTUNITY_OWNER_ID AS "OPPORTUNITY_OWNER_ID"
    ,IC.FIRST_NAME AS "FIRST_NAME"
    ,IC.LAST_NAME AS "LAST_NAME"
    ,IC.TITLE AS "TITLE"
    ,IC.BRANCH AS "BRANCH"
    ,IC.EMAIL_ADDRESS AS "EMAIL_ADDRESS"
    ,O.INDUSTRY_CODE AS "INDUSTRY_CODE"
    ,O.LAST_MODIFICATION_DATE_TIME AS "LAST_MODIFICATION_DATE_TIME"
    ,O.OPPORTUNITY_DESCRIPTION AS "OPPORTUNITY_DESCRIPTION"
    ,O.OPPORTUNITY_SOLUTION AS "OPPORTUNITY_SOLUTION"
    ,O.OPPORTUNITY_STEP_PROGRESSION_CODE AS "OPPORTUNITY_STEP_PROGRESSION_CODE"
    ,O.OPPORTUNITY_TYPE_CODE AS "OPPORTUNITY_TYPE_CODE"
    ,O.OPPORTUNITY_ID AS "OPPORTUNITY_ID"
FROM
    SALES.OPPORTUNITY O
LEFT JOIN
    SALES.INTERNAL_CONTACT IC ON IC.EMPLOYEE_ID = O.OPPORTUNITY_OWNER_ID
WHERE
    O.ACCOUNT_ID = '${Account_Id}'
AND (DATE(O.LAST_MODIFICATION_DATE_TIME) >= DATE(DAYS(CURRENT_DATE) - 365))
AND (O.OPPORTUNITY_KEY IS NOT NULL)
AND (O.OPPORTUNITY_STATUS_CODE = '${OPPORTUNITY_STATUS_CODE}')
