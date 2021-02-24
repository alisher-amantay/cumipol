#creating a json file input.json
import json
#input JSON format
loan_obj = {
    "Initial" : 100000, #loan amount
    "APR" : 5.00, #annual percentage rate
    "N of payments" : 48, #number of payments that will be made, usually n of months
    "start": 1, #beginning of desired period, preferrably integer
    "end": 48, #end of desired period, preferrably lower than 'N of payments'
    "Pay in year": 12 #usually 12 for each month
}
with open("input.json", "w") as outfile:
    json.dump(loan_obj, outfile)
