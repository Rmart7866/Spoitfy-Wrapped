<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="author" content="Ryan Martin">
        <title>My Wrapped</title>
        <meta name="description" content="spotify wrapped :)">
        <link href="webpage.css" rel="stylesheet" type="text/css" media="screen" />
    </head>
    <body>
    	<header>
    		<h1>CS 120</h1>
            <h2>Spotify Wrapped</h2>
    	</header>
        
        <?php
            $rand_number = rand();
            while (file_exists($rand_number)) {
                $rand_number = rand();
            }
            //make a dierctory with a random number
            $command_mkdir = escapeshellcmd("mkdir " . $rand_number);
            $output_mkdir = shell_exec($command_mkdir);
            //copy all the files into a folder 
            $output_cp = shell_exec("cp test.csv " . $rand_number);
            $output_cp = shell_exec("cp test2.csv " . $rand_number);
            $output_cp = shell_exec("cp test3.csv " . $rand_number);
            //call c++ file
            $command_cp2 = escapeshellcmd("cp wrapped.cpp " . $rand_number);
            $output_cp2 = shell_exec($command_cp2);
            //run c++ in this directory that was created
            $output = shell_exec("cd " . $rand_number . ";g++ -std=c++1y -o wrapped.exe wrapped.cpp;./wrapped.exe; cd ..");
            // Print the output from the C++ program to the webpage.
            echo $output;
            
            //delete the directory 
            array_map("unlink", glob($rand_number . "/*"));
            rmdir($rand_number);

        ?>
        
    </body>
</html>