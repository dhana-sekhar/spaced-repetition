import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# Function to calculate review dates
def calculate_review_dates(start_date):
    intervals = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378]
    return [(start_date + timedelta(days=interval)).strftime('%Y-%m-%d') for interval in intervals]

# Function to add a new study entry
def add_study_entry(topic, study_date, csv_file='study_schedule.csv'):
    if not os.path.exists(csv_file):
        pd.DataFrame(columns=['Study Date', 'Topic'] + [f'Review {i+1}' for i in range(27)]).to_csv(csv_file, index=False)
    
    review_dates = calculate_review_dates(study_date)
    new_entry = pd.DataFrame([[study_date.strftime('%Y-%m-%d'), topic] + review_dates], 
                             columns=['Study Date', 'Topic'] + [f'Review {i+1}' for i in range(len(review_dates))])
    new_entry.to_csv(csv_file, mode='a', header=False, index=False)

# Function to get today's reviews
def get_todays_reviews(csv_file='study_schedule.csv'):
    if not os.path.exists(csv_file):
        return []

    today = datetime.now().date()
    reviews = []
    data = pd.read_csv(csv_file)
    for index, row in data.iterrows():
        if today.strftime('%Y-%m-%d') in row[2:].values:
            reviews.append(row['Topic'])
    return reviews

# Streamlit UI
def main():
    st.title('Spaced Repetition Study Scheduler')

    with st.form(key='study_form'):
        topic = st.text_input('Enter what you studied today:')
        submit_button = st.form_submit_button(label='Save Study Session')

    if submit_button and topic:
        add_study_entry(topic, datetime.now())
        st.success('Study session saved!')

    st.header('Today’s Review Schedule:')
    reviews = get_todays_reviews()
    if reviews:
        for review in reviews:
            st.markdown(f"- {review}")
    else:
        st.write("Nothing to review today!")

if __name__ == "__main__":
    main()
