from base import KnowledgeBase

class ExpertSystem:
    def __init__(self, patient_symptoms):
        self.symptoms = patient_symptoms
        self.diseases = KnowledgeBase().diseases
        self.result = {}

    def calculate_shared_symptoms(self, disease_symptoms):
        total_shared_severity = 0
        for symptom in disease_symptoms:
            if symptom in self.symptoms:
                total_shared_severity += self.symptoms[symptom]
        return total_shared_severity    

    def diagnose_disease(self):
        max_shared_symptoms = 0
        likely_disease = None    
        for disease in self.diseases:
            shared_symptoms = self.calculate_shared_symptoms(disease["symptoms"])
            if shared_symptoms > max_shared_symptoms:
                max_shared_symptoms = shared_symptoms
                likely_disease = disease
        return {
            "name": likely_disease["name"],
            "treatment": likely_disease["treatment"],
        }

    def run(self):
        return self.diagnose_disease()



if __name__ == "__main__":
    patient_data = {
        "fever": True,
        "cough": True,
        "runny_nose": True,
        "sore_throat": True,
        "fatigue": True,
        "body_aches": True,
        "rash": True,
        "itchiness": True,
        "swollen_glands": True,
        "vomiting": True,
        "diarrhea": True,
        "abdominal_pain": True,
        "wheezing": True,
        "difficulty_breathing": True,
        "ear_pain": True,
        "difficulty_sleeping": True,
        "sneezing": True,
        "itchy_eyes": True,
        "high_fever": True,
        "blisters": True,
        "excessive_thirst": True,
        "frequent_urination": True,
        "unexplained_weight_loss": True,
        "facial_pain": True,
        "headache": True,
        "nasal_congestion": True,
        "dehydration": True
    }

    engine = ExpertSystem(patient_data)
    result = engine.run()