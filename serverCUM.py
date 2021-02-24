#server code
from http.server import HTTPServer, BaseHTTPRequestHandler
import json, urllib.parse

def rate_pay (rate_ann, pay_in_year):
    #in format 1.__ (higher than 1)
    return 1+rate_ann/float(100*pay_in_year)

#calculate payment per period
def per_pay (rate_pay, PV, n_per):
    per_pay = (rate_pay-1)*PV/(1-(rate_pay)**(-n_per))
    return per_pay

#main function that calculates CUMIPOL
def c_interest (per_pay, rate_pay, PV, start, end):
    n_of_cum = list(range(start, end+1))
    left = PV
    period = 0
    intr_sum = 0
    while int(left) > 0:
        period += 1
        intr_one = left*(rate_pay-1)
        if period in n_of_cum:
            intr_sum+=intr_one
        left = left - (per_pay - intr_one)
    return intr_sum

#Defining server functions
class CUMIPOL(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        #reads the length of the Headers
        length = int(self.headers['Content-Length'])
        #reads the contents of the request
        content = self.rfile.read(length)
        self.end_headers()
        return content
    #GET Method Definition
    def do_GET(self):
        #defining headers
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        data="Submit a POST statement in form of JSON with loan, for format proceed to Github"
        self.wfile.write(data.encode())
    #POST method
    def do_POST(self):
        loan_param = json.loads(self._set_headers().decode())
        rate = rate_pay(float(loan_param['APR']),int(loan_param['Pay in year']))
        PV = float(loan_param['Initial'])
        per_payment = per_pay(rate, PV, int(loan_param['N of payments']))
        CUMP = c_interest(per_payment, rate, PV, int(loan_param['start']), int(loan_param['end']))
        self.wfile.write(str(CUMP).encode())
        #Server Initialization

server = HTTPServer(('127.0.0.1',8080), CUMIPOL)
server.serve_forever()
