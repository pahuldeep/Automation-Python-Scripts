import argparse
import logging
from google_play_scraper import app, reviews, Sort
from tqdm import tqdm
import pandas as pd

def fetch_app_info(app_packages, lang, country):
    app_infos = []
    for ap in tqdm(app_packages, desc="Fetching app information"):
        try:
            info = app(ap, lang=lang, country=country)
            del info['comments']
            app_infos.append(info)
            logging.info(f"Fetched info for {ap}")
        except Exception as e:
            logging.error(f"Error fetching info for {ap}: {e}")
    return app_infos

def fetch_app_reviews(app_packages, lang, country):
    app_reviews = []
    for ap in tqdm(app_packages, desc="Fetching app reviews"):
        try:
            for score in range(1, 6):
                for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
                    try:
                        count = 50 
                        rvs, _ = reviews(
                            ap,
                            lang=lang,
                            country=country,
                            sort=sort_order,
                            count=count,
                            filter_score_with=score
                        )
                        
                        if rvs:
                            for r in rvs:
                                r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
                                r['appId'] = ap
                            app_reviews.extend(rvs)
                            logging.info(f"Fetched {len(rvs)} reviews for {ap}, score {score}, sort order {sort_order}, count {count}")
                        else:
                            logging.info(f"No reviews found for {ap}, score {score}, sort order {sort_order}, count {count}")

                    except Exception as e:
                        logging.error(f"Error fetching reviews for {ap}, score {score}, sort order {sort_order}, count {count}: {e}")
        except Exception as e:
            logging.error(f"Error in review fetching loop for {ap}: {e}")
    return app_reviews

def main():
    parser = argparse.ArgumentParser(description='Fetch app info and reviews from Google Play Store.')
    parser.add_argument('app_ids', nargs='+', help='App package IDs to fetch information and reviews for.')
    parser.add_argument('--lang', default='en', help='Language to fetch the data in (default: en).')
    parser.add_argument('--country', default='in', help='Country to fetch the data from (default: in).')
    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(level=logging.INFO)

    app_packages = args.app_ids
    lang = args.lang
    country = args.country

    app_infos = fetch_app_info(app_packages, lang, country)
    app_reviews = fetch_app_reviews(app_packages, lang, country)

    app_infos_df = pd.DataFrame(app_infos).T
    app_infos_df.to_excel('app_details.xlsx')


    app_reviews_df = pd.DataFrame(app_reviews)
    app_reviews_df.to_excel('app_reviews.xlsx')

    # Save or process fetched data as needed
    logging.info(f"Total apps info fetched: {len(app_infos)}")
    logging.info(f"Total reviews fetched: {len(app_reviews)}")

if __name__ == "__main__":
    main()
