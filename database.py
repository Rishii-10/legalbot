import pandas as pd
data = [['John', 'john123@gmail.com', 'abc123'],
        ['Jane', 'jane456@gmail.com', '123abc'],
        ['Jim', 'jim321@gmail.com', 'a1b2c3']]
df = pd.DataFrame(data, columns=['Name', 'Email', 'Password'])
print(df)

property_articles = [
    ('19', "Protection of certain rights regarding property"),
    ('31', "Compulsory acquisition of property"),
    ('300A', "Persons not to be compelled to be witnesses"),
    ('343', "Official language of the Union"),
    ('348', "Language to be used in representations for redress of grievances"),
    ('350A', "Facilities for instruction in mother-tongue at primary stage"),
    ('350B', "Special Officer for linguistic minorities"),
    ('372', "Bar to interference by courts in disputes arising out of certain treaties, agreements, etc."),
    ('372A', "Power of the President to adapt laws"),
    ('391', "Meaning of property vested in the Union")
]

family_laws_articles = [
    ('44', "Classes of persons to be deemed to be Scheduled Castes"),
    ('48', "Duties of the Prime Minister as respects the furnishing of information to the President, etc."),
    ('50', "Separation of the judiciary from the executive"),
    ('51', "Promotion of international peace and security"),
    ('51A', "Fundamental duties"),
    ('60', "Disputes relating to Waters of inter-State rivers or river valleys"),
    ('74', "Council of States"),
    ('75', "Duration of Houses of Parliament"),
    ('76', "Attorney General for India"),
    ('77', "Conduct of business of the Government of India")
]

road_rules_articles = [
    ('112', "Annual financial statement"),
    ('113', "Procedure in Parliament with respect to estimates"),
    ('114', "Appropriation Bills"),
    ('115', "Supplementary, additional or excess grants"),
    ('116', "Votes on account, votes of credit and exceptional grants"),
    ('117', "Special provisions as to financial Bills"),
    ('118', "Rules of procedure"),
    ('119', "Regulation by law of procedure in Parliament in relation to financial business"),
    ('120', "Language to be used in Parliament"),
    ('350B', "Special Officer for linguistic minorities")
]
all_articles = property_articles + family_laws_articles + road_rules_articles
df = pd.DataFrame(all_articles, columns=['Article Number', 'Article Description'])
df.loc[0:10, "Type"] = "property"
df.loc[10:20, "Type"] = "family"
df.loc[20:30, "Type"] = "road"
print(df)
