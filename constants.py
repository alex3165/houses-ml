HEADERS = {
    'id': 0,
    'price': 1,
    'date_of_transfer': 2,
    'postcode': 3,
    # D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
    'property_type': 4,
    # Y = a newly built property, N = an established residential building
    'old_new': 5,
    #  F = Freehold, L= Leasehold
    'duration': 6,
    # 	Primary Addressable Object Name. Typically the house number or name.
    'paon': 7,
    # Secondary Addressable Object Name. Where a property has been divided into separate units
    'saon': 8,
    'street': 9,
    'locality': 10,
    'town_city': 11,
    'district': 12,
    'county': 13,
    # A = Standard Price Paid entry, includes single residential property sold for full market value.
    # B = Additional Price Paid entry including transfers under a power of sale/repossessions,
    'ppd_category': 14,
    # Indicates additions, changes and deletions to the records.(see guide below).
    # A = Addition
    # C = Change
    # D = Delete.
    'record_status': 15
}

DEFAULT_CITY_FILTER = ['LONDON']
