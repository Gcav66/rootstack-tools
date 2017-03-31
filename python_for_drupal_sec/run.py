# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:03:35 2017

@author: Gus Cavanaugh
"""

import csv
import requests


if __name__ == "__main__":
    contact_list = []
    error_list = []
    with open("data.csv", "rb") as myfile:
        for row in myfile:
            url = "http://" + row.strip()
            try:
                resp = requests.get(url)
            except:
                error_list.append(row.strip())
            if resp.status_code == 200:
                contact_list.append(url)
            else:
                print "Good " + url
            
    