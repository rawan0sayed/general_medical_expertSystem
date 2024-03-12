class Controller():
    def __int__(self):
        self.diseases_list = []
        self.diseases_symptoms = []
        self.symptom_map = {}
        self.d_desc_map = {}
        self.d_treatment_map = {}

    def preprocess(self):
        # global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
        diseases = open("diseases/diseases.txt")
        diseases_t = diseases.read()
        diseases_list = diseases_t.split("\n")
        diseases.close()
        for disease in diseases_list:
            disease_s_file = open("diseases/symptoms/" + disease + ".txt")
            disease_s_data = disease_s_file.read()
            s_list = disease_s_data.split("\n")
            self.diseases_symptoms.append(s_list)
            self.symptom_map[str(s_list)] = disease
            disease_s_file.close()

            disease_s_file = open("diseases/descriptions/" + disease + ".txt")
            disease_s_data = disease_s_file.read()
            self.d_desc_map[disease] = disease_s_data
            disease_s_file.close()

            disease_s_file = open("diseases/treatments/" + disease + ".txt")
            disease_s_data = disease_s_file.read()
            self.d_treatment_map[disease] = disease_s_data
            disease_s_file.close()

    def identify_disease(self, *arguments):
        symptom_list = []
        for symptom in arguments:
            symptom_list.append(symptom)
        return self.symptom_map[str(symptom_list)]

    def get_details(self, disease):
        return self.d_desc_map[disease]

    def get_treatments(self, disease):
        return self.d_treatment_map[disease]

    def if_not_matched(self, disease):
        print("")
        id_disease = disease
        disease_details = self.get_details(id_disease)
        treatments = self.get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" % (id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print("The common medications and procedures suggested by other real doctors are: \n")
        print(treatments + "\n")