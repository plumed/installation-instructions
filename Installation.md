# Installation

The instructions that follow explain how to configure, compile and install a single version of plumed on a local machine.  For most users the instructions 
below will work fine.  A small fraction of users will want to do something more complicated at install time.  Such users can 
use the "How would you like to build PLUMED" button below to get instructions on what to do in these more exotic cases.  

It is perhaps easiest to install PLUMED using the macports or conda package manager.  For instructions on how to install PLUMED in this way "How would you like to build PLUMED" button. 

You will find a "show defaults" button by the boxes that shows a configure command below.  If you click this button the default flags that are used when that command is executed are shown.
Information on what is controlled by each flag is provided through tooltips, which you are shown if you hover over the flag.  

Some flags are shown in bold in the short versions of the configure commands below.  Clicking on these commands will open a pop-up window that contains further information 
about the flag.  You will most likely not need to worry about the information in these pop ups but it may be worth considering as these options can affect the performance of the
compiled code.

PLUMED can be used in tandem with the MD codes shown in the table on the right below.  To see instructions on what you must do in order have versions
of these codes that work with PLUMED click the checkbox associated with the code you require.  Instructions on patching the code you select with PLUMED 
will appear at the bottom of the web page.

{% raw %}
<style>
  pre {
    overflow-x: auto;
    white-space: pre-wrap;
    white-space: -moz-pre-wrap;
    white-space: -pre-wrap;
    white-space: -o-pre-wrap;
    word-wrap: break-word;
  }
</style>
<script>

var current_instructions="local";

