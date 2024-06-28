import data_collection
import data_analysis

def main():
    url = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S11.htm"
    
    # Collect data
    df = data_collection.fetch_election_data(url)
    data_collection.save_data_to_csv(df)

    # Analyze data
    df = data_analysis.load_data()
    insights = data_analysis.generate_insights(df)
    for i, insight in enumerate(insights, 1):
        print(f"Insight {i}: {insight}")
    data_analysis.plot_top_10_parties(df)

if __name__ == "__main__":
    main()
