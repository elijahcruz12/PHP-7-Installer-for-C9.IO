# PHP 7 Installer Script for C9.IO!

Installs PHP 7 onto your C9 IDE.<br>
Version 1.0

## One-Line Install and Run Script.
To install the script then run it, just use this one liner:

```
git clone https://github.com/elijahcruz12/PHP-7-Installer-for-C9.IO.git && cd PHP-7-Installer-for-C9.IO/ && python c9.io.php.py
```

It will clone the script then run it.

## Installing the Script
To install the script use this:
```
git clone https://github.com/elijahcruz12/PHP-7-Installer-for-C9.IO.git
```

## Running the installer
To run the installer just enter on your command line:
```
python c9.io.php.py
```

The script will run for you.

Here is the order of events that take place in the script:

- It will add the repository that has PHP7
- We will `apt-get update`
- Then we will install PHP 7
- After we install that part we will move the envars file to `envars.bak` to prevent errors before changing the `libapache-mod`
- Now we remove `libapache2-mod-php5` and install `libapache2-mod-php7`
- Then the envars file is moved back.
- Now we test your PHP version
- And SUCCESS! You will have PHP 7 With no errors.

## Troubleshooting
If you are having trouble with the script such as errors please feel free to create an issue and I will be glad to respond asap.
