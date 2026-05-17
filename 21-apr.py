'''1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation'''

pa = int(input("Policy Age = "))
ca = int(input("Claim Amount = "))
at = input("Accident Type (minor/major) = ")

if pa>=2:
    if ca<=50000:
        if at =="minor":
            print("approve the claim")
        else:
            print("approve it with inspection")
    
    elif ca>50000 and ca<=200000:
        if at=="major":
            print("approve with investigation")
        else:
            print("Reject")

    else:
        print("Reject")

else:
    if at == "minor":
        print("Reject")
    else:
        print("mark as pending review")


'''2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted
'''

m = int(input("Enter marks :"))
e = int(input("Entrance Score = "))
c = input("Enter category (General/others)= ")

if m>=70:
    if e>=80:
        if c == "general":
            print(" Admission Status = Admitted")
        else:
            print("Admission Status = Admitted with scholarship")
    elif e<80:
        if m>=85:
            print("Admission Status = Admitted under management quota")
        else:
            print("Admission Status = Reject")
        
elif m<70:
    if c!="general" and m>=60:
        if e>=70:
            print("Admission Status = waitlist")

else:
    print("Admission Status = Reject")



'''3. Smart Loan Risk Categorization

A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.

Input:
Salary = 40000
Credit Score = 760
Existing Loans = 1

Output:
Risk Level = Medium Risk'''

s = int(input("Salary = "))
cs = int(input("Credit Score = "))
el = int(input("Existing Loans = "))

if s>=30000:
    if cs>=750:
        if el==0:
            print("Risk Level = low risk")
        elif el>0 and el<=2:
            print("Risk Level = medium risk")
        else:
            print("Risk Level = high risk")

    elif cs<750:
        if s>=50000:
            if cs>=650:
                print("Risk Level = medium risk")
            else:
                print("Risk Level = high risk")
else:
    print("Not eligible")



'''4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test'''

sp = input("Enter subscription type : ")
p = int(input("Enter course progress (0-100) : "))
t = int(input("Enter test score (0-100) : "))


if sp =="premium":
    if p>=80:
        if t>=70:
            print("Access Status = unlock certificate")
        else:
            print("Access Status = Retry Test")
    elif p<80:
        print("Access Status = complete course")

elif sp =="basic":

    if t >=50:
        print("Access Status = limited access")
    else:
        print("Access Status = lock content")
else:
    print("Access Status = Access Denied")

'''5. Smart Warehouse Dispatch System
A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier'''

st= int(input("Enter Stock = "))
py= input("Enter Priority (high/low)= ")
d= int(input("Enter distance = "))

if st>=100:
    if py=="high":
        if d<=200:
            print("Dispatch Status = Dispatch Immediately ")
        else:
            print("Dispatch Status = Dispatch via Fast Courier")
    elif py!="high":
        if st>=300:
            print("Dispatch Status = Bulk Dispatch")
        else:
            print("Dispatch Status = Normal Dispatch")
else:
    if st>=50:
        if py=="high":
            print("Dispatch Status = Partially Dispatch")
        else:
            print("Dispatch Status = Dispatch hold")

    else:
        print("Out of stock")



'''6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged'''

ta = int(input("Enter Transaction Amount = "))
loc =  input("Enter Location (domestic/international) = ")
aa = int(input("Account Age = "))

if ta>=10000:
    if loc=="international":
        otp=input("Enter OTP = ")
        if otp=="1234":
            print("Allowed")
        else:
            print("Block")
    else:
        if ta>=50000:
            if aa>=2:
                print("allow")
            else:
                print("Flag")
        elif ta<50000:

            print("allow")
        
        
'''7. Ride Booking Surge Pricing System

A ride booking app calculates fare multiplier based on demand, time, and distance.

If demand is at least 80, then check time. If peak time, then check distance. If distance is at least 10, apply 2x fare; otherwise 1.5x. If not peak time, then check if demand is at least 90. If yes, 1.8x; otherwise 1.3x. If demand is less than 80, then check if demand is at least 50. If yes, then if peak time, apply 1.2x; otherwise normal fare. If demand is below 50, normal fare.

Input:
Demand = 85
Time = peak
Distance = 12

Output:
Fare Multiplier = 2x Fare'''

