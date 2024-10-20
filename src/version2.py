import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Function to calculate review dates
def calculate_review_dates(start_date):
    intervals = [1, 3, 7, 14, 30, 60, 90, 180, 365, 730]
    return [(start_date + timedelta(days=interval)).strftime('%Y-%m-%d') for interval in intervals]

# Updated function to add a new study entry
def add_study_entry(topic, study_date, csv_file='study_schedule.csv'):
    if os.path.exists(csv_file):
        data = pd.read_csv(csv_file)
        if 'Completed Reviews' not in data.columns:
            data['Completed Reviews'] = 0
            data.to_csv(csv_file, index=False)
    else:
        data = pd.DataFrame(columns=['Study Date', 'Topic'] + [f'Review {i+1}' for i in range(10)] + ['Completed Reviews'])
    
    review_dates = calculate_review_dates(study_date)
    new_entry = pd.DataFrame([[study_date.strftime('%Y-%m-%d'), topic] + review_dates + [0]],
                             columns=['Study Date', 'Topic'] + [f'Review {i+1}' for i in range(10)] + ['Completed Reviews'])
    data = pd.concat([data, new_entry], ignore_index=True)
    data.to_csv(csv_file, index=False)

# Function to get today's reviews
def get_todays_reviews(csv_file='study_schedule.csv'):
    if not os.path.exists(csv_file):
        return pd.DataFrame()
    
    today = datetime.now().date()
    data = pd.read_csv(csv_file)
    reviews = []
    
    for index, row in data.iterrows():
        for i in range(2, 12):  # Check Review 1 to Review 10
            if today.strftime('%Y-%m-%d') == row[f'Review {i-1}']:
                reviews.append({'Topic': row['Topic'], 'Index': index})
    
    return pd.DataFrame(reviews)

# Function to update completed reviews
def update_completed_reviews(index, csv_file='study_schedule.csv'):
    data = pd.read_csv(csv_file)
    if 'Completed Reviews' not in data.columns:
        data['Completed Reviews'] = 0
    data.loc[index, 'Completed Reviews'] += 1
    data.to_csv(csv_file, index=False)

# Updated function to generate insights
def generate_insights(csv_file='study_schedule.csv'):
    if not os.path.exists(csv_file):
        return None, None
    
    data = pd.read_csv(csv_file)
    
    # Ensure 'Completed Reviews' column exists
    if 'Completed Reviews' not in data.columns:
        data['Completed Reviews'] = 0
        data.to_csv(csv_file, index=False)
    
    # Topic distribution
    topic_counts = data['Topic'].value_counts()
    topic_chart = px.pie(values=topic_counts.values, names=topic_counts.index, title='Distribution of Study Topics')
    
    # Review completion rate
    total_reviews = len(data) * 10  # Assuming 10 reviews per entry
    completed_reviews = data['Completed Reviews'].sum()
    completion_rate = (completed_reviews / total_reviews) * 100 if total_reviews > 0 else 0
    
    completion_chart = px.bar(x=['Completion Rate'], y=[completion_rate], title='Review Completion Rate')
    completion_chart.update_yaxes(range=[0, 100])
    
    return topic_chart, completion_chart

# New function to calculate streaks and daily stats
def calculate_streaks_and_stats(csv_file='study_schedule.csv'):
    if not os.path.exists(csv_file):
        return 0, 0, [], []

    data = pd.read_csv(csv_file)
    data['Study Date'] = pd.to_datetime(data['Study Date'])
    data = data.sort_values('Study Date')

    # Calculate study streak
    data['Consecutive'] = (data['Study Date'].diff() != timedelta(days=1)).cumsum()
    current_study_streak = data.groupby('Consecutive').size().max()

    # Calculate revision streak
    if 'Completed Reviews' not in data.columns:
        data['Completed Reviews'] = 0
    data['Revision Date'] = data['Study Date'].dt.date
    revision_data = data.groupby('Revision Date')['Completed Reviews'].sum().reset_index()
    revision_data['Consecutive'] = (revision_data['Revision Date'].diff() != timedelta(days=1)).cumsum()
    current_revision_streak = revision_data[revision_data['Completed Reviews'] > 0].groupby('Consecutive').size().max()

    # Daily task completion
    daily_tasks = data.groupby('Study Date').size().reset_index(name='Tasks')
    daily_tasks['Date'] = daily_tasks['Study Date'].dt.strftime('%Y-%m-%d')

    # Daily revision completion
    daily_revisions = revision_data
    daily_revisions['Date'] = daily_revisions['Revision Date'].astype(str)

    return current_study_streak, current_revision_streak, daily_tasks, daily_revisions

