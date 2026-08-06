class Address:
    def __init__(self,street,city,pincode):

        if len(street)<=0:
                raise ValueError("Invalid street")
        else:
             self.street=street

        if len(city)<=0:
             raise ValueError("Invalid City.")
        else:
             self.city=city
        
        if len(pincode)<0:
            raise ValueError("Pincode must be 6 digit.")
        else:
            self.pincode=pincode

    def showAddressDetails(self):
        return "Street Name :", self.street,"City Name :", self.city ,"Pincode :", self.pincode         

    