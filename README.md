# A tutorial on installing PLUMED

This repository contains instructions with various levels of detail for installing PLUMED.

The files InstallationPP.md and linkingPP.md that are shown on the PLUMED website are constructed
using the shell script.  You should not edit these files directly.  You should instead edit the corresponding
Installation.md and linking.md file.  Once you have finished editing these files you can generate the 
InstallationPP.md file by running the following command:

````
./generate_installation_page >> InstallationPP.md
```` 

Plumed must be available in your path to run this command and should ideally have been included in the path by using the command

````
source sourceme.sh
````

You can then add the changed Installation.md and InstallationPP.md files to the repository to rebuild the website.

Notice also that if there is specific information about installing PLUMED on a particular machine you can add an additional file in the computers directory.