dmd = int(input("Enter demand = "))
time = input("Enter time (peak/not peak) = ")
dist = int(input("Enter distance = "))

if dmd>=80:
    if time=="peak":
        if dist>=10:
            print("Fare Multiplier = 2x Fare")
        else:
            print("Fare Multiplier = 1.5x Fare")
    elif time!="peak":
        if dmd>=90:
            print("Fare Multiplier = 1.8x Fare")
        else:
            print("Fare Multiplier = 1.3x Fare")
else:
    if dmd>=50:
        if time=="peak":
            print("Fare Multiplier = 1.2x Fare")
        else:
            print("Fare Multiplier = Normal Fare")
    else:
        print("Fare Multiplier = Normal Fare")

'''8. Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply'''

sm = int(input("Enter Soil moisture = "))
tmp = int(input("Enter temperature = "))
cr = input("Enter crop (Wheat/Not wheat) = ")
rf= input("enter rainfall(expected/Not expected) = ")

if sm<=30:
    if tmp>=35:
        if  cr=="wheat":
            print("Irrigation = High Water Supply")
        else:
             print("Irrigation = Moderate Water Supply")
    else:
        print("Irrigation = Moderate Water Supply")
elif sm>30:
    if sm<=60:
        if rf=="expected":
            print("Delay irrigation")
        else:
            print("Light irrigation")
    else:
        print("No irrigation")

'''9. Multi-Level Employee Promotion System

A company promotes employees based on experience, rating, projects completed, and salary.

If experience is at least 5 years, then check rating. If rating is at least 4, then check projects. If projects are at least 3, then check salary. If salary is up to 50000, promote with 30 percent hike; otherwise 20 percent hike. If projects are less than 3, promote with 10 percent hike. If rating is below 4, no promotion. If experience is less than 5, then check if rating is 5. If yes, fast track promotion; otherwise no promotion.

Input:
Experience = 6
Rating = 4
Projects = 2

Output:
Promotion Status = Promoted with 10% hike'''

ex = int(input("Enter Experiance = "))
rt = int(input("Enter Rating = "))
pr = int(input("Enter Projects = "))
sa = int(input("Enter Salary = "))
if ex>=5:
    if rt>=4:
        if pr>=3:
            if sa<=50000:
                print("Promotion Status = Promoted with 30% hike ")
            else:
                print("Promotion Status = Promoted with 20% hike ")
        else:
            print("Promotion Status = Promoted with 10% hike ")
    else:
        print("Promotion Status = No Promotion  ")
else:
    if rt==5:
        print("Promotion Status = fast track promotion")
    else:
        print("Promotion Status = No Promotion  ")

'''10. Smart Restaurant Order Processing System

A restaurant offers discounts and benefits based on order amount, customer type, and payment method.

If order amount is at least 2000, then check customer type. If VIP, then check payment method. If online, give free dessert and 20 percent discount; otherwise only free dessert. If not VIP, then check if amount is at least 5000. If yes, give 15 percent discount; otherwise 10 percent discount. If order amount is less than 2000, then check if it is at least 1000. If yes, then if customer is VIP, give 10 percent discount; otherwise 5 percent discount. If below 1000, no offer.

Input:
Order Amount = 2500
Customer Type = VIP
Payment Method = online

Output:
Offer = Free Dessert + 20% Discount'''

oa = int(input("Enter order amount = "))
ct = input("ENter Customer Type (VIP/non vip)= ")
pm = input("Enter payment method = ")
if oa>=2000:
    if ct=="VIP" or ct=="vip":
        if pm=="online":
            print("Offer = Free Dessert + 20% Discount")
        else:
            print("Offer = Free Dessert")
    else:
        if oa>=5000:
            print("Offer = 15% Discount")
        else:
            print("Offer = 10% Discount")
else:
    if oa>=1000:
        if ct=="VIP" or ct=="vip":
            print("Offer = 10% Discount")
        else:
             print("Offer = 5% Discount")
    else:
         print("Offer = No offer")