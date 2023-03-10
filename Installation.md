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

@MODALSTUFF@
{% endraw %}
