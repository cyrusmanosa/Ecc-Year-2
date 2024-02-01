<?php
    include_once('DB.php');
    $op ='none';
    if( isset($_GET['op']) ) $op = $_GET['op'];

    if( $op == 'logout' ){ Logout(); }

    if( $op == 'checklogin' ){ checklogin($_POST['staffid'],$_POST['password']); }
    
    function manage()
    {
        
    }
    function Logout()
    {
        session_start();
        session_destroy();
        header("Location:index.php");
    }

    function checklogin($staffId, $password)
    {
        global $dbConnection;
        $staffQ = mysqli_query($dbConnection, " SELECT * FROM `Staff` WHERE `Sid` = '.$staffId.' ");
        $staff = mysqli_fetch_assoc($staffQ);
        $hashPassword = password_hash($password , PASSWORD_BCRYPT, [ "cost" => 12 ] );

        if($staffId != $staff['staffid'] && !var_dump(password_verify($staff['password'], $hahashPasswordsh)) )
        {
            session_start();
            $_SESSION['staffid'] = $_POST['staffid'];
            header("Location: menu.php");
        }
        else
        {   
            $ERROR = "Check!";
            header("Location: index.php"); 
        }
    }
?>
