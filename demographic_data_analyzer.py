import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / df.shape[0] * 100, 1
    )

    # 4. Advanced education filter
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]

    # 5. Rich percentages
    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1
    )

    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1
    )

    # 6. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. Rich percentage among people who work min hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1
    )

    # 8. Country with highest percentage of rich people
    total_per_country = df['native-country'].value_counts()
    rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_percentage_per_country = (rich_per_country / total_per_country) * 100
    highest_earning_country = rich_percentage_per_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_per_country.max(), 1)

    # 9. Most popular occupation for rich people in India
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_indians['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
