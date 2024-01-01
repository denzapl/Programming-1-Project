# List of questions and answers
questions = [" What are the major risk factors that increase the severity of COVID-19 symptoms?",
    "How effective are booster doses in enhancing immunity against COVID-19?",
    "What is the role of ventilation in reducing the spread of COVID-19 indoors?",
    "Are there any specific dietary recommendations to boost immunity against COVID-19?",
    "How do monoclonal antibodies work in treating COVID-19?",
    "What are the potential long-term effects of COVID-19 vaccination?",
    "How do public health measures differ in managing COVID-19 in various countries?",
    "What strategies can help mitigate 'pandemic fatigue' or burnout?",
    "Can pets or animals transmit COVID-19 to humans?",
    "How does COVID-19 affect individuals with pre-existing health conditions?",
    "What are the possible reasons behind vaccine hesitancy or resistance in some populations?",
    "What measures can schools take to minimize COVID-19 transmission among students and staff?",
    "How effective are natural remedies or alternative therapies in treating COVID-19 symptoms?",
    "What are the challenges faced in distributing vaccines globally?",
    "How can businesses implement safety protocols to protect employees from COVID-19 in the workplace?",
    "What are the ethical considerations surrounding vaccine prioritization and distribution?",
    "How does COVID-19 impact lung health in the long term?",
    "Are there any specific guidelines for safely attending gatherings or events during the pandemic?",
    "What research is being conducted on new treatments or medications for COVID-19?",
    "How does COVID-19 vaccination affect the transmission rate of the virus within communities?"]

answers = ["Major risk factors for severe COVID-19 symptoms include age, underlying health conditions (such as diabetes or heart disease), weakened immune systems, and certain occupations or living conditions that increase exposure.",
    "Booster doses significantly enhance immunity against COVID-19, especially against variants, by increasing antibody levels and providing stronger protection against severe illness.",
    "Proper ventilation reduces the concentration of airborne virus particles indoors, lowering the risk of transmission among individuals.",
    "While a balanced diet rich in fruits, vegetables, whole grains, and adequate protein supports the immune system, there's no specific diet proven to prevent COVID-19.",
    "Monoclonal antibodies neutralize the virus, reduce viral load, and help the immune system fight COVID-19, often used for high-risk individuals or those with mild to moderate symptoms.",
    "Long-term effects of vaccination focus on immune response, with severe adverse effects being rare.",
    "Public health measures vary based on country policies, including vaccination strategies, mask mandates, lockdowns, testing, and contact tracing.",
    "Strategies to mitigate pandemic fatigue include promoting self-care, encouraging breaks, maintaining routines, fostering social connections, and seeking professional support.",
    "While pets can contract the virus, transmission to humans is rare and mostly occurs from human to pet rather than the other way around.",
    "Individuals with pre-existing health conditions are at higher risk for severe illness or complications if they contract COVID-19.",
    "Reasons for vaccine hesitancy vary from safety concerns, misinformation, lack of trust in authorities, historical issues, religious or cultural beliefs, to political influences.",
    "School measures to minimize COVID-19 transmission include implementing mask mandates, promoting vaccinations for eligible students and staff, maintaining physical distancing, improving ventilation, and regular testing.",
    "While some natural remedies might help alleviate symptoms, there's limited evidence supporting their effectiveness in treating COVID-19.",
    "Challenges in vaccine distribution include supply chain issues, equitable access, storage requirements, and vaccine hesitancy.",
    "Business safety protocols include implementing mask mandates, encouraging vaccinations, maintaining physical distancing, improving ventilation, and offering remote work options where feasible.",
    "Ethical considerations in vaccine prioritization and distribution involve prioritizing vulnerable populations, ensuring equitable distribution globally, and balancing individual rights with public health.",
    "Some individuals may experience long-term lung damage, including reduced lung function and fibrosis, after severe COVID-19 infection.",
    "Guidelines for safely attending gatherings or events during the pandemic often include vaccination, mask-wearing, maintaining distance, and ensuring proper ventilation.",
    "Research on new treatments or medications for COVID-19 focuses on antiviral medications, monoclonal antibodies, and repurposed drugs to reduce severity and improve recovery.",
    "COVID-19 vaccination reduces transmission by lowering the likelihood of infection and severe disease, thus decreasing the spread within communities."]


# Dictionary to store user data
user_data = {}

# Function to validate email
def validate_email(email):
    valid_mail = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
    for domain in valid_mail:
        if domain in email:
            return True
    return False

