import datetime as dt
from urllib.parse import urlparse, urljoin
import pandas as pd

import transformers
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
import tensorflow as tf

def find_all_links(args, url, rss, model, driver):
    """
    Returns all the URLs that are found on this website
    """
    date_hour = list()
    now = dt.datetime.now()

    if (len(url) < 1):
        raise Exception("Invalid url")

    input = str(url)

    # change the url format to https://ft.com
    _urlparse = urlparse(input)
    input = _urlparse.scheme + "://" + _urlparse.netloc


    ## For each <a> element, retrieve Text & Link
    pair_dict, _html = parse_urls(input)

    # TODO: start integration from here
    dict_df = pd.DataFrame(set(pair_dict.items()), columns=['title', 'content'])

    # retreive link and title 
    dict_df['link'] = dict_df['content'].apply(lambda x: x[0])
    dict_df['DOM'] = dict_df['content'].apply(lambda x: x[1])
    dict_df = dict_df.drop('content', axis=1)

    title_columns = dict_df.iloc[:, 0]

    # Load text classification model
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained(model)
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

    model_results = []

    # For each test sentence related to a link, apply the classifier and get a score from 0 to 1
    for index, row in dict_df.iterrows():
        test_sentence = row['title']
        predict_input = tokenizer.encode(test_sentence, truncation=True, padding=True, return_tensors="tf")
        tf_output = loaded_model.predict(predict_input)[0]
        tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
        model_results.append(tf_prediction[1])

    # Remove all links where N_words < 4
    for index, title in enumerate(title_columns):
        if (len(title.split()) < 4):
            model_results[index] = 0

    dict_df['prediction'] = model_results

    threshold = 0.01
    # selecting rows based on condition
    rslt_df = dict_df[dict_df['prediction'] >= threshold]

    rslt_df = rslt_df.drop(['prediction'], axis=1)
    print(rslt_df)

    # get html tree

    tree = html.fromstring(_html)

    a_dom = []

    for link in rslt_df['link']:
        path = urlparse(link).path

        if path == "":
            continue

        a_dom = a_dom + tree.xpath('//a[contains(@href, "' + path + '")]/..')

    dom_list = []

    for a in a_dom:

        if a is None:
            continue
        if a[0].tag != "a":
            continue

        dom_list.append(a)

    # build backpack (WSJTheme--headline--unZqjb45 	attribute=class 	count=1)
    bagpack = get_bagpack(dom_list)

    print(bagpack)

    # build attribute list (WSJTheme--headline--unZqjb45 	attribute=class 	count>1)
    liste_dom = get_attribute_list(dom_list, bagpack)

    ### CLUSTERING ###

    bag_of_words = []
    list_of_vectors = []

    # create bag of words
    for _, dom_df in liste_dom:
        for i in range(dom_df.count()['tag']):
            ref = dom_df['tag'][i] + "." + str(dom_df['parent'][i]) + "." + dom_df['attribute'][i] + "=" + \
                  dom_df['value'][i]
            bag_of_words.append(ref)

    bag_of_words = set(bag_of_words)

    # create vectors
    for _, dom_df in liste_dom:
        ref = ""
        for i in range(dom_df.count()['tag']):
            ref += dom_df['tag'][i] + "." + str(dom_df['parent'][i]) + "." + dom_df['attribute'][i] + "=" + \
                   dom_df['value'][i] + " "

        vector = []
        for w in bag_of_words:
            vector.append(ref.split().count(w))

        list_of_vectors.append(vector)

    ## PREDICTION ##
    X = np.array(list_of_vectors)
    db = DBSCAN(eps=0.5, min_samples=2, metric='cosine').fit(X)  # use cosine similarity to compute the distance

    db.fit(X)
    y_pred = db.fit_predict(X)

    ## CLUSTERS ##
    nb_cluster = y_pred.max() + 1
    print("Nb clusters: " + str(nb_cluster))

    threshold = 0.75  ## add to args
    list_simplified = []

    for i in range(0, nb_cluster):
        cl_vectors = X[y_pred == i]
        mean = cl_vectors.mean(axis=0)

        cl_simplified = np.array((mean > threshold) == True)
        list_simplified.append(cl_simplified)

    b_w = np.array(list(bag_of_words))

    for i in range(0, nb_cluster):
        print(b_w[list_simplified[i]])

        print("\n")

    # BUILD XPATH EXPRESSION
    xpath_list = to_xpath(nb_cluster, b_w, list_simplified)

    # FIND THE CORRECT LINKS
    _dom = []
    liste_href = []
    liste_dom = []
    ns = {"re": "http://exslt.org/regular-expressions"}

    for xpath in xpath_list:
        try:
            _dom = _dom + tree.xpath(xpath, namespaces=ns)
            print("expression validated: {}".format(xpath))
        except:
            print("Invalid expression: {}".format(xpath))


    for a_dom in _dom:
        href = a_dom.get('href')

        text = a_dom.text_content()

        if (not args.preserve_categories):
            if (len(text.split()) <= 4):
                continue  # skip

        # Handle limit case :if href starts with //domain_name
        if (href is not None and href[:2]) == '//':
            href = href[2:]
            href = href[href.find('/'):]

        if (href is not None and href[0] == '/'):
            href = input + href

        _urlparse = urlparse(href)

        # Match domain name ?
        if (args.match_domain_name):
            _tld = tldextract.extract(href)

            domain_name = urlparse(url).netloc
            if domain_name not in href:
                continue

        # Filter by extension
        find = re.search(r"\.(jpg|jpeg|svg|xml)$", _urlparse.path)

        if (find is not None):
            continue  # skip

        # Remove get parameters?
        if (args.remove_get_parameters):
            href = _urlparse.scheme + "://" + _urlparse.netloc + _urlparse.path
        liste_href.append(href)
        liste_dom.append(html.tostring(a_dom))
        date_hour.append(now.strftime("%d/%m/%Y %H:%M:%S"))

    result = pd.DataFrame({'URL': liste_href, 'DOM': liste_dom})
    result['DOM'] = result['DOM'].apply(lambda x: x.decode('utf-8'))

    true_name = list()
    for link in result['URL']:
        if not dict_df.loc[dict_df['link'] == link, 'title'].empty:
            title = dict_df.loc[dict_df['link'] == link, 'title'].iloc[0]
        else:
            title = ''
        true_name.append(title)

    result['title'] = true_name

    # display links

    result = pd.merge(dict_df[['link', 'title', 'DOM', 'prediction']].rename(columns={'link': 'URL'}), result,
                      on=['URL', 'title'], how='left',
                      indicator='predicted_class')

    result['DOM'] = np.where(result.predicted_class == 'both', result.DOM_y, result.DOM_x)
    result['predicted_class'] = np.where(result.predicted_class == 'both', 1, 0)

    result['annotated_class'] = ''

    # Pre-annotate links as positive links if matching the RSS feed
    if not pd.isnull(rss):
        d = feedparser.parse(rss)
        rss_links = [entry.link for entry in d.entries]
        result['annotated_class'] = result['URL'].apply(lambda x: '1' if x in rss_links else '')

    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    result['date-time'] = date_time

    columns = ['date-time', 'title', 'URL', 'DOM', 'predicted_class', 'annotated_class']

    return result[columns], date_time
