import xml.etree.ElementTree as et

def parse_data(file):

    # XML element tree object
    xml_tree = et.parse(file)

    # root element
    root = xml_tree.getroot()

    # list for news items
    newsitems = []

    # iterate through news items
    for item in root.findall('./channel/item'):

        # news dictionary
        news = {}

        # iterate through child elements of item
        for child in item:

            # get descriptions
            if (child.tag == 'description'):

                # add description to news dict
                news[child.tag] = str(child.text.encode('utf8'))

        # add news dict to newsitems
        newsitems.append(news)

    # return news items
    return newsitems

def save_data(newsitems, file):

    # write descriptions to text file
    with open(file, 'w') as f:

        for news in newsitems:

            for desc in news:

                description = news[desc]
                string = description[2:-1]

                # write description to file
                f.write(string + "\n\n")

newsitems = parse_data('data/soccer.xml')

save_data(newsitems, 'data/soccer.txt')