function showInstructions( name ) {
 current_instructions=name;
 var mydiv = document.getElementById("installdiv");
 if( name=="local" ) {
   var mydata1 = document.getElementById("local-1");
   var mydata2 = document.getElementById("config-opts");
   var mydata3 = document.getElementById("compiling");
   var mydata4 = document.getElementById("installing");
   var mydata5 = document.getElementById("testing");
   var mydata6 = document.getElementById("modules-2");
   mydiv.innerHTML = mydata1.innerHTML + mydata2.innerHTML + mydata3.innerHTML + mydata4.innerHTML + mydata5.innerHTML + mydata6.innerHTML;
 } else if( name=="cluster" ) { 
   var mydata1 = document.getElementById("cluster-1");
   var mydata2 = document.getElementById("config-opts");
   var mydata3 = document.getElementById("compiling");
   var mydata4 = document.getElementById("installing");
   var mydata5 = document.getElementById("testing");
   var mydata6 = document.getElementById("modules-1"); 
   var mydata7 = document.getElementById("modules-3");
   mydiv.innerHTML = mydata1.innerHTML + mydata2.innerHTML + mydata3.innerHTML + mydata4.innerHTML + mydata5.innerHTML + mydata6.innerHTML + mydata7.innerHTML; 
 } else if( name=="multiple" ) {
   var mydata1 = document.getElementById("multiple-1");
   var mydata2 = document.getElementById("config-opts");
   var mydata3 = document.getElementById("compiling");
   var mydata4 = document.getElementById("installing");
   var mydata5 = document.getElementById("testing");
   var mydata6 = document.getElementById("modules-1"); 
   var mydata7 = document.getElementById("modules-3"); 
   mydiv.innerHTML = mydata1.innerHTML + mydata2.innerHTML + mydata3.innerHTML + mydata4.innerHTML + mydata5.innerHTML + mydata6.innerHTML + mydata7.innerHTML; 
 } else if( name=="developer" ) {
   var mydata1 = document.getElementById("developer-1");
   var mydata2 = document.getElementById("compiling");
   var mydata4 = document.getElementById("--standalone-executable-content");
   var mydata3 = document.getElementById("developer-2");
   mydiv.innerHTML = mydata1.innerHTML + mydata2.innerHTML + mydata4.innerHTML + mydata3.innerHTML;
 } else if( name=="cross" ) {
   var mydata1 = document.getElementById("cross-1");
   var mydata2 = document.getElementById("config-opts");
   var mydata3 = document.getElementById("compiling");
   var mydata4 = document.getElementById("installing");
   var mydata5 = document.getElementById("cross-testing");
   mydiv.innerHTML = mydata1.innerHTML + mydata2.innerHTML + mydata3.innerHTML + mydata4.innerHTML + mydata5.innerHTML; 
 } else if( name=="python" ) {
   var mydata1 = document.getElementById("python-1");
   var mydata2 = document.getElementById("config-opts");
   var mydata3 = document.getElementById("compiling");
   var mydata4 = document.getElementById("installing");
   var mydata5 = document.getElementById("testing");
   mydiv.innerHTML = mydata1.innerHTML + mydata2.innerHTML + mydata3.innerHTML + mydata4.innerHTML + mydata5.innerHTML; 
 } else {
   showData( name, "installdiv");
 }
}
function showData( name, indiv ) {
 var mydiv = document.getElementById(indiv);
 var mydata = document.getElementById(name);
 mydiv.innerHTML = mydata.innerHTML;
}
function swapConfigure(name) {
 var btn = document.getElementById(name + "_button");
 var mydiv = document.getElementById("conf_" + name); 
 if( btn.textContent=="show defaults" ) { 
   btn.textContent = "hide defaults";
   var dataField = document.getElementById(name + "_long");
   mydiv.innerHTML = dataField.innerHTML;
 } else if( btn.textContent=="hide defaults" ) {
   btn.textContent = "show defaults"; 
   var dataField = document.getElementById(name + "_short");
   mydiv.innerHTML = dataField.innerHTML;
 }
}
function openModal( name ) {
 var mymodal = document.getElementById( name );
 mymodal.style.display = "block";  
}
window.onload = function(event) {
 showInstructions("local");
}
@MODALFUNC@
</script>
<div class="dropdown">
 <button class="dropbtn">How would you like to build PLUMED?</button>
 <div class="dropdown-content">
  <a onclick='showInstructions("local")'>I want to compile a single version of PLUMED on a local machine.</a>
  <a onclick='showInstructions("cluster")'>I want to compile PLUMED on a cluster so it can be used by several users.</a>
  <a onclick='showInstructions("multiple")'>I would like to install multiple versions of PLUMED on a single machine.</a>
  <a onclick='showInstructions("developer")'>I would like to install PLUMED and work on the development of new features.</a>
  <a onclick='showInstructions("cross")'>I would like to cross compile PLUMED.</a>
  <a onclick='showInstructions("macports")'>I would like to install PLUMED using MacPorts.</a>
  <a onclick='showInstructions("conda")'>I would like to install PLUMED using Conda.</a>
  <a onclick='showInstructions("python")'>I would like to call PLUMED from python.</a>
 </div>
</div>
<div style="width: 100%; float:left" id="installdiv"></div>
<div style="display:none;" id="config-opts">
<p>You can control the compilers and compiler flags that are used to build PLUMED by setting the environmental variables. For example, if you wanted to use
the icpc and icc compilers you might use the command shown in the example below:</p>
         
@configure("./configure CXX=icpc CC=icc CXXFLAGS=-O3 LDFLAGS=-L/opt/local/lib CPPFLAGS=-I/opt/local/include LIBS=-lmyxdrfile" copts1)@

<p>You can enable and disable various features within PLUMED by using the --enable-FEATURE and --disable-FEATURE options during the configure step. We would
recommend using a configure command with the following options enabled.</p>

@configure("./configure LIBRARY_PATH=/path --enable-rpath --enable-modules=all --enable-mpi --enable-asmjit --enable-external-lapack --enable-molfile-plugins --prefix=/usr/local" copts2)@
</div>
<div style="display:none;" id="local-1">
<h1> Building PLUMED on a local machine </h1>
<h2>Configuring PLUMED</h2>

<p>The first step in building PLUMED is to configure the makefiles based on the setup of your computer. You can do this by issuing the following command:</p>

