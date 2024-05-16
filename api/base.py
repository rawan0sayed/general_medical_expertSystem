class KnowledgeBase:
    def __init__(self):
        self.diseases = [
            {
                'name': 'Common Cold',
                'symptoms': ['fever', 'cough', 'runny_nose', 'sore_throat', 'fatigue'],
                'description': 'The common cold is a viral infection of the upper respiratory tract. It is characterized by symptoms such as sneezing, nasal congestion, sore throat, and mild fever.',
                'treatment': 'Get plenty of rest, stay hydrated, and take over-the-counter cold medication such as decongestants, antihistamines, and pain relievers. Gargling with warm salt water may also help relieve a sore throat.'
            },
            {
                'name': 'Flu',
                'symptoms': ['fever', 'cough', 'fatigue', 'body_aches'],
                'description': 'Influenza, commonly known as the flu, is a highly contagious viral infection that affects the respiratory system. Symptoms often include high fever, muscle aches, headache, fatigue, and cough.',
                'treatment': 'Rest, drink plenty of fluids, and take antiviral medication if prescribed by a doctor. Over-the-counter medications such as pain relievers, decongestants, and cough suppressants can help alleviate symptoms. In severe cases, hospitalization may be necessary.'
            },
            {
                'name': 'Chickenpox',
                'symptoms': ['fever', 'rash', 'itchiness', 'fatigue'],
                'description': 'Chickenpox is a highly contagious viral infection characterized by an itchy rash, fever, and fatigue. It is caused by the varicella-zoster virus.',
                'treatment': 'Apply calamine lotion to relieve itching, take oatmeal baths to soothe the skin, and avoid scratching the rash to prevent scarring. Over-the-counter pain relievers such as acetaminophen or ibuprofen can help reduce fever and discomfort.'
            },
            {
                'name': 'Strep Throat',
                'symptoms': ['sore_throat', 'fever', 'swollen_glands'],
                'description': 'Strep throat is a bacterial infection that causes inflammation and soreness of the throat, often accompanied by fever and swollen lymph nodes in the neck.',
                'treatment': 'Take antibiotics as prescribed by a doctor to treat the bacterial infection. Rest, drink plenty of fluids, and use over-the-counter pain relievers such as acetaminophen or ibuprofen to alleviate symptoms.'
            },
            {
                'name': 'Gastroenteritis',
                'symptoms': ['vomiting', 'diarrhea', 'abdominal_pain'],
                'description': 'Gastroenteritis, commonly known as stomach flu, is an inflammation of the stomach and intestines caused by viral or bacterial infection. Symptoms include diarrhea, vomiting, stomach cramps, and fever.',
                'treatment': 'Stay hydrated with electrolyte solutions, eat bland foods like rice and toast, and rest. Seek medical attention if symptoms worsen or persist. In severe cases, hospitalization may be necessary.'
            },
            {
                'name': 'Asthma',
                'symptoms': ['cough', 'shortness_of_breath'],
                'description': 'Asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways, leading to wheezing, shortness of breath, chest tightness, and coughing.',
                'treatment': 'Use inhalers as prescribed to control symptoms and prevent asthma attacks. Avoid triggers such as allergens and irritants, and seek medical help if symptoms worsen despite treatment.'
            },
            {
                'name': 'Ear Infection',
                'symptoms': ['ear_pain', 'fever', 'difficulty_sleeping'],
                'description': 'An ear infection, or otitis media, is an inflammation of the middle ear often caused by bacterial or viral infection. Symptoms include ear pain, fever, and sometimes hearing loss.',
                'treatment': 'Take antibiotics as prescribed by a doctor to treat the bacterial infection. Apply warm compresses to the ear to relieve pain, and use over-the-counter pain relievers such as acetaminophen or ibuprofen.'
            },
            {
                'name': 'Allergies',
                'symptoms': ['runny_nose', 'sneezing', 'itchy_eyes', 'itchiness'],
                'description': 'Allergies occur when the immune system reacts abnormally to substances that are usually harmless, such as pollen, dust mites, pet dander, or certain foods. Symptoms vary depending on the allergen but commonly include sneezing, runny nose, itchy eyes, and rash.',
                'treatment': 'Avoid allergens whenever possible. Take antihistamines to relieve symptoms, and use nasal sprays as prescribed. In severe cases, allergy shots (immunotherapy) may be recommended.'
            },
            {
                'name': 'Measles',
                'symptoms': ['fever', 'cough', 'rash', 'sore_throat'],
                'description': 'Measles is a highly contagious viral infection characterized by high fever, cough, runny nose, rash, and red, watery eyes. Complications can include pneumonia, encephalitis, and death.',
                'treatment': 'Rest, stay hydrated, and take fever-reducing medication. Seek medical attention if complications such as pneumonia or encephalitis arise. Vaccination with the measles, mumps, and rubella (MMR) vaccine can prevent measles.'
            },
            {
                'name': 'Hand, Foot, and Mouth Disease',
                'symptoms': ['fever', 'sore_throat', 'rash'],
                'description': 'Hand, foot, and mouth disease is a viral infection common in children under 5 years old. It is characterized by fever, sore throat, rash, and blisters on the hands, feet, and mouth.',
                'treatment': 'Rest, stay hydrated, and use over-the-counter pain relievers to reduce fever and discomfort. Avoid close contact with others to prevent spread. Symptoms usually resolve on their own within a week.'
            },
            {
                'name': 'Diabetes',
                'symptoms': ['excessive_thirst', 'frequent_urination', 'fatigue'],
                'description': 'Diabetes is a chronic condition characterized by high blood sugar levels due to insufficient production of insulin (Type 1 diabetes) or the body\'s inability to use insulin effectively (Type 2 diabetes). Symptoms of high blood sugar include frequent urination, increased thirst, and unexplained weight loss.',
                'treatment': 'Monitor blood sugar levels regularly, adhere to a balanced diet, take insulin or oral medications as prescribed, exercise regularly, and maintain a healthy lifestyle. Regular medical check-ups are essential for proper management of diabetes.'
            },
            {
                'name': 'Paranasal Sinusitis',
                'symptoms': ['facial_pain', 'headache', 'nasal_congestion', 'cough'],
                'description': 'Paranasal sinusitis, or sinus infection, is an inflammation of the paranasal sinuses caused by viral, bacterial, or fungal infection. Symptoms include facial pain, nasal congestion, headache, and postnasal drip.',
                'treatment': 'Use saline nasal sprays to help clear nasal passages, apply warm compresses to relieve facial pain, take over-the-counter pain relievers such as acetaminophen or ibuprofen, and stay hydrated. In some cases, antibiotics may be prescribed for bacterial sinusitis.'
            },
            {
                'name': 'Diarrheal Diseases',
                'symptoms': ['abdominal_pain', 'diarrhea', 'vomiting', 'dehydration'],
                'description': 'Diarrheal diseases are gastrointestinal infections that cause frequent loose stools, abdominal cramps, and sometimes vomiting and fever. They can be caused by viruses, bacteria, or parasites.',
                'treatment': 'Stay hydrated with clear fluids such as water, broth, or oral rehydration solutions to replace lost fluids and electrolytes. Eat bland foods like bananas, rice, and toast, and avoid dairy and fatty foods. Seek medical attention if symptoms persist or worsen.'
            },
            {
                'name': 'Coronary Artery Disease (CAD)',
                'symptoms': ['chest_pain', 'shortness_of_breath', 'heart_attack'],
                'description': 'Coronary artery disease is a condition characterized by the narrowing or blockage of the coronary arteries, usually caused by atherosclerosis. Symptoms can include chest pain (angina), shortness of breath, and heart attack.',
                'treatment': 'Lifestyle changes such as a healthy diet, regular exercise, and smoking cessation. Medications like statins, beta-blockers, and aspirin. Medical procedures including angioplasty, stent placement, and coronary artery bypass surgery.'
            },
            {
                'name': 'Heart Failure',
                'symptoms': ['shortness_of_breath', 'fatigue', 'swelling', 'rapid_heartbeat'],
                'description': 'Heart failure, also known as congestive heart failure, occurs when the heart is unable to pump blood efficiently. Symptoms include shortness of breath, fatigue, swelling in the legs, ankles, and feet, and a rapid or irregular heartbeat.',
                'treatment': 'Lifestyle changes such as a low-sodium diet, fluid restriction, and regular exercise. Medications like ACE inhibitors, beta-blockers, and diuretics. Devices such as pacemakers and defibrillators. Surgery may include heart valve repair or replacement.'
            },
            {
                'name': 'Arrhythmia',
                'symptoms': ['palpitations', 'dizziness', 'shortness_of_breath', 'chest_pain'],
                'description': 'Arrhythmia is a condition in which the heart beats with an irregular or abnormal rhythm. Symptoms can include palpitations, dizziness, shortness of breath, and chest pain.',
                'treatment': 'Medications such as antiarrhythmic drugs, beta-blockers, and calcium channel blockers. Medical procedures like cardioversion, ablation, and implantation of pacemakers or defibrillators. Lifestyle changes and managing underlying conditions.'
            },
            {
                'name': 'Hypertension',
                'symptoms': ['headache', 'dizziness', 'blurred_vision', 'shortness_of_breath'],
                'description': 'Hypertension, or high blood pressure, is a condition where the force of the blood against the artery walls is too high. Symptoms are often not noticeable but can include headache, dizziness, blurred vision, and shortness of breath.',
                'treatment': 'Lifestyle changes such as a healthy diet, regular exercise, weight loss, and reduced salt intake. Medications like diuretics, ACE inhibitors, beta-blockers, and calcium channel blockers. Regular monitoring of blood pressure.'
            },
            {
                'name': 'Chronic Obstructive Pulmonary Disease (COPD)',
                'symptoms': ['chronic_cough', 'shortness_of_breath', 'wheezing', 'chest_tightness'],
                'description': 'COPD is a chronic inflammatory lung disease that causes obstructed airflow from the lungs. Symptoms include chronic cough, shortness of breath, wheezing, and chest tightness.',
                'treatment': 'Smoking cessation, bronchodilators, inhaled steroids, pulmonary rehabilitation, and oxygen therapy. In severe cases, surgery such as lung volume reduction or lung transplant may be needed.'
            },
            {
                'name': 'Chronic Kidney Disease (CKD)',
                'symptoms': ['fatigue', 'swelling', 'changes_in_urination', 'shortness_of_breath'],
                'description': 'Chronic kidney disease is the gradual loss of kidney function. Symptoms include fatigue, swelling in the legs and ankles, changes in urination patterns, and shortness of breath.',
                'treatment': 'Managing underlying conditions like diabetes and hypertension, medications to relieve symptoms and slow progression, dietary changes, and in severe cases, dialysis or kidney transplant.'
            },
            {
                'name': 'Peptic Ulcer Disease',
                'symptoms': ['abdominal_pain', 'bloating', 'nausea', 'vomiting'],
                'description': 'Peptic ulcer disease is characterized by sores or ulcers in the lining of the stomach or duodenum. Symptoms include abdominal pain, bloating, nausea, and vomiting.',
                'treatment': 'Antibiotics to treat H. pylori infection, proton pump inhibitors, H2-receptor antagonists, and antacids. Avoiding NSAIDs, alcohol, and smoking. Eating smaller, more frequent meals.'
            },
            {
                'name': 'Hepatitis B',
                'symptoms': ['fatigue', 'jaundice', 'abdominal_pain', 'loss_of_appetite'],
                'description': 'Hepatitis B is a viral infection that attacks the liver. Symptoms include fatigue, jaundice, abdominal pain, and loss of appetite.',
                'treatment': 'Antiviral medications, regular monitoring of liver function, and in severe cases, liver transplant. Vaccination can prevent hepatitis B infection.'
            },
            {
                'name': 'Rheumatoid Arthritis',
                'symptoms': ['joint_pain', 'stiffness', 'swelling', 'fatigue'],
                'description': 'Rheumatoid arthritis is an autoimmune disorder that primarily affects joints. Symptoms include joint pain, stiffness, swelling, and fatigue.',
                'treatment': 'Medications like disease-modifying antirheumatic drugs (DMARDs), biological agents, pain relievers, and steroids. Physical therapy and lifestyle changes. Surgery in severe cases.'
            },
            {
                'name': 'Depression',
                'symptoms': ['persistent_sadness', 'loss_of_interest', 'fatigue', 'changes_in_sleep'],
                'description': 'Depression is a mood disorder characterized by persistent sadness, loss of interest in activities, and a variety of physical and emotional problems.',
                'treatment': 'Psychotherapy, medications like antidepressants, lifestyle changes, and support from family and friends. In severe cases, electroconvulsive therapy (ECT) or other brain stimulation therapies.'
            },
            {
                'name': 'Anxiety Disorders',
                'symptoms': ['excessive_worry', 'restlessness', 'fatigue', 'difficulty_concentrating'],
                'description': 'Anxiety disorders are characterized by excessive fear or anxiety. Symptoms include excessive worry, restlessness, fatigue, and difficulty concentrating.',
                'treatment': 'Psychotherapy, medications like anti-anxiety drugs or antidepressants, lifestyle changes, and stress management techniques.'
            }
        ]

