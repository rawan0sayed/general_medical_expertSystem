class ExpertSystem:
    def _init_(self, patient_symptoms):

        self.symptoms = patient_symptoms

        self.diseases = [
            {
                'name': 'Common Cold',
                'symptoms': ['fever', 'cough', 'runny nose', 'sore throat', 'fatigue'],
                'treatment': 'Get plenty of rest, stay hydrated, and take over-the-counter cold medication.',
            },
            {
                'name': 'Flu',
                'symptoms': ['fever', 'cough', 'fatigue', 'body aches'],
                'treatment': 'Rest, drink fluids, and take antiviral medication if prescribed by a doctor.',
            },
            {
                'name': 'Chickenpox',
                'symptoms': ['fever', 'rash', 'itchiness', 'fatigue'],
                'treatment': 'Apply calamine lotion, take oatmeal baths, and avoid scratching the rash.',
            },
            {
                'name': 'Strep Throat',
                'symptoms': ['sore throat', 'fever', 'swollen glands'],
                'treatment': 'Take antibiotics as prescribed by a doctor, rest, and drink plenty of fluids.',
            },
            {
                'name': 'Gastroenteritis',
                'symptoms': ['vomiting', 'diarrhea', 'abdominal pain'],
                'treatment': 'Stay hydrated, eat bland foods, and rest. Seek medical attention if symptoms worsen.',
            },
            {
                'name': 'Asthma',
                'symptoms': ['cough', 'wheezing', 'difficulty breathing'],
                'treatment': 'Use inhalers as prescribed, avoid triggers, and seek medical help if symptoms worsen.',
            },
            {
                'name': 'Ear Infection',
                'symptoms': ['ear pain', 'fever', 'difficulty sleeping'],
                'treatment': 'Take antibiotics as prescribed, apply warm compresses, and use over-the-counter pain relievers.',
            },
            {
                'name': 'Allergies',
                'symptoms': ['runny nose', 'sneezing', 'itchy eyes', 'itchiness'],
                'treatment': 'Avoid allergens, take antihistamines, and use nasal sprays as prescribed.',
            },
            {
                'name': 'Measles',
                'symptoms': ['high fever', 'cough', 'rash', 'sore throat'],
                'treatment': 'Rest, stay hydrated, and take fever-reducing medication. Seek medical attention if complications arise.',
            },
            {
                'name': 'Hand, Foot, and Mouth Disease',
                'symptoms': ['fever', 'sore throat', 'rash', 'blisters'],
                'treatment': 'Rest, stay hydrated, and use over-the-counter pain relievers. Avoid close contact with others to prevent spread.',
            },
            {
                'name': 'Diabetes',
                'symptoms': ['excessive thirst', 'frequent urination', 'fatigue', 'unexplained weight loss'],
                'treatment': 'Monitor blood sugar levels, adhere to a balanced diet, take insulin as prescribed, and exercise regularly.',
            },
            {
                'name': 'Paranasal Sinusitis',
                'symptoms': ['facial pain', 'headache', 'nasal congestion', 'cough'],
                'treatment': 'Use saline nasal sprays, apply warm compresses, take over-the-counter pain relievers, and stay hydrated.',
            },
            {
                'name': 'Diarrheal Diseases',
                'symptoms': ['abdominal pain', 'diarrhea', 'vomiting', 'dehydration'],
                'treatment': 'Stay hydrated, eat bland foods, and avoid dairy and fatty foods. Seek medical attention if symptoms persist or worsen.'
            }
        ]

    def get_symptoms(self):
        print("Please answer with yes or no.")
        for symptom in self.symptoms.keys():
            response = input(f"Do you have {symptom}? ").lower()
            if response == 'yes':
                self.symptoms[symptom] = True

    def diagnose_disease(self):
        max_shared_symptoms = 0
        likely_disease = None
        
        for disease, disease_symptoms in self.diseases.items():
            shared_symptoms = sum(self.symptoms[symptom] for symptom in disease_symptoms if symptom in self.symptoms)
            if shared_symptoms > max_shared_symptoms:
                max_shared_symptoms = shared_symptoms
                likely_disease = disease

        return {likely_disease, self.get_treatment(likely_disease)}

    def get_treatment(self, disease):
        if disease in self.treatments:
            return self.treatments[disease]

    def run(self):
        self.diagnose_disease()

if __name__ == "__main__":
    data = {}
    expert_system = ExpertSystem(data)
    expert_system.run()
