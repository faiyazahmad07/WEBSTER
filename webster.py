import requests
from optparse import OptionParser
from urllib.parse import urlparse, urljoin
from colorama import Fore
import threading
parser = OptionParser()
parser.add_option('-u',dest='url', help="Enter the URL")
parser.add_option('-p',dest='payloads', help= "Enter payload file")
parser.add_option('-t',dest='thread',help="Enter thread value(1: Fastest 100: Normal)")
parser.add_option('-w',dest='whitelist_domain',help="Enter whitelisted domain")
parser.add_option('-c',dest='cookies',help='Enter cookies value(For authenticated endpoints) ')
val, arguments = parser.parse_args()

url = val.url
payload_file = val.payloads
#print(urljoin('https://google.com/index.php','?redirec=true'))

print(Fore.BLUE+"""
       __        __   _         _
       \ \      / /__| |__  ___| |_ ___ _ __
 	\ \ /\ / / _ \ '_ \/ __| __/ _ \ '__|
 	 \ V  V /  __/ |_) \__ \ ||  __/ |
	  \_/\_/ \___|_.__/|___/\__\___|_|
	     Open Redirection Scanner
		 By: Faiyaz Ahmad
	        @bepractical.tech
	""")

class Scanner:
	def __init__(self,url,payload_file):
		process = []
		self.url = url
		self.payload_file = payload_file
		#self.scanner()
		payloads = self.payload_parser()
		'''
		mid = int(len(payloads) / 2)
		payload1 = payloads[0:mid]
		payload2 = payloads[mid::]
		process1 = threading.Thread(target=self.scanner, args=(payload1,))
		process2 = threading.Thread(target=self.scanner, args=(payload2,))
		process1.start()
		process2.start()
		process1.join()
		process2.join()
		#print(len(payload2))
		'''
		global final_payload
		if val.thread:
			final_payload = self.divide_list(payloads,int(val.thread))
		else:
		 	final_payload = self.divide_list(payloads,100)
		#print(Fore.WHITE + f'{len(final_payload)}')
		index = 0
		if not val.cookies:
			for i in final_payload:
				#print(len(i))
				process.append(threading.Thread(target=self.scanner,args=(i,)))
				process[index].start()
				index += 1
		else:
			for i in final_payload:
                                #print(len(i))
                                process.append(threading.Thread(target=self.scanner,args=(i,self.cookies_parser(val.cookies))))
                                process[index].start()
                                index += 1
		#print(len(final_payload))

	def divide_list(self,list,n):
		final_arr = []
		for i in range(0,len(list),n):
			#print(len(list[i:i+n]))
			final_arr.append(list[i:i+n])
		return final_arr

	def open_file(self):
		payload = []
		with open(self.payload_file,'r') as data:
			full_data = data.read().split()
			for i in full_data:
				payload.append(i)
			data.close()
		return payload

	def payload_parser(self):
		final_payloads = []
		total_payload = self.open_file()
		for payload in total_payload:
			if 'whitelist' in payload:
				final_payload = payload.replace('%whitelist%',val.whitelist_domain)
				final_payloads.append(final_payload)
				continue
			final_payloads.append(payload)
		print(Fore.GREEN + f'[+]{ len(final_payloads)} PAYLOADS LOADED')
		return final_payloads

	def cookies_parser(self,value):
		dict = {}
		value = value.split(';')
		for i in value:
			i = i.split('=')
			dict[i[0]] = i[1]
		return dict

	def parse_url(self,url,payload):
		final_url = urljoin(url,f'?{urlparse(url).query.split("=")[0]}={payload}')
		return final_url

	def scanner(self,payloads,cookies=None):
		#payloads = self.payload_parser()
		for payload in payloads:
			url = self.parse_url(self.url,payload)
			try:
				if not cookies:
					response = requests.get(url,allow_redirects=False)
				else:
					response = requests.get(url,allow_redirects=False,cookies=cookies)
			except UnicodeDecodeError:
				continue
			#print(response.text)
#			print(payload)
			try:
				net_loc = urlparse(response.headers['Location']).netloc
			except KeyError:
				continue
#			print(url)
			#print(len(net_loc))
			if 'example.com' in net_loc:
				print(Fore.RED + f'Vulnerable {url}')
			if not len(net_loc):
				#print(Fore.BLUE + f'Possible Open Redirection with {url}')
				continue
			if response.status_code in range(400,500):
				print(Fore.RED +f"Warning: GETTING {response.status_code}")
				continue
#AKIAR4YEYRJL6JKBNRGP

Scanner(url,payload_file)

