<?php
if (!isset($_SESSION['username']))
    session_start();

if (isset($_SESSION['username'])){

    require '../top_header/bar_LI.html';
    require '../index_page/index.html';
} else{
    require '../top_header/bar_LO.html';
    require '../index_page/index.html';
}
?>