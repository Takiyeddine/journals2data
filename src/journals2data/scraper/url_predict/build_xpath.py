import pandas as pd
import re

def to_xpath(nb_cluster, b_w, list_simplified):
    xpath_list = []
        
    for i in range(0, nb_cluster):
        dom_df = pd.DataFrame(columns=['tag', 'parent', 'attribute', 'value'])
        elements = b_w[list_simplified[i]]
        
        if len(elements) == 0:
            continue
        
        xpath = "//"
        for e in elements:
            _e = e.split('.')
            df = pd.DataFrame([(_e[0], _e[1], _e[2].split('=')[0], _e[2].split('=')[1])], columns=['tag', 'parent', 'attribute', 'value'])
            dom_df = dom_df.append(df, ignore_index=True)

        parent_df = dom_df.loc[dom_df['parent']=='1']
        if not parent_df.empty:
            xpath += parent_df['tag'].iloc[0]
            xpath += "["
            
            count = 0
            
            # check if two elements have the same attribute
            for _, p in parent_df.iterrows():
                if "[0-9]+" in p['value']:
                    xpath += "re:match(@"+p['attribute']+", '^"+p['value'].replace('[0-9]+', r'\d+') +"$')"
                else:
                    xpath += "contains(@"+p['attribute']+", '"+p['value']+"')"
                
                count += 1
                
                if count < parent_df.count()[0]:
                    xpath += " and "
            
            xpath += "]/"
        
        child_df = dom_df.loc[dom_df['parent']=='0']
        
        if not child_df.empty:
            xpath += child_df['tag'].iloc[0]
            xpath += "["
            
            count = 0
            
            # check if two elements have the same attribute
            for _, p in child_df.iterrows():
                if "[0-9]+" in p['value']:
                    xpath += "re:match(@"+p['attribute']+", '^"+p['value'].replace('[0-9]+', r'\d+') +"$')"
                else:
                    xpath += "contains(@"+p['attribute']+", '"+p['value']+"')"
                
                count += 1
                
                if count < child_df.count()[0]:
                    xpath += " and "
            
            xpath += "]"
        else:
            xpath += "a"

        xpath_list.append(xpath)

    return xpath_list
