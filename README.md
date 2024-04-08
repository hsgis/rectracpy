# Rectracpy

Small wrapper abstraction library for interaction with Vermont System's API.

# Reservations

sadetail: filelinkcode1, filelinkcode2, filelink3

correlate to...

frfacility: FacilityClass, facilitylocation, facilitycode

see Facility Management and/or Facility Class Management...


Passs membership.

# Examples

Get reservations where ...
1) it is a court
2) location is Womble Park abbreviated 'WP'

    req = Request_Table(
            SessionID=sessionId,
            Fields="sadetail_filelinkcode3,sadetail_begindatetime,sadetail_enddatetime",
            Filters=[
                {"sadetail_filelink1_filter": "Court"},
                {"sadetail_filelink2_filter": "WP"},
                {"sadetail_begindatetime_filter": "gt"},
                {"sadetail_begindatetime_filterby": "gt"},
            ]
    )
    reservations = rec.searchTable("sadetail", req)


Get reservations where ...
1) it is a court
2) location is Womble Park abbreviated 'WP'

    # Get reservations where the begindatetime is greater than ('gt'), the provided datetime
    req = Request_Table(
            SessionID=sessionId,
            Fields="sadetail_filelinkcode3,sadetail_begindatetime,sadetail_enddatetime",
            Filters=[
                {"sadetail_begindatetime_filter": "gt"},
                {"sadetail_begindatetime_filterby": {start datetime}},
            ]
    )

    reservations = rec.searchTable("sadetail", req)
