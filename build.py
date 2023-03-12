import yaml
import os
import glob
import urllib.request
import shutil
import zipfile

def read_config_help() :
  # try to download plumed
  try:
    urllib.request.urlretrieve('https://github.com/plumed/plumed2/archive/refs/heads/master.zip', 'file.zip')
  except urllib.error.URLError:
    return
  # try to open the zip file
  try:
    zf = zipfile.ZipFile("file.zip", "r")
  except zipfile.BadZipFile:
    return
  zf.extractall(path="tmpplumed")
  # Get all the help information from the configure script so that we can use it to construct configure commands
  cfile = open("tmpplumed/plumed2-master/configure","r")
  inp = cfile.read()
  cfile.close()

  inoptions, key, desc, keys = False, "", "", {}
  for line in inp.splitlines() :
      if "Optional Features:" in line : 
         inoptions = True
      elif inoptions and "Some influential environment variables:" in line : 
         break
      elif inoptions and len(line.split())>0 :
         if "--disable-option-checking" in line : continue 
         if "--disable-FEATURE" in line : continue
         if "--enable-FEATURE" in line : continue
         first = line.split()[0]
         if "--enable" in first or "--disable" in first :
            if len(key)>0 : 
               keys[key] = desc
               key, desc = line.split()[0], " ".join(line.split()[1:])
            else : key, desc = line.split()[0], " ".join(line.split()[1:]) 
         else : desc += " " + line.strip()
  keys[key] = desc

  # Get the configuration for conda
  bf = open( "tmpplumed/plumed2-master/conda/plumed/build.sh", "r")
  binp, condaconf = bf.read(), ""
  bf.close() 
  for dat in binp.splitlines() :
      if 'configure' in dat : 
         condaconf = dat 
         break 

  # Remove PLUMED once we are done with it
  os.remove("file.zip")
  shutil.rmtree("tmpplumed")
  return keys, condaconf

def create_configure( ofile, compcom, ccc, configflags ) :
   # Build the links that insert information from the options included
   ccc, baseconf = ccc.strip(), "./configure"
   for opt in compcom.replace("./configure","").split() :
       modaln = opt.split("=")[0].replace("-","")
       # Note this shitty fix so we can convert things like CXXFLAGS='-DMPICH_IGNORE_CXX_SEEK&-mt_mpi' to CXXFLAGS="-DMPICH_IGNORE_CXX_SEEK -mt_mpi".
       # Any better ideas? 
       fopt = opt.replace("\'","\"").replace("&"," ")
       baseconf = baseconf + " <b onclick=\'openModal(\"" + modaln + "\")\'>" + fopt + "</b>"

   # And build the expanded version of the configuration that includes the tooltips
   allconf="";
   for key, value in configflags.items() :
       if key in compcom.replace("./configure","") : continue
       # Create a tooltip for this option from the help information
       hasdef, founddef = False, False
       for v in value.split() :
           if founddef and "yes" in v : founddef, allconf = False, allconf + " <div class=\"tooltip\">" + key 
           elif founddef and "no" in v :  founddef, allconf = False, allconf + " <div class=\"tooltip\">" + key.replace("enable","disable") 
           elif founddef : founddef, allconf = False, allconf + " <div class=\"tooltip\">" + key + "=" + v
           elif "default:" in v : hasdef, founddef = True, True 
       if not hasdef : allconf = allconf + " <div class=\"tooltip\">" + key
       allconf = allconf + "<div class=\"right\">" + value + "<i></i></div></div>" 

   # Write out the button to toggle between versions
   ofile.write("<div style=\"width: 90%; float:left\">Click on the options in the command shown below for more information</div>\n")
   ofile.write("<div style=\"width: 10%; float:left\"><button type=\"button\" id=\"" + ccc + "_button\" onclick=\'swapConfigure(\"" + ccc + "\")\'>hide defaults</button></div>\n")
   # Write out the div that holds the configure command
   ofile.write("<div style=\"width: 100%; float:left\" id=\"conf_" + ccc + "\"></div>\n")
   # Write out the div that will hold the information on the various commands that the user will look at
   #ofile.write("<div style=\"width: 100%; float:left\" id=\"" + ccc +"\"></div>\n")
   # Write out the short version of the configure
   ofile.write("<div style=\"display:none;\" id=\"" + ccc + "_short\">\n")
   ofile.write("<pre style=\"width: 97%;\" class=\"fragment\">" + baseconf + "</pre>\n")
   ofile.write("</div>\n")
   # Write out the long version of the configure
   ofile.write("<div style=\"display:none;\" id=\"" + ccc + "_long\">\n")
   ofile.write("<pre style=\"width: 97%;\" class=\"fragment\">" + baseconf + allconf + "</pre>\n")
   ofile.write("</div>\n")

