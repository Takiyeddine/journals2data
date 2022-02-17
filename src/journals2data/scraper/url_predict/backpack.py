import pandas as pd
import re

def get_bagpack(dom_list):
    """
    Build bagpack: (WSJTheme--headline--unZqjb45 	attribute=class 	count=1)
    """

    bag_pack = pd.DataFrame(columns=['attribute', 'count'])

    for dom in dom_list:
        
        parent = dom
        child = dom[0]

        parent_attributes = parent.items()
        child_attributes = child.items()
            
        for attr, value in parent_attributes:
            for val in value.split(" "):
                
                if val.strip() == "":
                    continue

                try:
                    count = bag_pack.loc[(bag_pack.index == ''+val) & (bag_pack.attribute == attr) , 'count']
                    
                    if count.size > 0:
                        bag_pack.loc[(bag_pack.index == ''+val) & (bag_pack.attribute == attr), 'count'] = count[0] + 1 
                    else:
                        df = pd.DataFrame([(attr, 1)], columns=['attribute', 'count'], index=[val])
                        bag_pack = bag_pack.append(df)
                except:
                    df = pd.DataFrame([(attr, 1)], columns=['attribute', 'count'], index=[val])
                    bag_pack = bag_pack.append(df)

        for attr, value in child_attributes:

            # the href attribute should not be taken into account
            if attr == "href":
                continue
                
            for val in value.split(" "): 
                if val.strip() == "":
                    continue

                try:
                    count = bag_pack.loc[(bag_pack.index == ''+val) & (bag_pack.attribute == attr) , 'count']
                    
                    if count.size > 0:
                        bag_pack.loc[(bag_pack.index == ''+val) & (bag_pack.attribute == attr), 'count'] = count[0] + 1 
                    else:
                        df = pd.DataFrame([(attr, 1)], columns=['attribute', 'count'], index=[val])
                        bag_pack = bag_pack.append(df)
                except Exception:
                    df = pd.DataFrame([(attr, 1)], columns=['attribute', 'count'], index=[val])
                    bag_pack = bag_pack.append(df)

    return bag_pack

def get_attribute_list(dom_list, bag_pack):
    p = re.compile("^.*[0-9]+.*$")
    r_h = re.compile("h[1-6]$")

    liste_dom = []

    for dom in dom_list:
        dom_df = pd.DataFrame(columns=['tag', 'attribute', 'value', 'parent'], )

        parent = dom
        child = dom[0]

        parent_attributes = parent.items()
        child_attributes = child.items()
            
        parent_name = parent.tag
        if r_h.match(parent_name):
            parent_name = "h" # transform h1, h2, ..., h6 to h
            
        for attr, value in parent_attributes:        
            for val in value.split(" "): # class="abc def" => value["abc", "def"]
                try:
                    if bag_pack.loc[val, 'count'] <= 1:
                        if p.match(val):
                            rg = re.sub(r'[0-9]+', '[0-9]+', val)
                            if bag_pack.filter(regex=rg, axis=0).count()['attribute'] > 1 :
                                # add attribute to the list
                                df = pd.DataFrame([(parent_name, attr, rg, 1)], columns=['tag', 'attribute', 'value', 'parent'])
                                dom_df = dom_df.append(df, ignore_index=True)
                            else:
                                print("L'attribut "+attr+"("+val+")"+" est inutile. Discard.")
                        else:
                            print("L'attribut "+attr+"("+val+")"+" est inutile. Discard.")
                    else:
                        df = pd.DataFrame([(parent_name, attr, val, 1)], columns=['tag', 'attribute', 'value', 'parent'])
                        dom_df = dom_df.append(df, ignore_index=True)
                except:
                    df = pd.DataFrame([(parent_name, attr, val, 1)], columns=['tag', 'attribute', 'value', 'parent'])
                    dom_df = dom_df.append(df, ignore_index=True)
                
        for attr, value in child_attributes:
            if attr == "href":
                continue
                
            for val in value.split(" "):
                try:
                    if bag_pack.loc[val, 'count'] <= 1:
                        if p.match(val):
                            rg = re.sub(r'[0-9]+', '[0-9]+', val)
                            if bag_pack.filter(regex=rg, axis=0).count()['attribute'] > 1 :
                                # add attribute to the list
                                df = pd.DataFrame([(child.tag, attr, rg, 0)], columns=['tag', 'attribute', 'value', 'parent'])
                                dom_df = dom_df.append(df, ignore_index=True)
                            else:
                                print("L'attribut "+attr+"("+val+")"+" est inutile. Discard.")
                        else:
                            print("L'attribut "+attr+"("+val+")"+" est inutile. Discard.")
                    else:
                        df = pd.DataFrame([(child.tag, attr, val, 0)], columns=['tag', 'attribute', 'value', 'parent'])
                        dom_df = dom_df.append(df, ignore_index=True) 
                except:
                    df = pd.DataFrame([(child.tag, attr, val, 0)], columns=['tag', 'attribute', 'value', 'parent'])
                    dom_df = dom_df.append(df, ignore_index=True)
                
        liste_dom.append((dom, dom_df))

    return liste_dom