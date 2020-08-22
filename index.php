<form action="index.php" method="POST">
	<input type="text" name="username" placeholder="username"><br>
	<input type="text" name="content" placeholder="comment"><br>
	<input type="hidden" name="newcomment" value="1">
	<input type="submit"><br>
</form>
<?php
$db = new SQLite3('data.sqlite', SQLITE3_OPEN_CREATE | SQLITE3_OPEN_READWRITE);
//Create table
$db->query('CREATE TABLE IF NOT EXISTS "comments" (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	"username" VARCHAR,
	"comment" VARCHAR
)');

if($_POST['newcomment'] == 1)
{
	$db->exec('BEGIN');
	$db->query('INSERT INTO "comments" ("username", "comment")
		VALUES ("'. $_POST['username'] .'", "'. $_POST['content'] .'")');
	$db->exec('COMMIT');
}

?>
