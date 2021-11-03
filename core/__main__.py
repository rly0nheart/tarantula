import sys
import time
import logging
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from assets.COLORS import RED,WHITE,GREEN,YELLOW,RESET

class Tarantula:		
	def __init__(self):
		self.internal_urls = set()
		self.external_urls = set()
		self.total_urls_visited = 0
		
	# check if url is valid (returns True or False)						
	def is_valid(self,url):
	   parsed = urlparse(url)
	   return bool(parsed.netloc) and bool(parsed.scheme)
	
	# get all the links from a specified website   
	def get_all_website_links(self,url):
	   urls = set()
	   # domain name of the URL without the protocol
	   domain_name = urlparse(url).netloc
	   soup = BeautifulSoup(requests.get(url).content, "html.parser")
	   for a_tag in soup.findAll("a"):
	       href = a_tag.attrs.get("href")
	       if href == "" or href is None:
	           # Continue if href is an empty tag
	           continue
	           
	       # join the URL if it's relative (not absolute link)
	       href = urljoin(url, href)
	       parsed_href = urlparse(href)
	       # remove URL GET parameters, URL fragments
	       href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
	       if not self.is_valid(href):
	           # Continue if URL is not valid
	           continue
	           
	       if href in self.internal_urls:
	           # Continue if URL is already in the set
	           continue
	           
	       if domain_name not in href:
	           if href not in self.external_urls:
	               print(f"{WHITE}* external_link:{GREEN} {href}")
	               time.sleep(0.08)
	               self.external_urls.add(href)
	               continue
	               
	       print(f"{WHITE}* internal_link:{GREEN} {href}")
	       time.sleep(0.08)
	       urls.add(href)
	       self.internal_urls.add(href)
	   print(f"{WHITE}* Finished crawling {RED}{url}{RESET}\n")
	   return urls
	   	   
	
	def main(self,url,max_urls):
		count = 0
		count = count + 1
		self.crawl(url,max_urls)
		domain_name = urlparse(url).netloc				    
	   
	def crawl(self,url,max_urls = 30):
	   global total_urls_visited
	   
	   self.total_urls_visited += 1
	   links = self.get_all_website_links(url)
	   for link in tqdm(links):
	       if self.total_urls_visited >= max_urls:
	           break
	          
	       self.crawl(link,max_urls)
