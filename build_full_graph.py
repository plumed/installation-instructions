import yaml
import os
import glob

def processInstallation() :
   if not os.path.exists("Installation.md") :
      raise RuntimeError("No Installation.md file found")
   f = open("Installation.md", "r")
   inp = f.read() 
   f.close()

   ofile = open("Installation.md", "w+")
   for line in inp.splitlines() : 
       if line == "@configure-conda@" :
          pass
#           concomm=`grep configure $HOME/plumed2/conda/plumed/build.sh`
#           # Create the configure
#           create_configure "$concomm" condaconf1
       elif "@configure(" in line :
          pass
#           inputconf=`echo $thisline | sed -e s/"@configure("// | sed -e s/")@"//`
#           # Create the configure (command below ensure correct interprettation of input)
#           confcom=`echo $inputconf | awk -F[\"] '{print $2}'`
#           divname=`echo $inputconf | awk -F[\"] '{print $3}'`
#           create_configure "$confcom" $divname
       elif line=="@computer-data@" : 
          pass
#          build_computer_list()
       elif line=="@MODALSTUFF@" : 
          pass
#          for file in `ls Modals` ; do
#              nfile=`echo ${file/.md/}`
#              echo "<div id=\"$nfile\" class=\"modal\">"
#              echo "<div class=\"modal-content\">"
#              cat Modals/$file
#              echo '</div></div>' 
#          done   
       # This builds a function to shut all the modals
       elif line=="@MODALFUNC@" : 
          pass
#          echo "window.onclick = function(event) {" 
#          for file in `ls Modals` ; do
#              nfile=`echo ${file/.md/}`
#              echo "var "$nfile"modal = document.getElementById("$nfile")"
#              echo "if (event.target == "$nfile"modal) { "$nfile"modal.style.display = \"none\"; }"
#          done 
#          echo "}"
       else :
          ofile.write(line)
   ofile.close()

def addMDCodesToNavigation() :
   if not os.path.exists("md_notes.yml") :
      raise RuntimeError("No md_notes.yml file found")
   stream=open("md_notes.yml", "r")
   mdcodes=yaml.load(stream,Loader=yaml.BaseLoader)
   stream.close()

   f = open( "NAVIGATION.md", "r" )
   inp = f.read()
   f.close()

   ofile, efile, inmermaid = open( "NAVIGATION.md", "w+"), open( "EMBED.yml", "w+"), False
   for line in inp.splitlines() :
        if "```mermaid" in line :
           inmermaid = True
           ofile.write( line + "\n")
           n, inmermaid = 1, True
           for key, value in mdcodes.items() :
               if n==1 :
                  ofile.write("  A[Compiling PLUMED] ==> C" + str(n) + "[Using with " +  key + "]\n")
               else :
                  ofile.write("  A ==> C" + str(n) + "[Using with " +  key + "]\n")
               n = n + 1
        elif inmermaid and "```" in line :
           n, inmermaid = 1, False
           for key, value in mdcodes.items() :
               if value["patch"]=="yes" :
                  ofile.write("  click C" + str(n) + " \"" + key + ".md\" \"" + value["notes"] + "\";\n")
                  pfile = open( key + ".md", "w+" )
                  pfile.write("# Patching " + key + "\n")
                  pfile.write("To use PLUMED with " + key + " you need to use the `plumed patch` script to modify " + key + " before compiling.  This process is not difficult you can simply issue the command: \n")
                  pfile.write("```` \n")
                  pfile.write("plumed-patch --runtime \n")
                  pfile.write("````\n")
                  pfile.write("You then need to select the appropriate version of " + key + " from list of codes that are output. PLUMED currently supports the following versions of " + key + ":\n")
                  versions = glob.glob("~/plumed2/patches/" + key + "*diff")
                  for v in versions : pfile.write("* " + v + "\n")
                  pfile.write("Once this script has completed you then proceed to compile " + key + " as you would normally do.\n")
                  pfile.write("## Patching options\n")
                  pfile.write("The way PLUMED is linked is controlled by a flag that is given to the `plumed patch` command. This flag can be set to any one of the following three options:\n");
                  pfile.write("* _--static_ With this flag PLUMED is linked as a collection of object files. This is only suggested if you absolutely need a static executable. Notice that when this setting is used it is often more difficult to configure the MD code properly as all the libraries that PLUMED depends on need to be specified properly. The `./configure` script does its best to look after all this for you but it cannot solve all the problems you might encounter. For example, we have had reports that this patching mode does not work properly on OSX.\n")
                  pfile.write("* _--shared_ This is the default mode for linking PLUMED. When this option is specified PLUMED is linked as a shared library.  One consequence of this is that when PLUMED is updated, there is no need to recompile the MD code.  Linking with the --shared option is superior to linking with --static as the libraries that PLUMED depends are linked automatically.  If, however, you later remove the directory where the version of PLUMED that you linked with then then MD code will not run anymore.\n")
                  pfile.write("* _--runtime_ If you patch your MD code using this option then you can choose the location of the PLUMED library at runtime by setting the environment variable PLUMED_KERNEL.  This option is probably the most flexible of the three, and we encourage system administrators to use this option when installing PLUMED on shared facilities. When this setting is used it is possible to update the PLUMED library and the MD code separately. Users can, thereore, combine the MD code with different versions of PLUMED at will. If you are using this option we would also recommend using a modulefile to set the runtime environment.\n")
                  pfile.write("Notice that the precise behaviour of the `--static` flag depends on the PLUMED version. For versions of PLUMED earlier than 2.5 there was no possibility to link PLUMED as a static library. In PLUMED 2.5 onwards, however, the `./configure` script tries to set up the system so that a `libplumed.a` file is produced. If an MD code is patched with PLUMED 2.5 or later and the `--static` option the MD code is linked against this static library.  If you wish to revert to the pre-version-2.5 behaviour and to just link with the object files you will need to configure PLUMED using the command:\n")
                  pfile.write("````\n")
                  pfile.write("./configure --disable-static-archive\n")
                  pfile.write("````\n")
                  pfile.close()
               else :
                  efile.write(key + ":\n")
                  efile.write("  location: " + value["site"] + "\n")
                  efile.write("  type: external\n")
                  ofile.write("  click C" + str(n) + " \"" + key + "\" \"" + value["notes"] + "\";\n")
               n = n + 1
           ofile.write( line + "\n" )
        else :
           ofile.write( line + "\n" )
   ofile.close()
   efile.close()

if __name__ == "__main__":
  # Process the navigation file to add all the stuff about the MD codes to the directory
  addMDCodesToNavigation()
  # Process the Installation file
  processInstallation()