# Updated generate_insights function
def generate_insights(csv_file='study_schedule.csv'):
    if not os.path.exists(csv_file):
        return None, None, None, None

    data = pd.read_csv(csv_file)

    # Ensure 'Completed Reviews' column exists
    if 'Completed Reviews' not in data.columns:
        data['Completed Reviews'] = 0
        data.to_csv(csv_file, index=False)

    # Topic distribution
    topic_counts = data['Topic'].value_counts()
    topic_chart = px.pie(values=topic_counts.values, names=topic_counts.index, title='Distribution of Study Topics')

    # Review completion rate
    total_reviews = len(data) * 10  # Assuming 10 reviews per entry
    completed_reviews = data['Completed Reviews'].sum()
    completion_rate = (completed_reviews / total_reviews) * 100 if total_reviews > 0 else 0

    completion_chart = px.bar(x=['Completion Rate'], y=[completion_rate], title='Review Completion Rate')
    completion_chart.update_yaxes(range=[0, 100])

    # Calculate streaks and daily stats
    study_streak, revision_streak, daily_tasks, daily_revisions = calculate_streaks_and_stats(csv_file)

    # Daily activity chart
    daily_activity = go.Figure()
    daily_activity.add_trace(go.Scatter(x=daily_tasks['Date'], y=daily_tasks['Tasks'], mode='lines+markers', name='Study Tasks'))
    daily_activity.add_trace(go.Scatter(x=daily_revisions['Date'], y=daily_revisions['Completed Reviews'], mode='lines+markers', name='Completed Revisions'))
    daily_activity.update_layout(title='Daily Study Activity', xaxis_title='Date', yaxis_title='Count')

    return topic_chart, completion_chart, daily_activity, study_streak, revision_streak

# Updated Streamlit UI
def main():
    st.title('Enhanced Spaced Repetition Study Scheduler')

    # Input for new study topic
    with st.form(key='study_form'):
        topic = st.text_input('Enter what you studied today:')
        submit_button = st.form_submit_button(label='Save Study Session')

    if submit_button and topic:
        add_study_entry(topic, datetime.now())
        st.success('Study session saved!')

    # Today's review schedule
    st.header("Today's Review Schedule:")
    reviews = get_todays_reviews()

    if not reviews.empty:
        for _, review in reviews.iterrows():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"- {review['Topic']}")
            with col2:
                if st.checkbox('Completed', key=f"checkbox_{review['Index']}"):
                    update_completed_reviews(review['Index'])
                    st.success('Review marked as completed!')
    else:
        st.write("Nothing to review today!")

    # Insights
    st.header("Study Insights")
    topic_chart, completion_chart, daily_activity, study_streak, revision_streak = generate_insights()

    if topic_chart and completion_chart and daily_activity is not None:
        # Display streaks
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Study Streak", f"{study_streak} days")
        with col2:
            st.metric("Current Revision Streak", f"{revision_streak} days")

        # Display charts
        st.plotly_chart(topic_chart, use_container_width=True)
        st.plotly_chart(completion_chart, use_container_width=True)
        st.plotly_chart(daily_activity, use_container_width=True)
    else:
        st.write("Not enough data to generate insights yet. Keep studying!")

if __name__ == "__main__":
    main()