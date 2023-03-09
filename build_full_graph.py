import yaml
import os
import glob

def create_configure( ofile, compcom, ccc ) :
   ccc = ccc.strip()
   #local option_start=`grep -n "Optional Features:" configure_help.log | sed -e s/":Optional Features:"//`
   #local option_end=`grep -n "Some influential environment variables:" configure_help.log | sed -e s/":Some influential environment variables:"//`
   #local noptions=`head -n $(($option_end-2)) configure_help.log | tail -n +$(($option_start+4)) | grep "\-\-enable\-" | wc -l | awk '{print $1}'`

   # Build the links that insert information from the options included
   baseconf="./configure"
   for opt in compcom.replace("./configure","").split() :
       modaln = opt.split("=")[0].replace("-","")
       # Note this shitty fix so we can convert things like CXXFLAGS='-DMPICH_IGNORE_CXX_SEEK&-mt_mpi' to CXXFLAGS="-DMPICH_IGNORE_CXX_SEEK -mt_mpi".
       # Any better ideas? 
       fopt = opt.replace("\'","\"").replace("&"," ")
       baseconf = baseconf + "<b onclick=\'openModal(\"" + modaln + "\")\'>" + fopt + "</b>"

   # And build the expanded version of the configuration that includes the tooltips
   allconf="";
   # for ((i=1;i<$noptions;i++)) ; do
   #     com_start=`head -n $(($option_end-2)) configure_help.log | tail -n +$(($option_start+4)) | grep -n "\-\-enable\-" | head -n $i | tail -n 1 | awk '{print $1}' | sed -e s/":"//`
   #     com_end=`head -n $(($option_end-2)) configure_help.log | tail -n +$(($option_start+4)) | grep -n "\-\-enable\-" | head -n $((i+1)) | tail -n 1 | awk '{print $1}' | sed -e s/":"//`
   #     dataopt=`head -n $(($option_end-2)) configure_help.log | tail -n +$(($option_start+4)) | head -n $(($com_end-1)) | tail -n +$com_start`
   #     # Search for this option in input string
   #     found=0
   #     for opt in "${opts[@]}"; do
   #         substr="$(cut -d'=' -f1 <<<"$opt")"
   #         if [[ "$dataopt" == *"$substr"* ]]; then
   #            found=1
   #            break
   #         fi
   #     done
   #     # Create a tooltip for this option from the help information if it is not included in the input command
   #     if [ $found -eq 0 ] ; then
   #          fff=`echo $dataopt | 
   #               awk '{
   #                 hasdef=0
   #                 tooltip=""
   #                 for(i=1;i<=NF;++i){
   #                     if(nrec==0){ option=$i; } 
   #                     else { tooltip = tooltip " " $i; }                
   # 
   #                     if(founddef==1 && $i=="yes"){printf "<div class=\"tooltip\">%s", option; founddef=0;}
   #                     else if(founddef==1 && $i=="no"){gsub(/enable/,"disable",option); printf "<div class=\"tooltip\">%s", option; founddef=0;}
   #                     else if(founddef==1){printf "<div class=\"tooltip\">%s=%s ",option, $i; founddef=0;}
   #                     else if($i=="default:"){hasdef=1; founddef=1;}
   #                     nrec++;
   #                 }
   #                 if(hasdef==0){ printf "<div class=\"tooltip\">%s", option; }
   #                 printf "<div class=\"right\">%s<i></i></div></div>", tooltip;
   #               }'`
   #          allconf=`echo $allconf $fff`
   #     fi
   # done

   # Write out the button to toggle between versions
   ofile.write("<div style=\"width: 80%; float:left\">Click on the options in the command shown below for more information</div>\n")
   ofile.write("<div style=\"width: 10%; float:left\"><button type=\"button\" id=\"" + ccc + "_button\" onclick=\'swapConfigure(\"" + ccc + "\")\'>hide defaults</button></div>\n")
   # Write out the div that holds the configure command
   ofile.write("<div style=\"width: 100%; float:left\" id=\"conf_" + ccc + "\"></div>\n")
   # Write out the div that will hold the information on the various commands that the user will look at
   ofile.write("<div style=\"width: 100%; float:left\" id=\"" + ccc +"\"></div>\n")
   # This script ensures that the short version of the configure is loaded when the page opens
   # echo '<pre style="width: 97%;" class="fragment"></pre>'
   # echo '<script type="text/javascript">'
   # echo 'if (window.addEventListener) { // Mozilla, Netscape, Firefox'
   # echo "    window.addEventListener('load', "$ccc"_Load, false);"
   # echo '} else if (window.attachEvent) { // IE'
   # echo "    window.attachEvent('onload', "$ccc"_Load);";
   # echo '}'
   # echo 'function '$ccc'_Load(event) {'
   # echo '    swapConfigure("'$ccc'");'
   # echo '}'
   # echo '</script>'
   # Write out the short version of the configure
   ofile.write("<div style=\"display:none;\" id=\"" + ccc + "_short\">\n")
   ofile.write("<pre style=\"width: 97%;\" class=\"fragment\">" + baseconf + "</pre>\n")
   ofile.write("</div>\n")
   # Write out the long version of the configure
   ofile.write("<div style=\"display:none;\" id=\"" + ccc + "_long\">\n")
   ofile.write("<pre style=\"width: 97%;\" class=\"fragment\">" + baseconf + allconf + "</pre>\n")
   ofile.write("</div>\n")