@configure("./configure" localinp1)@
</div>
<div style="display:none;" id="multiple-1">
<h1> Building multiple PLUMED versions </h1>
<h2>Configuring PLUMED</h2>

<p>The first step in building PLUMED is to configure the makefiles based on the setup of your computer. If you would like to have multiple versions of the code
installed on your computer, you will also need to give them all different names and place them in different locations. You will thus need to use a configure 
command such as the one below: </p>

@configure("./configure prefix=$HOME/opt --program-suffix=2.2 --program-prefix=mpi-" multiinp1)@

<p>By using this command you ensure that the PLUMED executible will be named <code>mpi-plumed2.2</code> and that other PLUMED files will be named similarly. To load this PLUMED library 
you will thus need to use the flag <code>-lmpi-plumed2.2</code>. PLUMED header files would then be included by using <code>#include <mpi-plumed_2.2/tools/Vector.h></code>.  
It is also possible to use arbitrary scripts to edit the name of the executable by adding the option <code>--program-transform-name=PROGRAM</code> to your configure command.
(see <a href="http://www.gnu.org/software/autoconf/manual/autoconf-2.69/html_node/Transformation-Examples.html#Transformation-Examples"> autoconf documentation </a> for more info).
This options is useful if you do not want to set up modules. As detailed below, however, we believe that using modules is more flexible.</p> 
</div>
<div style="display:none;" id="developer-1">
<h1> Building PLUMED for development purposes </h1>
<h2>Configuring PLUMED</h2>

<p>The first step in building PLUMED is to configure the makefiles based on the setup of your computer. If you are developing PLUMED, we recommend that you configure
using the options below:</p>

@configure("./configure --enable-modules=all --enable-mpi --enable-debug" devinp1)@

<p>Once you are confident that your feature is working correctly you can then reconfigure and compile an optimized version of the code.</p>

<p>You can control the compilers and compiler flags that are used to build PLUMED by setting the environment variables. For example, if you wanted to use
the icpc and icc compilers you might use the command shown in the example below:</p>

@configure("./configure CXX=icpc CC=icc CXXFLAGS=-O3 LDFLAGS=-L/opt/local/lib CPPFLAGS=-I/opt/local/include LIBS=-lmyxdrfile" devinp2)@
</div>
<div style="display:none;" id="developer-2">
<h2> Running PLUMED</h2>

<p>If you are developing PLUMED you are probably compiling the code regularly. You thus might choose to <b>not</b> run the <code>make install</code> command
every time you recompile the code. If you are working in this way and if you use the bash shell you can can run PLUMED from the compilation directory by using the <code>sourceme.sh</code>
file that was created by configure script. This file appears in the main PLUMED directory and can be "sourced" as shown below:</p>
<pre class="fragment">
&gt; source sourceme.sh
</pre>
<p>Running this command ensures that the "plumed" executable appears in your path. To test this executable you might run:</p>
<pre class="fragment">
&gt; plumed -h
</pre>
<h2> Testing PLUMED </h2>
<p>You can test if plumed has been compiled correctly by using the commands:</p>
<pre class="fragment">
&gt; make check
</pre>
<p>Alternatively, you can run all tests using the following command: </p>
<pre class="fragment">
&gt; source sourceme.sh
&gt; cd regtest
&gt; make
</pre>
<p> You can even run a particular test by changing to the directory that contains it and by running the command <code>make</code> within that directory. </p>
<h2> Merging your changes </h2>
<p>Before starting work on a new feature that you plan to share with the PLUMED community we would ask you to read 
<a href="../../developer-doc/html/_how_to_contribute_to_plumed.html">this brief summary of best practise.</a></p>

