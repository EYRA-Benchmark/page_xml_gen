pip install generateDS
wget http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19/pagecontent.xsd
generateDS -f -o page_api.py -s page_sub.py pagecontent.xsd


