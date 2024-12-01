from googleapiclient.discovery import build
import pandas as pd
import json

def get_keywords_from_search_console():
    with open('../config/config.json') as f:
        config = json.load(f)

    service = build('searchconsole', 'v1')
    request = {
        "startDate": config['google_search_console']['start_date'],
        "endDate": config['google_search_console']['end_date'],
        "dimensions": ["query"],
        "rowLimit": 1000
    }
    response = service.searchanalytics().query(
        siteUrl=config['google_search_console']['site_url'], body=request
    ).execute()

    keywords = [
        {
            "keyword": row['keys'][0],
            "clicks": row['clicks'],
            "impressions": row['impressions'],
            "ctr": row['ctr'],
            "position": row['position']
        }
        for row in response.get("rows", [])
    ]

    df = pd.DataFrame(keywords)
    df.to_csv('../data/keywords_report.csv', index=False)
    print("Keywords report saved as 'keywords_report.csv'.")