<p>If you finish your coding a new feature in PLUMED and if you want to share it with the community then you can open a 
<a href="https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request" >pull request</a> on the PLUMED
repository. Before doing so we would ask that you:</p>
<ul>
<li> Write suitable <a href="../../developer-doc/html/using_doxygen.html">documentation</a> for your new feature</li>
<li> Add a new <a href="../../developer-doc/html/regtests.html">regtest or modified an existing regtest</a> to validate your changes</li> 
<li> <a href="../../developer-doc/html/_using_external_libs.html">Modify the configure script</a> so that any libraries your feature uses can be setup at configure time</li>
<li> Check the format of your code using <a href="../../developer-doc/html/_plumedcheck.html">plumedcheck</a> and 
<a href="../..//developer-doc/html/_code_formatting.html">astyle</a></li>
</ul>
</div>
<div style="display:none;" id="cluster-1">
<h1> Building PLUMED on a cluster </h1>
<h2>Some general advice</h2>
<p>If you are compiling PLUMED on a cluster and if several users will take advantage of the code we would recomment that you:</p>
<ul>
<li> Follow the advice given below about using modules and the module file that PLUMED provides to set up the environment. N.B you will need to edit this file to make it suitable for your environment.</li>
<li> Compile with all the modules enabled so that users can use the full range of features. In addition, ensure that features that are provided by specific libraries are enabled. For example, users employing gromacs will likely want to use libxdrfile to write trr/xtc files. If gromacs is installed before PLUMED, and if the location of libxdrfile is provided to PLUMED during the configure stage then this feature will be available.</li>
<li> Try to patch all MD codes using the <code>--runtime</code> option. When codes are patched in this way users are able to combine any of the installed gromacs/amber/etc versions with any of the 
installed PLUMED versions. It is sometimes claimed that statically linked codes are faster. In our experience, however, this is not true. Furthermore, we have found that non-trivial linking issues are often encountered when building static executables because PLUMED is written in C++ and thus requires the appropriate C++ library to be linked as well as other additional libraries (e.g. libxdrfile).</li>
<li> Keep track of the version of PLUMED you used to patch each of the MD codes. You might do this by giving the MD code modules names such as <code>gromacs/4.6.7p2.2.0</code> to indicate that this is gromacs patched with PLUMED 2.2.0. By keeping track of this information you make it more straightforward for users to report errors on our forum.</li>  
<li> Use the environment variables descsribed below to control the compiler flags and to build an optimized executable.</li>
</ul>
<p>Advice on specific topics and architectures is provided by the drop down menu below. If you have advice on compiling PLUMED on specific architecture please share your tricks! 
You can post information in your blog, or ask as to update the list of topics in this dropdown. The advice you can provide others on compiling PLUMED is very useful and we will happily 
post it here. </p>

@computer-data@

<h2>Configuring PLUMED</h2>
<p>As a bare minimum we would recommend using a command like the one shown below when configuring PLUMED on a cluster</p>

@configure("./configure --enable-modules=all --enable-rpath" clustp1)@

<p>The <code>--enable-rpath</code> flag is recommended as by including this flag you ensure that PLUMED will remember the locations of any runtime libraries that were used at compile time.
The locations of these libraries will thus not need to provided at runtime. This trick often does not work for fundamental libraries such as the C++ and MPI library. The PLUMED module 
should thus load the compiler and MPI modules.</p>
</div>
<div style="display:none;" id="cross-1">
<h1>Cross compiling PLUMED</h1>
<h2>Configuring PLUMED</h2>
<p>If you are cross compiling PLUMED on a different machine than you intend to run it on then you will need to begin by configuring using the usual command.</p>

@configure("./configure" cross1)@

<p>You will likely need to use the options detailed below from controlling the compilers and compiler flags as detailed below, however.</p>
</div>
<div style="display:none;" id="cross-testing">
<h2> Testing PLUMED </h2>
<p>If you have compiled the executable on a machine that is different from the one on which you will ultimately run it the 
<code>plumed</code> executable is not available in the compilation environment. You thus cannot perform the regtests on
the machine and you cannot compile the manual.</p>

<p>You might try to run the regtests on the computing nodes in this case. You may need to do some tweaks to get this 
to work as machines where people do cross-compiling often have architectures with limited capabilities on the compute nodes.</p> 

