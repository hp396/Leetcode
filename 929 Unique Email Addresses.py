class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        domains =[]
        outputemail=[]
        for email in emails:
            address = email.split("@")[1]
            e = email.split("@")[0]
            if address in domains:
                if "." in e or "+" in e:
                    if "." in e:
                        e = e.replace(".","")
                    if "+" in e:
                        e = e.split("+", 1)[0]
                        print(e)

                if e not in outputemail: outputemail.append(e)
                        
                        
                     
            if address not in domains:
                domains.append(address)
                if "." in e:
                    e = e.replace(".","")
                if "+" in e:
                    e = e.split("+", 1)[0]
                outputemail.append(e)
                    
        return int(len(outputemail))
