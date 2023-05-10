SELECT DISTINCT
    M.MEETING_METHOD_CODE AS "MEETING_METHOD_CODE"
    ,LEFT(M.MEETING_START_DATE_TIME,10) AS "MEETING_START_DATE_TIME"
    ,M.MEETING_SUBJECT AS "MEETING_SUBJECT"
    ,M.OWNING_BRANCH_CODE AS "OWNING_BRANCH_CODE"
    ,M.OWNER_EMPLOYEE_ID AS "OWNER_EMPLOYEE_ID"
    ,IC.FIRST_NAME AS "FIRST_NAME"
    ,IC.LAST_NAME AS "LAST_NAME"
    ,IC.TITLE AS "TITLE"
    ,IC.BRANCH AS "BRANCH"
    ,IC.EMAIL_ADDRESS AS "EMAIL_ADDRESS"
    ,M.POST_MEETING_NOTES AS "POST_MEETING_NOTES"
FROM
    SALES.MEETING M
LEFT JOIN
    DIMENSIONS.NEW_CLIENT_DIMENSION N ON N.GCI = M.GCI_NUMBER
    AND M.STATUS_CODE = 'COMPLETED'
    AND DATE(M.MEETING_START_DATE_TIME) >= DATE(DAYS(CURRENT_DATE) - 365)
LEFT JOIN
    SALES.INTERNAL_CONTACT IC ON IC.EMPLOYEE_ID = M.OWNER_EMPLOYEE_ID
WHERE
    N.CLIENT_ACTIVE_YN = 'Y'
    AND (N.GCI LIKE 'G%' OR N.GCI LIKE '0%')
    AND (N.CUSTOMER_ORGANIZATION_ID = '${Account_Id}')
