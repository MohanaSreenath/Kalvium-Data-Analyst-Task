import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename='party_wise_results.csv'):
    return pd.read_csv(filename)

def generate_insights(df):
    insights = []

    total_parties = df['Party'].nunique()
    insights.append(f"Total number of parties: {total_parties}")

    top_party = df.loc[df['Total'].idxmax()]
    insights.append(f"Top party by total seats: {top_party['Party']} with {top_party['Total']} seats")

    top_5_parties = df.nlargest(5, 'Total')
    insights.append("Top 5 parties by total seats:\n" + top_5_parties[['Party', 'Total']].to_string(index=False))

    zero_seat_parties = df[df['Total'] == 0]
    insights.append(f"Number of parties with zero seats won: {zero_seat_parties.shape[0]}")

    average_seats_won = df['Won'].mean()
    insights.append(f"Average number of seats won per party: {average_seats_won:.2f}")

    median_seats_won = df['Won'].median()
    insights.append(f"Median number of seats won per party: {median_seats_won}")

    std_seats_won = df['Won'].std()
    insights.append(f"Standard deviation of seats won: {std_seats_won:.2f}")

    total_seats_won = df['Won'].sum()
    insights.append(f"Total seats won by all parties: {total_seats_won}")

    top_party_proportion = (top_party['Won'] / total_seats_won) * 100
    insights.append(f"Proportion of seats won by the top party: {top_party_proportion:.2f}%")

    more_won_than_leading = df[df['Won'] > df['Leading']]
    insights.append(f"Number of parties with more seats won than leading: {more_won_than_leading.shape[0]}")

    return insights

def plot_top_10_parties(df, filename='top_10_parties.png'):
    top_10_parties = df.nlargest(10, 'Total')
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Total', y='Party', data=top_10_parties, palette='viridis')
    plt.xlabel('Total Seats')
    plt.ylabel('Party')
    plt.title('Top 10 Parties by Total Seats')
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    df = load_data()
    insights = generate_insights(df)
    for i, insight in enumerate(insights, 1):
        print(f"Insight {i}: {insight}")
    plot_top_10_parties(df)
