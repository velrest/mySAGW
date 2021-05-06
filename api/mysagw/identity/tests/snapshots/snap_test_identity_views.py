# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_identity_export[admin] 1"] = [
    [
        "first_name",
        "last_name",
        "localized_salutation",
        "language",
        "is_organisation",
        "organisation_name",
        "email",
        "additional_emails",
        "phone_numbers",
        "address_addition",
        "street_and_number",
        "po_box",
        "postcode",
        "town",
        "country",
    ],
    [
        "Carol",
        "Anderson",
        "",
        "de",
        0,
        "",
        "thomas86@yahoo.com",
        """cassandra17@hotmail.com
jonathan55@gmail.com
tonymata@hotmail.com""",
        """+41316558056
+41566278583
+41777769447""",
        "",
        "2805 Kristin Estate Apt. 842",
        "",
        "40940",
        "Jimenezview",
        "China",
    ],
    [
        "William",
        "Brown",
        "Monsieur",
        "fr",
        0,
        "",
        "chennicole@hotmail.com",
        """chadlong@green.com
justincain@williams-moody.com
utaylor@hotmail.com""",
        """+41779705140
+41312929485
+41561727655""",
        "",
        "6778 Parker Canyon Apt. 565",
        "",
        "44382",
        "Sandersview",
        "Nepal",
    ],
    [
        "Anthony",
        "Dawson",
        "Mrs.",
        "en",
        0,
        "",
        "carlcunningham@hardin.com",
        """adamsbryce@gmail.com
cherylkeller@hotmail.com
karen86@gmail.com""",
        """+41441099841
+41316299487
+41779957818""",
        "",
        "8671 Mitchell Grove",
        "",
        "14020",
        "Rachaelhaven",
        "Paraguay",
    ],
    [
        "Nicole",
        "Fields",
        "",
        "de",
        0,
        "",
        "larryrichmond@gmail.com",
        """lawrencejones@rosales-long.net
mwilson@lee.org
sanchezvictor@cortez-mitchell.info""",
        """+41415799371
+41417404672
+41760802375""",
        "",
        "408 Huff Freeway",
        "",
        "47813",
        "Cobbburgh",
        "Luxemburg",
    ],
    [
        "Ronald",
        "Hernandez",
        "",
        "de",
        0,
        "",
        "hallsean@chavez.com",
        """ijones@harris.com
joseph46@yahoo.com
michele02@hotmail.com""",
        """+41787187622
+41762222301
+41795211227""",
        "",
        "831 Powell Freeway Apt. 642",
        "",
        "27677",
        "North Justin",
        "Bangladesch",
    ],
    [
        "Justin",
        "Irwin",
        "",
        "de",
        0,
        "",
        "wrightapril@gmail.com",
        """david42@sanders.com
ljones@thompson.net
msnyder@yahoo.com""",
        """+41773498099
+41763628840
+41775944798""",
        "",
        "4377 Matthew Corners",
        "",
        "40848",
        "Lake Walter",
        "Singapur",
    ],
    [
        "Lori",
        "Joseph",
        "",
        "de",
        1,
        "Thomas and Sons",
        "tkennedy@gmail.com",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ],
    [
        "Thomas",
        "Martinez",
        "",
        "de",
        0,
        "",
        "sarahmalone@allen.com",
        """bryan87@kent-wright.com
jennifer21@hotmail.com
samuel75@gmail.com""",
        """+41795432280
+41317366555
+41787336714""",
        "",
        "48822 Daniel Ford",
        "",
        "93728",
        "Lake Robertahaven",
        "Mikronesien (Föderierte Staaten von)",
    ],
    [
        "Grace",
        "Mccoy",
        "",
        "de",
        0,
        "",
        "phyllis84@hotmail.com",
        """leachashley@yahoo.com
rachel63@mcclain.com
sdean@lane.com""",
        """+41313199552
+41566840210
+41767703937""",
        "",
        "1046 Jennifer Roads Suite 784",
        "",
        "63854",
        "Staceymouth",
        "China",
    ],
    [
        "Kimberly",
        "Stanley",
        "",
        "de",
        0,
        "",
        "jamesacosta@zimmerman.com",
        """brenda22@hotmail.com
mendozachristina@ayers-lawson.info
vgordon@yang-hill.org""",
        """+41414519945
+41316482941
+41319070673""",
        "",
        "55884 William Passage",
        "",
        "58917",
        "East Charlestown",
        "Guatemala",
    ],
    [
        "Karen",
        "Young",
        "",
        "de",
        0,
        "",
        "leerussell@hotmail.com",
        """hmolina@yahoo.com
justindominguez@gmail.com
lori16@gmail.com""",
        """+41445751864
+41418894603
+41778561623""",
        "",
        "9416 Maurice Centers",
        "",
        "59259",
        "Antonioville",
        "Liberia",
    ],
]