<h2> Patching MD codes with a cross compiled code </h2>
<p>As discussed in the previous section, if PLUMED has been cross compiled the <code>plumed</code> executable is not available in the compilation environment.
You thus cannot run <code>plumed patch</code> on the compiler nodes. It is also likely that it will not be possible to run this command on the compute nodes
as on machines where cross compilation is necessary it is often not possible to fork new processes from the compute nodes. To get around these issues you can 
use the command: </p>
<pre class="fragment">
&gt; plumed-patch 
</pre>
<p>instead. This script provides a "shell only" implementation of <code>plumed patch</code> and thus does not launch of the <code>plumed</code> executable.
You can thus run this command (and patch MD codes) on the compiler nodes. If you have installed PLUMED you can find the <code>plumed-patch</code> code
script (and some other similar shell scripts that allow you to run various plumed command line tools without launching the <code>plumed</code> executable)
in the directory <code>$(prefix)/plumed/plumed-</code>. The reason these files are not included in the execution path (prefix/bin) is to avoid clashes.</p>
</div>
<div style="display:none;" id="compiling">
<h2>Compiling PLUMED</h2>
<p>PLUMED can be compiled using the following command once the <code>configure</code> script has finished running:</p>
<pre class="fragment">
&gt; make -j 4
</pre>
<p>This command compiles the entire code and produces a number of files in the <code>src/lib</code> directory, including the executable
<code>src/lib/plumed</code>. If the shared libraries are enabled a shared libraries called <code>src/lib/libKernel.so</code> should also be generated.
The extension for this file will be <code>.dylib</code> if you are building PLUMED on a Mac. There are some rare occasions when this command fails
because the configure script fails to find some of the required libraries. If this happens you can <a onclick='showData("makefileconf","makeconfdiv")'>edit the Makefile.conf file</a> so that the suitable
compilation options are set up.</p>
<div style="width: 100%; float:left" id="makeconfdiv"></div>
</div>
<div style="display:none;" id="makefileconf">
<p>The most important variables to edit in the Makefile.conf file are:</p>
<ul>
<li> DYNAMIC_LIB : the libraries (e.g. BLAS and LAPACK) that are linked when the the PLUMED library is compiled are listed here.  
Flags such as -L/path/to/xdrfile -lxdrfile that were specified using the environment variables <code>LDFLAGS</code> and <code>LIBS</code> 
in the call to <code>configure</code> will appear here. The fact that the flags specified using <code>LIBS</code> is perhaps confusing but this 
is necessary to keep the configuration files compatible with PLUMED 2.0. Notice that for the PLUMED shared library to be compiled correctly only dynamic libraries should be listed here.</li>
<li> LIBS : the libraries that are needed to patching the MD codes (typically only <code>-ldl</code> which is needed to have functions for dynamic loading) are specified here.</li> 
<li> CPPFLAGS : definitions that are needed to enable specific optional functions (e.g. -D__PLUMED_HAS_XDRFILE to enable the xdrfile library) are specified here.</li>
<li> SOEXT : the extension for shared libraries on your system is specified here. Typically an "so" extension is used on UNIX and a "dylib" extension is used on mac. 
If your system does not support dynamic libraries or if you would like a static executable you can just set this variable blank i.e. <code>SOEXT=</code>. </li>
</ul>
</div>
<div style="display:none;" id="installing">
<h2> Installing PLUMED </h2>
<p>You can install PLUMED using the command:</p>
<pre class="fragment">
&gt; make install
</pre>
<p>or the command:</p>
<pre class="fragment">
&gt; sudo make install
</pre>
<p>If you want to install PLUMED in a system directory. Unless modifications are made to the standard autoconf directories this command copies the 
executable to <code>$(prefix)/bin</code>, the libraries to <code>$(prefix)/lib</code>,
the include files to <code>$(prefix)/include</code>, and the documentation to <code>$(prefix)/shared/doc/plumed</code>. A directory called
<code>$(prefix)/lib/plumed</code> is also created by this command. This directory contains several other files, including
the patch files and the object files that are used for static patching.  
<p><code>$(prefix)</code> here is the directory specified using the <a onclick="openModal('prefix')">--prefix</a> keyword of the configure script.</p>
<p>Once PLUMED has been installed using the <code>make install</code> command you can delete the original compilation directory 
or you can recompile a different PLUMED version in the same place. You should not delete any of the installed files, however, as 
<a onclick="openModal('standaloneexecutable')">PLUMED will not run</a> if there are files missing from these directories</p>
</div>
<div style="display:none;" id="testing">
<h2> Testing PLUMED </h2>
<p>It is important to test PLUMED every time you install PLUMED, as Even though we regularly perform tests on 
<a href="https://github.com/plumed/plumed2/actions">GitHub actions</a>, it is possible that aggressive optimization or even architecture dependent features
trigger bugs that do not show up on GitHub. To test the PLUMED executable that you have installed you should, therefore, type</p>
<pre class="fragment">&gt; make installcheck </pre>
<p>Running this command tells PLUMED to run all the tests in the test suite using the version of PLUMED that was just installed. If you would like to test
PLUMED using some other PLUMED version then you can. The tests can be run using the PLUMED executable that is in your current path by using the commands: </p>
<pre class="fragment">
&gt; cd regtest
&gt; make
</pre>
<p>To determine the version of PLUMED that has been run using the commands above you can use the command:</p>
<pre class="fragment">
&gt; which plumed
</pre>
<p>When you do this you might get certain <a onclick='showData("testerrors","errdiv")'>innocous errors</a></p>
<div style="width: 100%; float:left" id="errdiv"></div>
</div>
<div style="display:none;" id="testerrors">
<p>If you see errors when you run the regression tests using the commands:</p>
<pre class="fragment">
&gt; cd regtest
&gt; make
</pre>
<p>The first thing you should try to work out is the version of PLUMED that is being used to run the tests. When the tests are run 
using the commands above the version of PLUMED that is found in the PATH is used. If the version of PLUMED in your path is not the same
as the version that you just downloaded and compiled then you may observe one of two innocuous errors:</p>
<ul>
<li> If the PLUMED executable in your path is older than the test suite you are running on the tests might fail. In this case the tests
fail as some feature was introduced to PLUMED in a newer version.</li>
<li> The tests might also fail if the PLUMED executable in your path is newer than the test suite. In this case some non-backward compatible change 
 was made in PLUMED. We try to keep the number of non-backward compatible changes small, but as you can see from the <a class="el" href="_change_log.html">ChangeLog</a> there
 are typically a few non-compatable changes at every new major release.</li>
