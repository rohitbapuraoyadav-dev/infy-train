class Address:
    def __init__(self,street,city,pincode):
        self.street=street
        self.city=city
        self.pincode=pincode



    def showAddressDetails(self):
        return "Street Name :", self.street,"City Name :", self.city ,"Pincode :", self.pincode         

    