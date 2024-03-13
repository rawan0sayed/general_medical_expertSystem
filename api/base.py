class KnowledgeBase:
    def __init__(self):
        self.diseases = [
            {
                'name': 'Common Cold',
                'symptoms': ['fever', 'cough', 'runny_nose', 'sore_throat', 'fatigue'],
                'description': 'The common cold is a viral infection of the upper respiratory tract. It is characterized by symptoms such as sneezing, nasal congestion, sore throat, and mild fever.',
                'treatment': 'Get plenty of rest, stay hydrated, and take over-the-counter cold medication such as decongestants, antihistamines, and pain relievers. Gargling with warm salt water may also help relieve a sore throat.'},
            {
                'name': 'Flu',
                'symptoms': ['fever', 'cough', 'fatigue', 'body_aches'],
                'description': 'Influenza, commonly known as the flu, is a highly contagious viral infection that affects the respiratory system. Symptoms often include high fever, muscle aches, headache, fatigue, and cough.',
                'treatment': 'Rest, drink plenty of fluids, and take antiviral medication if prescribed by a doctor. Over-the-counter medications such as pain relievers, decongestants, and cough suppressants can help alleviate symptoms. In severe cases, hospitalization may be necessary.'},
            {
                'name': 'Chickenpox',
                'symptoms': ['fever', 'rash', 'itchiness', 'fatigue'],
                'description': 'Chickenpox is a highly contagious viral infection characterized by an itchy rash, fever, and fatigue. It is caused by the varicella-zoster virus.',
                'treatment': 'Apply calamine lotion to relieve itching, take oatmeal baths to soothe the skin, and avoid scratching the rash to prevent scarring. Over-the-counter pain relievers such as acetaminophen or ibuprofen can help reduce fever and discomfort.'},
            {
                'name': 'Strep Throat',
                'symptoms': ['sore_throat', 'fever', 'swollen_glands'],
                'description': 'Strep throat is a bacterial infection that causes inflammation and soreness of the throat, often accompanied by fever and swollen lymph nodes in the neck.',
                'treatment': 'Take antibiotics as prescribed by a doctor to treat the bacterial infection. Rest, drink plenty of fluids, and use over-the-counter pain relievers such as acetaminophen or ibuprofen to alleviate symptoms.'},
            {
                'name': 'Gastroenteritis',
                'symptoms': ['vomiting', 'diarrhea', 'abdominal_pain'],
                'description': 'Gastroenteritis, commonly known as stomach flu, is an inflammation of the stomach and intestines caused by viral or bacterial infection. Symptoms include diarrhea, vomiting, stomach cramps, and fever.',
                'treatment': 'Stay hydrated with electrolyte solutions, eat bland foods like rice and toast, and rest. Seek medical attention if symptoms worsen or persist. In severe cases, hospitalization may be necessary.'},
            {
                'name': 'Asthma',
                'symptoms': ['cough', 'wheezing', 'difficulty_breathing'],
                'description': 'Asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways, leading to wheezing, shortness of breath, chest tightness, and coughing.',
                'treatment': 'Use inhalers as prescribed to control symptoms and prevent asthma attacks. Avoid triggers such as allergens and irritants, and seek medical help if symptoms worsen despite treatment.'},
            {
                'name': 'Ear Infection',
                'symptoms': ['ear pain', 'fever', 'difficulty_sleeping'],
                'description': 'An ear infection, or otitis media, is an inflammation of the middle ear often caused by bacterial or viral infection. Symptoms include ear pain, fever, and sometimes hearing loss.',
                'treatment': 'Take antibiotics as prescribed by a doctor to treat the bacterial infection. Apply warm compresses to the ear to relieve pain, and use over-the-counter pain relievers such as acetaminophen or ibuprofen.'},
            {
                'name': 'Allergies',
                'symptoms': ['runny nose', 'sneezing', 'itchy_eyes', 'itchiness'],
                'description': 'Allergies occur when the immune system reacts abnormally to substances that are usually harmless, such as pollen, dust mites, pet dander, or certain foods. Symptoms vary depending on the allergen but commonly include sneezing, runny nose, itchy eyes, and rash.',
                'treatment': 'Avoid allergens whenever possible. Take antihistamines to relieve symptoms, and use nasal sprays as prescribed. In severe cases, allergy shots (immunotherapy) may be recommended.'},
            {
                'name': 'Measles',
                'symptoms': ['fever', 'cough', 'rash', 'sore_throat'],
                'description': 'Measles is a highly contagious viral infection characterized by high fever, cough, runny nose, rash, and red, watery eyes. Complications can include pneumonia, encephalitis, and death.',
                'treatment': 'Rest, stay hydrated, and take fever-reducing medication. Seek medical attention if complications such as pneumonia or encephalitis arise. Vaccination with the measles, mumps, and rubella (MMR) vaccine can prevent measles.'},
            {
                'name': 'Hand, Foot, and Mouth Disease',
                'symptoms': ['fever', 'sore_throat', 'rash', 'blisters'],
                'description': 'Hand, foot, and mouth disease is a viral infection common in children under 5 years old. It is characterized by fever, sore throat, rash, and blisters on the hands, feet, and mouth.',
                'treatment': 'Rest, stay hydrated, and use over-the-counter pain relievers to reduce fever and discomfort. Avoid close contact with others to prevent spread. Symptoms usually resolve on their own within a week.'},
            {
                'name': 'Diabetes',
                'symptoms': ['excessive_thirst', 'frequent_urination', 'fatigue', 'unexplained_weight_loss'],
                'description': 'Diabetes is a chronic condition characterized by high blood sugar levels due to insufficient production of insulin (Type 1 diabetes) or the body\'s inability to use insulin effectively (Type 2 diabetes). Symptoms of high blood sugar include frequent urination, increased thirst, and unexplained weight loss.',
                'treatment': 'Monitor blood sugar levels regularly, adhere to a balanced diet, take insulin or oral medications as prescribed, exercise regularly, and maintain a healthy lifestyle. Regular medical check-ups are essential for proper management of diabetes.'},
            {
                'name': 'Paranasal Sinusitis',
                'symptoms': ['facial_pain', 'headache', 'nasal_congestion', 'cough'],
                'description': 'Paranasal sinusitis, or sinus infection, is an inflammation of the paranasal sinuses caused by viral, bacterial, or fungal infection. Symptoms include facial pain, nasal congestion, headache, and postnasal drip.',
                'treatment': 'Use saline nasal sprays to help clear nasal passages, apply warm compresses to relieve facial pain, take over-the-counter pain relievers such as acetaminophen or ibuprofen, and stay hydrated. In some cases, antibiotics may be prescribed for bacterial sinusitis.'},
            {
                'name': 'Diarrheal Diseases',
                'symptoms': ['abdominal_pain', 'diarrhea', 'vomiting', 'dehydration'],
                'description': 'Diarrheal diseases are gastrointestinal infections that cause frequent loose stools, abdominal cramps, and sometimes vomiting and fever. They can be caused by viruses, bacteria, or parasites.',
                'treatment': 'Stay hydrated with clear fluids such as water, broth, or oral rehydration solutions to replace lost fluids and electrolytes. Eat bland foods like bananas, rice, and toast, and avoid dairy and fatty foods. Seek medical attention if symptoms persist or worsen.'
            },
        ]