snapshots["test_identity_export_labels_context[admin] 1"] = [
    [
        {
            "address_addition": "",
            "country": "Paraguay",
            "first_name": "Carol",
            "last_name": "Anderson",
            "organisation_name": "",
            "po_box": "",
            "postcode": "14020",
            "street_and_number": "8671 Mitchell Grove",
            "town": "Rachaelhaven",
        },
        {
            "address_addition": "",
            "country": "Venezuela (Bolivarische Republik)",
            "first_name": "William",
            "last_name": "Brown",
            "organisation_name": "",
            "po_box": "",
            "postcode": "91635",
            "street_and_number": "660 Ramirez Forge",
            "town": "Zacharyview",
        },
        {
            "address_addition": "",
            "country": "Irak",
            "first_name": "Anthony",
            "last_name": "Dawson",
            "organisation_name": "",
            "po_box": "",
            "postcode": "64324",
            "street_and_number": "1126 Lam Streets Apt. 527",
            "town": "Thomasport",
        },
    ],
    [
        {
            "address_addition": "Haus der Akademien",
            "country": "Senegal",
            "first_name": "Nicole",
            "last_name": "Fields",
            "organisation_name": "SAGW",
            "po_box": "23",
            "postcode": "24545",
            "street_and_number": "004 Pena Freeway",
            "town": "New Lawrenceberg",
        },
        {
            "address_addition": "",
            "country": "Swasiland",
            "first_name": "Ronald",
            "last_name": "Hernandez",
            "organisation_name": "",
            "po_box": "",
            "postcode": "56363",
            "street_and_number": "10173 Warner Spur Apt. 385",
            "town": "Jeanberg",
        },
        {
            "address_addition": "",
            "country": "Schweiz",
            "first_name": "Justin",
            "last_name": "Irwin",
            "organisation_name": "",
            "po_box": "",
            "postcode": "56598",
            "street_and_number": "0356 Arroyo Isle Suite 694",
            "town": "North Sandraville",
        },
    ],
    [
        {
            "address_addition": "",
            "country": "Chile",
            "first_name": "Thomas",
            "last_name": "Martinez",
            "organisation_name": "",
            "po_box": "",
            "postcode": "37377",
            "street_and_number": "056 Blackwell Wall Apt. 785",
            "town": "Angelamouth",
        },
        {
            "address_addition": "",
            "country": "Kasachstan",
            "first_name": "Grace",
            "last_name": "Mccoy",
            "organisation_name": "",
            "po_box": "",
            "postcode": "03361",
            "street_and_number": "32812 Natasha Court",
            "town": "South Angelamouth",
        },
        {
            "address_addition": "",
            "country": "Liberia",
            "first_name": "Kimberly",
            "last_name": "Stanley",
            "organisation_name": "",
            "po_box": "",
            "postcode": "80832",
            "street_and_number": "10584 Moore Knolls",
            "town": "Rachelport",
        },
    ],
    [
        {
            "address_addition": "",
            "country": "Dominica",
            "first_name": "Karen",
            "last_name": "Young",
            "organisation_name": "",
            "po_box": "",
            "postcode": "69035",
            "street_and_number": "3129 Autumn Roads",
            "town": "Karamouth",
        }
    ],
]
