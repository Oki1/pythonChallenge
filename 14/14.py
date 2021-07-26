import xmlrpc.client
con = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(con.phone("Bert"))