# Display chatbot menu and handle user choices
def display_menu():
    while True:
        choices = int(input("Choose the category: \n"
                            "1. COVID-19 Health related questions\n"
                            "2. COVID-19 Symptoms\n"
                            "3. COVID-19 Prevention\n"
                            "4. COVID-19 Information\n"
                            "0. Exit Chatbot\n"))
        if choices == 0:
            print("Exiting the chatbot. Goodbye and take care")
            break

        if choices == 1:
            while True:
                for idx, q in enumerate(questions, start=1):
                    print(f"{idx}. {q}")
                question_choice = int(input("Choose a question number for more details: "))
                if 1 <= question_choice <= len(questions):
                    chosen_question = questions[question_choice - 1]
                    answer_index = question_choice - 1
                    print(f"Question: {chosen_question}")
                    print(f"Answer: {answers[answer_index]}")

                    moreq = str(input("Do you have any more questions: (Yes/No) "))
                    if moreq == "No":
                        print(
                            "Thank you for using the COVID-19 chatbot. If you have any more questions you can choose from the following categories: ")
                        break

        elif choices == 2:
            symptoms = str(input("""Within the last 10 days, have you experienced any of the following symptoms: (Yes/No)
                                   1.Fever or chills\n
                                   2.Cough\n
                                   3.Shortness of breath or difficulty breathing\n
                                   4.New loss of taste or smell\n
                                   5.Fatigue\n
                                   6.Muscle or body aches\n
                                   7.Headache\n
                                   8.Sore throat\n
                                   9.Congestion or runny nose\n
                                   10.Nausea or vomiting\n
                                   11.Diarrhea\n"""))

            if symptoms == "Yes":
                print(
                    "Consider undergoing a COVID-19 viral test. If symptoms have appeared earlier, get tested promptly. Meanwhile, follow the quarantine guidelines, considering your vaccination status, as you await your test results. Seek personalized medical advice from a healthcare professional for further guidance.")
            else:
                print("It seems like you haven't experienced any COVID-19 symptoms.")


        elif choices == 3:
            print("""
                            Additional COVID-19 Prevention Measures:
                            1. Avoid Crowded Places: Minimize time spent in crowded areas or gatherings.
                            2. Remote Work: If feasible, work from home to reduce exposure in workplaces.
                            3. Limit Close Contact: Avoid close contact with individuals outside your household.
                            4. Follow Quarantine Guidelines: Adhere to quarantine guidelines if exposed or infected.
                            5. Support Contact Tracing: Cooperate with contact tracing efforts by health authorities.
                            6. Disinfect Frequently: Clean and disinfect high-touch surfaces regularly.
                            7. Outdoor Activities: Opt for outdoor activities, where possible, over indoor gatherings.
                            8. Consider Ventilation: Open windows or use air purifiers for better indoor air circulation.
                            9. Immunocompromised Individuals: Take extra precautions to protect vulnerable individuals.
                            10. Mental Health Support: Seek mental health support to cope with stress or anxiety.

                            These measures, along with the standard preventive actions, help in reducing the spread of COVID-19.
                            """)


        elif choices == 4:
            print("""
                    1. Transmission: COVID-19 primarily spreads through respiratory droplets when an infected person coughs, sneezes, talks, or breathes. It can also spread by touching surfaces contaminated with the virus and then touching the face.
                    2. Symptoms: Common symptoms include fever, cough, shortness of breath, fatigue, muscle or body aches, headache, sore throat, loss of taste or smell, congestion, runny nose, nausea, or diarrhea.
                    3. Vaccines: Several vaccines have been developed and authorized for emergency use to prevent COVID-19. Vaccination helps reduce the severity of the illness and prevents hospitalization and death.
                    4. Variants: Multiple variants of the virus have emerged worldwide, some of which have shown increased transmissibility or the potential to evade immunity generated by previous infections or vaccination.
                    5. Preventive Measures: Effective preventive measures include wearing masks, practicing good hand hygiene, maintaining physical distance, getting vaccinated, and following public health guidelines.
                    6. Delta Variant: The Delta variant, identified as more transmissible, led to a surge in cases in various parts of the world due to its increased infectivity.
                    7. Long COVID: Some individuals experience lingering symptoms after recovering from acute COVID-19, known as long COVID. These symptoms can persist for weeks or months and may include fatigue, shortness of breath, brain fog, and others.
                    8. Pandemic Impact: COVID-19 significantly impacted global economies, healthcare systems, education, and mental health due to lockdowns, travel restrictions, and social distancing measures.
                    9. Treatments: Various treatments, such as antiviral medications and monoclonal antibodies, have been developed to help reduce the severity of COVID-19 in infected individuals.
                    10. Breakthrough Infections: Vaccinated individuals can still get infected with COVID-19, but vaccination significantly reduces the risk of severe illness, hospitalization, and death.
                    11. Booster Shots: Booster doses have been recommended for certain populations to enhance and prolong protection against COVID-19, especially amid concerns about waning immunity over time.
                    12. Global Response: Countries worldwide have implemented vaccination drives, travel restrictions, and other measures to curb the spread of the virus and protect their populations.
                    13. Misinformation: The pandemic has seen the spread of misinformation and conspiracy theories about the virus, vaccines, and public health measures, posing challenges to efforts in controlling the spread of COVID-19.
                    14. Vaccination Equity: Ensuring equitable access to vaccines has been a challenge globally, with disparities in vaccine distribution and access among different countries and populations.
                    15. Omicron Variant: In late 2021, a new variant called Omicron was identified, prompting concerns due to its high number of mutations. Efforts are ongoing to understand its transmissibility, severity, and its potential impact on vaccine effectiveness.""")

        elif choices == 0:
            print("Exiting the chatbot. Goodbye and take care")
            return

#Function to handle user login
def login_user():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    if email in user_data and user_data[email] == password:
        print("Login successful.")
        print("Welcome to the COVID-19 chatbot.")
        print("Hello, my name is covid.io, and I am here to answer all questions COVID-19 related.")
        return True
    else:
        print("Invalid email or password. Would you like to register?")
        return False

# User registration
def register_user():
    while True:
        email = input("Enter your email address: ")
        password = input("Set your password: ")
        if validate_email(email):
            if email not in user_data:
                user_data[email] = password
                print("Registration successful.")
                return True
            else:
                print("Email already exists. Registration failed.")
                return False
        else:
            print("Invalid email. Registration failed.")
            continue
register_user()

def userregistration():
    while True:
        login_option = input("Are you a registered user? (Yes/No): ").lower()
        if login_option == "yes":
            if login_user():
                display_menu()
            break
        elif login_option == "no":
            if register_user():
                display_menu()
            break
        else:
            print("Please enter a valid option (Yes/No)")



def startingchatbot():
    userregistration()

startingchatbot()






