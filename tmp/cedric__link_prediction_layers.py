# to be integrated inside apply_BERT_prediction



def predict_title_class(title):
    # predict_input = tokenizer.encode(title, truncation=True, padding=True, return_tensors="tf")
    # tf_output = loaded_model.predict(predict_input)[0]
    # tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
    # Load text classification model

    # get model_path depending on the language
    model_dirpath: str = utils.Global.BASE_BERT_MODEL_BASEPATH + \
        utils.Global.BERT_LANGUAGE_DIRS[self.source.language]
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained(model_dirpath)
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

    
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained(model_dirpath)
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

    inputs = tokenizer(title, return_tensors="pt")
    labels = torch.tensor([1]).unsqueeze(0)
    outputs = loaded_model(**inputs, labels=labels)

    return tf_prediction[1]

dframe['prediction'] = dframe["title"].apply(predict_title_class)




def apply_4_words_heuristic(title, prediction):
    if (len(title.split()) < 4):
        return 0
    else:
        return prediction

dframe['prediction'] = dframe.apply(lambda x: apply_4_words_heuristic(x.title, x.prediction), axis=1)






        # positive selection for clustering based on threshold
        threshold = 0.01
        rslt_df = dframe[dframe['prediction'] >= threshold]
        rslt_df = rslt_df.drop(['prediction'], axis=1)

        # get html tree
        tree = html.fromstring(self.source.html)

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

            # Handle limit case :if href starts with //domain_name
            if (href is not None and href[:2]) == '//':
                href = href[2:]
                href = href[href.find('/'):]

            if (href is not None and href[0] == '/'):
                href = input + href

            _urlparse = urlparse(href)

            # Filter by extension
            find = re.search(r"\.(jpg|jpeg|svg|xml)$", _urlparse.path)

            if (find is not None):
                continue  # skip

            # Remove get parameters?
            liste_href.append(href)
            liste_dom.append(html.tostring(a_dom))
            date_hour.append(now.strftime("%d/%m/%Y %H:%M:%S"))

        result = pd.DataFrame({'URL': liste_href})

        true_name = list()
        for link in result['URL']:
            if not dframe.loc[dframe['link'] == link, 'title'].empty:
                title = dframe.loc[dframe['link'] == link, 'title'].iloc[0]
            else:
                title = ''
            true_name.append(title)

        result['title'] = true_name

        # display links
        result = pd.merge(dframe[['link', 'title', 'prediction']].rename(columns={'link': 'URL'}), result,
                        on=['URL', 'title'], how='left',
                        indicator='predicted_class')

        result['predicted_class'] = np.where(result.predicted_class == 'both', 1, 0)

        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        result['datetime'] = date_time

        columns = ['datetime', 'title', 'URL', 'predicted_class']

        return result[columns]
    

