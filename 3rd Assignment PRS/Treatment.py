class Treatment:

    def __init__(self,treatment_id,treatment_name,cost):

        self.set_treatment_id(treatment_id)
        self.set_treatment_name(treatment_name)
        self.set_cost(cost)

    # =====================
    # Getters

    def get_treatment_id(self):
        return self.treatment_id

    def get_treatment_name(self):
        return self.treatment_name

    def get_cost(self):
        return self.cost

    # =====================
    # Setters

    def set_treatment_id(self, treatment_id):

        if treatment_id <= 0:
            raise ValueError(
                "Treatment ID must be positive"
            )

        self.treatment_id = treatment_id

    def set_treatment_name(
            self,
            treatment_name):

        if not treatment_name.strip():
            raise ValueError(
                "Treatment name cannot be empty"
            )

        self.treatment_name = treatment_name

    def set_cost(self, cost):

        if cost <= 0:
            raise ValueError(
                "Treatment cost must be greater than 0"
            )

        self.cost = cost

    def display_treatment(self):

        print(f"Treatment ID   : {self.treatment_id}")
        print(f"Treatment Name : {self.treatment_name}")
        print(f"Cost           : ₹{self.cost}")