def build_computer_list( ofile, configflags, condaconf ) :
   # Create the divs that hold all the information about the computers
   confg_commands = {}
   for computer in os.listdir("computers") : confg_commands[computer] = processfile( ofile, "computers", computer, configflags, condaconf )
   # Create the script for the dropdown menu that shows what each computer does
   n = 0
   ofile.write("<script>\nfunction showComputer( name ) {\n")
   ofile.write("  var mydiv = document.getElementById(\"computediv\");\n")
   for computer in os.listdir("computers") :
      if n==0 : ofile.write("if( name==\"" + computer+ "\") {\n")
      else : ofile.write("  } else if( name==\"" + computer + "\") {\n")
      n=1
      ofile.write("    var mydata1 = document.getElementById(\"" + computer + "\");\n")
      for configblock in confg_commands[computer] : ofile.write("    showMinimalConfigure(\"" + configblock + "\");\n") 
      ofile.write("    mydiv.innerHTML = mydata1.innerHTML;\n")
   ofile.write("  } else {\n")
   ofile.write("    mydiv.innerHTML = \"\";\n")
   ofile.write("  }\n")
   ofile.write("  showInstructions(current_instructions);\n")
   ofile.write("}\n")
   ofile.write("</script>\n")
   # Create the dropdown menu
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
   ofile.write("<div style=\"width: 100%; float:left\" id=\"computediv\"></div>\n")


def processfile( ofile, dirname, fname, configflags, condaconf ) :
   ofile.write("<div style=\"display:none;\" id=\"" + fname + "\">\n")
   cfile = open( dirname + "/" + fname, "r")
   cinp, config_commands = cfile.read(), []
   cfile.close()
   for line in cinp.splitlines() :
       if line == "@configure-conda@" :
          # Create the configure
          config_commands.append("condaconf1")
          create_configure( ofile, condaconf, "condaconf1", configflags)
       elif "@configure(" in line :
          inputconf=line.replace("@configure(","").replace(")@","")
          config_commands.append(inputconf.split("\"")[2].strip())
          # Create the configure (command below ensure correct interprettation of input)
          create_configure( ofile,  inputconf.split("\"")[1], inputconf.split("\"")[2], configflags )
       elif line=="@computer-data@" :
          build_computer_list( ofile, configflags, condaconf ) 
       elif "@question@" not in line :
          ofile.write( line + "\n" )  
   ofile.write("</div>\n")
   return config_commands

def processInstallation() :
   if not os.path.exists("options.yml") : 
      raise RuntimeError("No options.yml file found")
   stream = open("options.yml", "r")
   options = yaml.load(stream,Loader=yaml.BaseLoader)
   stream.close()

   if not os.path.exists("Installation.md") :
      raise RuntimeError("No Installation.md file found")
   configflags, condaconf = read_config_help()
   f = open("Installation.md", "r")
   inp = f.read() 
   f.close()

   ofile, confg_commands = open("Installation.md", "w+"), {}
   for line in inp.splitlines() : 
       if line=="{% endraw %}" :
          for file in os.listdir("sections" ) : confg_commands[file] = processfile( ofile, "sections", file, configflags, condaconf ) 
          for file in os.listdir("Modals") :
              f = open("Modals/" + file,  "r" )
              content = f.read()
              f.close()
              nfile = file.replace(".md","")
              ofile.write("<div id=\"" + nfile + "\" class=\"modal\">\n")
              ofile.write("<div class=\"modal-content\">\n")
              ofile.write( content )
              ofile.write("</div></div>\n")
          # Build the dropdown menu
          ofile.write("<div class=\"dropdown\">\n")
          ofile.write("  <button class=\"dropbtn\">How would you like to build PLUMED?</button>\n")
          ofile.write("  <div class=\"dropdown-content\">\n")
          for key, value in options.items() : ofile.write("<a onclick=\'showInstructions(\"" + key + "\")\'>" + value["question"] + "</a>\n")
          ofile.write("  </div>\n</div>\n")
          ofile.write("<div style=\"width: 100%; float:left\" id=\"installdiv\"></div>\n")
          # And build all the code for shutting down modals on click
          ofile.write("<script>\nwindow.onclick = function(event) {\n")
          for file in os.listdir("Modals") :
              nfile = file.replace(".md","")
              ofile.write( "var " + nfile + "modal = document.getElementById(\"" + nfile + "\");\n" )
              ofile.write( "if ( event.target == " + nfile + "modal ) { " + nfile + "modal.style.display = \"none\"; }\n") 
          ofile.write("}\n")
          # And the function for showing instructions
          ofile.write("var current_instructions=\"local\";\n\n")
          ofile.write("function showInstructions( name ) {\n")
          ofile.write("current_instructions = name;\n")
          ofile.write("var mydiv = document.getElementById(\"installdiv\");\n") 
          n=0
          for key, value in options.items() :
              if n==0 : 
                 ofile.write("if( name==\"" + key + "\" ) {\n")
              else :
                 ofile.write("} else if( name==\"" + key + "\" ) {\n")
              n, m, pdata = 1, 0, "mydiv.innerHTML ="
              for part in value["sections"] : 
                 if m==0 : pdata = pdata + "document.getElementById(\"" + part + "\").innerHTML"
                 else : pdata = pdata + " + document.getElementById(\"" + part + "\").innerHTML"
                 m = m + 1
              for part in value["sections"] :
                  if part not in confg_commands.keys() : continue
                  for configblock in confg_commands[part] : ofile.write("showMinimalConfigure(\"" + configblock + "\");\n")
              ofile.write( pdata + ";\n")
          ofile.write("  }\n}\n")
          ofile.write("</script>\n\n{% endraw %}\n")
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
                  if n<4 : ofile.write("  A ==> C" + str(n) + "[Using with " +  key + "]\n")
                  else : ofile.write("  C" + str(n-3) + " ==> C" + str(n) + "[Using with " +  key + "]\n")
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
