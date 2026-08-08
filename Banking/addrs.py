class Address:
    def __init__(self,street,city,pincode):

        if len(street)<=0:
            raise ValueError("Information cannot be empty.")
        else:
            self.street=street

        if len(city)<=0:
            raise ValueError("Mention city name.")
        else: 
            self.city=city

        if int(pincode)<=6:
            raise ValueError("Pincode cannot be less than 6 digits.")
        else:
            self.pincode=pincode

    def showAddressDetails(self):
        return f"""
        Street name: {self.street}
        City:{self.city}
        Pincode:{self.pincode}"""
        
    