def build_computer_list( ofile ) :
   n=0 
   ofile.write("<script>\nfunction showComputer( name ) {\n")
   ofile.write("  var mydiv = document.getElementById(\"computediv\");\n")
   for computer in os.listdir("computers") :
      if n==0 : ofile.write("if( name==\"" + computer+ "\") {\n")
      else : ofile.write("  } else if( name==\"" + computer + "\") {\n")
      n=1
      ofile.write("    var mydata1 = document.getElementById(\"" + computer + "\");\n")
      ofile.write("    mydiv.innerHTML = mydata1.innerHTML;\n")
   ofile.write("  } else {\n")
   ofile.write("    mydiv.innerHTML = \"\";\n")
   ofile.write("  }\n")
   ofile.write("}\n")
   ofile.write("</script>\n")
   ofile.write("<div class=\"dropdown\">\n")
   ofile.write("  <button class=\"dropbtn\">Select the topic you would like more information about</button>\n")
   ofile.write("  <div class=\"dropdown-content\">\n")
   for computer in os.listdir("computers") :
       cfile = open("computers/" + computer, "r" )
       cinp = cfile.read()
       cfile.close()
       for line in cinp.splitlines() :
           if "@question@" in line : 
              ofile.write("  <a onclick=\'showComputer(\"" + computer + "\")\'>" + line.replace("@question@","") + "</a>\n")
              break  
       cfile.close()
   ofile.write("  </div>\n")
   ofile.write("</div>\n")
   for computer in os.listdir("computers") :
      ofile.write("<div style=\"display:none;\" id=\"" + computer + "\">\n")
      cfile = open("computers/" + computer, "r" )
      cinp = cfile.read()
      cfile.close() 
      for line in cinp.splitlines() :
          if "@configure(" in line :
             inputconf=line.replace("@configure(","").replace(")@","")
             # Create the configure (command below ensure correct interprettation of input)
             create_configure( ofile,  inputconf.split("\"")[1], inputconf.split("\"")[2] )
             # Needs more work here
             ofile.write( line + "\n" )
          elif "@question@" not in line :
             ofile.write( line + "\n" )
      ofile.write("</div>\n") 
   ofile.write("<div style=\"width: 100%; float:left\" id=\"computediv\"></div>\n")


def processInstallation() :
   if not os.path.exists("Installation.md") :
      raise RuntimeError("No Installation.md file found")
   f = open("Installation.md", "r")
   inp = f.read() 
   f.close()

   ofile = open("Installation.md", "w+")
   for line in inp.splitlines() : 
       if line == "@configure-conda@" :
#           concomm=`grep configure $HOME/plumed2/conda/plumed/build.sh`
          concomm="./configure"
#           # Create the configure
          create_configure( ofile, concomm, "condaconf1")
       elif "@configure(" in line :
          inputconf=line.replace("@configure(","").replace(")@","")
          # Create the configure (command below ensure correct interprettation of input)
          create_configure( ofile,  inputconf.split("\"")[1], inputconf.split("\"")[2] )
       elif line=="@computer-data@" : 
          build_computer_list( ofile )
       elif line=="@MODALSTUFF@" : 
          for file in os.listdir("Modals") :
              f = open("Modals/" + file,  "r" )
              content = f.read()
              f.close()
              nfile = file.replace(".md","")
              ofile.write("<div id=\"" + nfile + "\" class=\"modal\">\n")
              ofile.write("<div class=\"modal-content\">\n")
              ofile.write( content )
              ofile.write("</div></div>\n")
       # This builds a function to shut all the modals
       elif line=="@MODALFUNC@" : 
          ofile.write("window.onclick = function(event) {\n")
          for file in os.listdir("Modals") :
              nfile = file.replace(".md","")
              ofile.write( "var " + nfile + "modal = document.getElementById(\"" + nfile + "\");\n" )
              ofile.write( "if ( event.target == " + nfile + "modal ) { " + nfile + "modal.style.display = \"none\"; }\n") 
          ofile.write("}\n")
       else :
          ofile.write(line + "\n")
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

   ofile, efile, inmermaid = open( "NAVIGATION.md", "w+"), open( "EMBED.yml", "a"), False
   for line in inp.splitlines() :
        if "```mermaid" in line :
           inmermaid = True
           ofile.write( line + "\n")
        elif inmermaid and "flowchart TB" in line :
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
