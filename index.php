<?php

header('Content-Type: application/json; charset=utf-8');

function json_indent($json)
{
	$result      = '';
	$pos         = 0;
	$strLen      = strlen($json);
	$indentStr   = '  ';
	$newLine     = "\n";
	$prevChar    = '';
	$outOfQuotes = true;

	for ($i=0; $i<=$strLen; $i++)
	{
		// Grab the next character in the string.
		$char = substr($json, $i, 1);

		// Are we inside a quoted string?
		if ($char == '"' && $prevChar != '\\') {
			$outOfQuotes = !$outOfQuotes;

			// If this character is the end of an element,
			// output a new line and indent the next line.
		} else if(($char == '}' || $char == ']') && $outOfQuotes) {
			$result .= $newLine;
			$pos --;
			for ($j=0; $j<$pos; $j++) {
				$result .= $indentStr;
			}
		}

		// Add the character to the result string.
		$result .= $char;

		// If the last character was the beginning of an element,
		// output a new line and indent the next line.
		if (($char == ',' || $char == '{' || $char == '[') && $outOfQuotes) {
			$result .= $newLine;
			if ($char == '{' || $char == '[') {
				$pos ++;
			}

			for ($j = 0; $j < $pos; $j++) {
				$result .= $indentStr;
			}
		}

		$prevChar = $char;
	}

	return $result;
}

$news = $_REQUEST["news"];
$keyinput = $_REQUEST["key"];
$key = "API_KEY";

if($keyinput == ""){
$myfile = fopen("cache.txt", "r") or die("Unable to open file!");
$teks = fread($myfile,filesize("cache.txt"));
fclose($myfile);

//echo json_encode($teks, JSON_PRETTY_PRINT);
echo json_indent($teks);
}
else {
$txt = $news;


if(strcmp($keyinput, $key) == 0) { 
  $myfile = fopen("cache.txt", "w") or die("Unable to open file!");
  fwrite($myfile, $txt);
  fclose($myfile);
  echo "Done!";
}
else {
  echo "Key Invalid";
  fclose($myfile);
}
}

?>