<?php
    $name = $_GET['name'];
    if($name != ""){
        echo "Welcome, $name";
    } else {
        echo "MAKE VALID ENTRY";
    }
?>