</ul>
</div>
<div style="display:none;" id="modules-1">
<h2>Setting up your environment</h2>
<p>Once the installation and testing has been completed you are ready to use PLUMED. Running PLUMED will be more straightforward if you set up the environment correctly.
If the environment is setup correctly you should be able to:</p>
<ul>
<li> use the <code>plumed</code> executable from the command line. Notice that you can also use this executable before installing. </li>
<li> link against the PLUMED library using the <code>-lplumed</code> flag for the linker. If this flag can be employed then it is possible to use PLUMED library in general purpose programs </li>
<li> use PLUMED internal functionality (C++ classes) including header files such as <code>#include <plumed/tools/Vector.h></code> in general purpose programs </li>
</ul>
</div>
<div style="display:none;" id="modules-2">
<p>The easiest way to setup the environment is to use <a onclick='showData("modules-3","localmoddiv")'>the module framework</a>. If you have installed plumed into a system directory such 
as <code>/usr/local</code> then the environment should already be setup correctly.</p>
<div style="width: 100%; float:left" id="localmoddiv"></div>
</div>
<div style="display:none;" id="modules-3">
<p>The easiest way to setup the environment is to use <a href="http://modules.sourceforge.net">the module framework</a>.  
A suitable module file for PLUMED can be found in <code>$(prefix)/lib/plumed/src/lib/modulefile</code> after installation is completed.
You can edit this file or just put it into your modulefile directory directly. If you do so it is then straightforward to 
set up the environment. </p>
<p> Notice that if you have installed more than one version of PLUMED on your machine you can use the module framework to easily
switch between them. </p> 
<p> Lastly note that even if you do not want to use modules it may still be useful to look at the modulefile as this file will tell 
you which environment variables need to be set for PLUMED to work correctly. </p>
</div>
<div style="display:none;" id="macports">
<h1> Building PLUMED with macports</h1>
<p>If you are using PLUMED on a Mac, you can intall it using MacPorts. To take advantage of this option
you proceed as follows:</p>
<ul>
<li> Install <a href="https://www.macports.org/">MacPorts</a></li> 
<li> Type <code>sudo port install plumed</code></li>
</ul>
<p>The default variant that is installed using <code>sudo port install plumed</code> is shipped as a compiled
binary and is thus significantly faster to install. A number of different PLUMED versions can be installed using MacPorts, however.  
You can get a list of the versions that are available by using the command:</p>

