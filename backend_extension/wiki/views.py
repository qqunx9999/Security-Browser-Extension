from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####
import joblib
import wikipedia
from original import Bmain

k = joblib.load("model_nn2.pkl")

def index(request):
    return HttpResponse("Hello, world. You're at the wiki index.")


# https://pypi.org/project/wikipedia/#description



def get_wiki_summary(request):
    gow = ["th","pantip","gmail","google","stackoverflow","instagram",'facebook','youtube','pornhub','medium',"w3schools","ugetfix","wikipedia","websiteplanet","microsoft","kaggle","webex","zoom","cyfence","linkedin","data.mendeley","alibaba","shopee","lazada","ku"]

    '''url = request.GET.get('url', None)
    op = (Bmain.extract_features(url, "unnown"))
    line = "url,length_url,length_hostname,ip,nb_dots,nb_hyphens,nb_at,nb_qm,nb_and,nb_or,nb_eq,nb_underscore,nb_tilde,nb_percent,nb_slash,nb_star,nb_colon,nb_comma,nb_semicolumn,nb_dollar,nb_space,nb_www,nb_com,nb_dslash,http_in_path,https_token,ratio_digits_url,ratio_digits_host,punycode,port,tld_in_path,tld_in_subdomain,abnormal_subdomain,nb_subdomains,prefix_suffix,shortening_service,path_extension,nb_redirection,nb_external_redirection,length_words_raw,char_repeat,shortest_words_raw,shortest_word_host,shortest_word_path,longest_words_raw,longest_word_host,longest_word_path,avg_words_raw,avg_word_host,avg_word_path,phish_hints,domain_in_brand,brand_in_subdomain,brand_in_path,suspecious_tld,statistical_report,nb_hyperlinks,ratio_intHyperlinks,ratio_extHyperlinks,ratio_nullHyperlinks,nb_extCSS,ratio_intRedirection,ratio_extRedirection,ratio_intErrors,ratio_extErrors,login_form,external_favicon,links_in_tags,submit_email,ratio_intMedia,ratio_extMedia,sfh,iframe,popup_window,safe_anchor,onmouseover,right_clic,empty_title,domain_in_title,domain_with_copyright,whois_registered_domain,domain_registration_length,domain_age,web_traffic,dns_record,google_index,page_rank,answer\n"
    try :
        for x in op :
            if x!=op[-1] : line = line+str(x)+','
            else :
                line = line+str("unknown")+"\n"
                return JsonResponse(line)
    except Exception:
        return JsonResponse(False)'''
    
    topic = request.GET.get('topic', None)

    topic = topic[1:len(topic)-1]
    print(f"The topic is {topic}")
    line = "url,length_url,length_hostname,ip,nb_dots,nb_hyphens,nb_at,nb_qm,nb_and,nb_or,nb_eq,nb_underscore,nb_tilde,nb_percent,nb_slash,nb_star,nb_colon,nb_comma,nb_semicolumn,nb_dollar,nb_space,nb_www,nb_com,nb_dslash,http_in_path,https_token,ratio_digits_url,ratio_digits_host,punycode,port,tld_in_path,tld_in_subdomain,abnormal_subdomain,nb_subdomains,prefix_suffix,shortening_service,path_extension,nb_redirection,nb_external_redirection,length_words_raw,char_repeat,shortest_words_raw,shortest_word_host,shortest_word_path,longest_words_raw,longest_word_host,longest_word_path,avg_words_raw,avg_word_host,avg_word_path,phish_hints,domain_in_brand,brand_in_subdomain,brand_in_path,suspecious_tld,statistical_report,nb_hyperlinks,ratio_intHyperlinks,ratio_extHyperlinks,ratio_nullHyperlinks,nb_extCSS,ratio_intRedirection,ratio_extRedirection,ratio_intErrors,ratio_extErrors,login_form,external_favicon,links_in_tags,submit_email,ratio_intMedia,ratio_extMedia,sfh,iframe,popup_window,safe_anchor,onmouseover,right_clic,empty_title,domain_in_title,domain_with_copyright,whois_registered_domain,domain_registration_length,domain_age,web_traffic,dns_record,google_index,page_rank,answer"
    line = line.split(",")
    try:
        io = (Bmain.extract_features(topic, "unknown"))
    except Exception:
        io="BRUH"
    io = [io]
    daf = pd.DataFrame(io)
    daf.columns = line
    daf = daf.drop(['url','answer'], axis=1)
    cpy = ['length_url',
 'length_hostname',
 'nb_dots',
 'nb_hyphens',
 'nb_and',
 'nb_eq',
 'nb_slash',
 'nb_colon',
 'nb_subdomains',
 'length_words_raw',
 'shortest_words_raw',
 'shortest_word_host',
 'longest_words_raw',
 'longest_word_host',
 'longest_word_path',
 'avg_words_raw',
 'avg_word_host',
 'avg_word_path',
 'ratio_intHyperlinks']
    daf = daf.drop(cpy,axis=1)
    ans = k.predict(daf)
    an = not(ans[0])
    if ans[0]:
        ans = "Danger"
    else:
        ans = "Safe"
    for x in gow:
        if x in topic:
            ans = "Safe"
            break
    if "192.168" in topic or "127.0" in topic:
        ans = "Danger"
    data = {
        'summary': ans,
        'raw': 'Successful',
    }
    return JsonResponse(data)