<pre class="fragment">&gt; sudo port info plumed</pre>

<p>The various options that can be viewed using this command allow you to install PLUMED using multiple different compilers.
You can thus install plumed with mpich using the command:</p>

<pre class="fragment">&gt; sudo port install plumed +mpich</pre>

<p>We would recommend using the recent clang compiler instead of native compilers to take advantage of openMP. To install
using this option you can use the command:</p> 

<pre class="fragment">&gt; sudo port install plumed +mpich +clang50</pre>

<p>Notice that support for c++11 with gcc compilers in MacPorts is difficult as it is not possible to 
use the system's c++ library. For this reason, we, therefore, only support the clang compilers. If you are 
interested reading more about this issue we would direct you to 
<a href="https://github.com/macports/macports-ports/pull/1252">this discussion</a> </p> 

<p>In addition to the variants that allow you to use MacPorts with a range of compilers there are also options that 
allow you to compile with debug flags (<code>+debug</code>), to pick a linear algebra library
(e.g. <code>+openblas</code>) and to enable all the optional modules (<code>+allmodules</code>).
You can also install a developer version of PLUMED by using the command: </p> 

<pre class="fragment">&gt; sudo port install plumed-devel</pre>

<p>This developer version is typically a later version of PLUMED that is not yet considered stable. When installing
<code>plumed-devel</code> using MacPorts you can use all the variants that were available for <code>plumed</code> to 
customize the compilation. You cannot, however, install <code>plumed-devel</code> and <code>plumed</code> at the same time.</p>

<p>You can also use MacPorts to install a plumed-patched version of gromacs. To install gromacs patched with a stable version of PLUMED that
was compiled using the clang-5.0 compiler and mpich you would use the following sequence of commands:</p>

<pre class="fragment"> 
&gt; sudo port install plumed +mpich +clang50
&gt; sudo port install gromacs-plumed +mpich +clang50
</pre>

<p>If, by contract, the objective was to use a version of gromacs patched with the development version of PLUMED you would use the commands:</p>

<pre class="fragment">
&gt; sudo port install plumed-devel +mpich +clang50
&gt; sudo port install gromacs-plumed +mpich +clang50
</pre>

<p>Notice that the same compiler variants must be used for gromacs and PLUMED (in this example <code>+mpich +clang50</code>). If gromacs and PLUMED are built using different 
compiler variants then compilation will fail.</p>

<p>The patched version of gromacs that can be installed using MacPorts links PLUMED in runtime mode. The path for libplumedKernel.dylib in the MacPorts tree
is hardcoded, however. As a consequence:<p>

<ul>
<li>If gromacs is run and if the <code>PLUMED_KERNEL</code> environment variable is unset (or set to empty), then the version of PLUMED that was installed using MacPorts is used.</li>
<li>If gromacs is run and if the <code>PLUMED_KERNEL</code> environment variable points to another instance of the PLUMED library then this other instance of PLUMED is used in place of 
the version that was installed using MacPorts</li>
</ul>

<p>Having the <code>PLUMED_KERNEL</code> operate in this way is useful if you are developing PLUMED as you can install gromacs once using MacPorts and then combine it with any version of 
PLUMED on your computer.</p>
</div>
<div style="display:none;" id="conda">
<h1><a class="anchor" id="Installation-conda"></a>Installing PLUMED with conda</h1>
<p>If you use the conda package manager you can quictkly install a pre-compiled PLUMED binary by using the following command: </p>
<pre class="fragment">&gt; conda install -c conda-forge plumed </pre>
<p> Similarly, the python wrappers can be installed by using the command: </p>
<pre class="fragment">&gt; conda install -c conda-forge py-plumed </pre>
<p>These packages are part of <a href="https://anaconda.org/conda-forge">conda-forge</a>. They should thus be binary compatible with other codes from 
the same distribution. Furthermore, it should also be possible to combine the PLUMED kernel installed from conda with an MD code that has been compiled outside 
of conda (or within a different conda environment) if PLUMED is linked in runtime mode. The only variable that you need to set in order to access to the PLUMED kernel 
that is installed through conda is <code>PLUMED_KERNEL</code> (e.g., <code>export PLUMED_KERNEL=/conda/prefix/lib/libplumedKernel.so</code>).</p>

<p>Conda binaries are only available for Linux and macOS. The installed conda binaries were configured using the command:</p>

@configure-conda@

<p> so the features are limited accordindly. Notice that there additional conda packages are available on the <a href="https://anaconda.org/plumed/plumed">plumed</a> channel. 
These packages are for testing only.</p>
</div>
<div style="display:none;" id="python-1">
<h1>Calling PLUMED from python</h1>
<p>It is possible to call PLUMED 2.5 and later versions in a python script. If you would like to do so you simply add the command below in your python script:</p>
<div class="fragment"><div class="line"><a name="l00001"></a><span class="lineno">  1</span>&#160;<span class="keyword">import</span> plumed</div></div>
<p>The interface is designed with developers in mind rather than users as the interface from python to PLUMED is similar to the interface that is used to link PLUMED 
with the various MD codes. If you are only compiling one version of PLUMED you might configure using the command: </p>

@configure("./configure PYTHON_BIN=python3.6 --prefix=$HOME/opt" python1)@

<p>Once you have compiled and installed PLUMED by following the instructions that are laid out in the sections that follow, the python wrappers for PLUMED will be in 
<code>$HOME/opt/plumed/python</code>. To use plumed in a python script the location of these wrappers must be added <code>PYTHONPATH</code> environment variable using
a command such as the one shown below:</p>
<pre class="fragment">
&gt; PYTHONPATH="$HOME/opt/lib/plumed/python:$PYTHONPATH"
</pre>
<p>If you have installed muliple PLUMED versions you might find it easier to install the Python wrappers and PLUMED separately. The simplest way to install the python
wrappers by themselves is with <code>pip</code> as shown below:</p>
<pre class="fragment">
&gt; pip3.6 install --user plumed
</pre>
<p> In the command above the <code>--user</code> flag allows you to install the packages on your home. Notice also that you don't even need to download 
PLUMED in order to install the wrappers. The command above can be run before you configure, compile and install PLUMED. You will, however, need PLUMED 
in order to use it within a python script. You can tell the wrappers where PLUMED is by setting the <code>PLUMED_KERNEL</code> environment variable as shown
below:</p>
<pre class="fragment">
&gt; PLUMED_KERNEL=$HOME/opt/lib/libplumedKernel.so
</pre>
<p>When you install the wrappers in this manner described above you will download those that are packaged on <a href="https://pypi.org/project/plumed/">[Pypi]</a>.
If you want to install the development version of the wrappers using pip you should download the PLUMED repository and use the following commands:</p>
<pre class="fragment">
&gt; pip3.6 install --user cython 
&gt; cd plumed2/python
&gt; make pip
&gt; pip3.6 install --user .
</pre>
<p>You are highly recommended to use a virtualenv when installing the development version as you will then ensure that the code you install does not interfere with the released pacakages.</p>
@MODALSTUFF@
{% endraw %}
